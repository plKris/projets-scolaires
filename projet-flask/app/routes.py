from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, Ticket, Chambre, StatusEnum, PriorityEnum
from app.forms import TicketForm, UpdateStatusForm
from app.auth import login_required, admin_required
from sqlalchemy import desc
from sqlalchemy.exc import OperationalError
from datetime import datetime

main_bp = Blueprint('main', __name__)
tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')

# ==================== ACCUEIL ====================

@main_bp.route('/')
@main_bp.route('/accueil')
def accueil():
    """Page d'accueil avec redirection selon le rôle utilisateur"""
    if 'user_id' not in session:
        return render_template('homepage.html')
    
    user_role = session.get('user_role', 'client')
    
    if user_role == 'admin':
        return _afficher_dashboard_admin()
    else:
        return _afficher_dashboard_client()


@main_bp.route('/dmca-security')
def dmca_security():
    """Page de conformité DMCA et sécurité"""
    return render_template('dmca_security.html')


def _afficher_dashboard_admin():
    """Afficher le tableau de bord admin avec statistiques"""
    try:
        tickets = Ticket.query.order_by(desc(Ticket.date_creation)).all()
    except OperationalError:
        tickets = []

    total = len(tickets)
    ouverts = len([t for t in tickets if t.statut == StatusEnum.OUVERT.value])
    en_cours = len([t for t in tickets if t.statut == StatusEnum.EN_COURS.value])
    resolus = len([t for t in tickets if t.statut == StatusEnum.RESOLU.value])

    return render_template('dashboard_admin.html',
                         tickets=tickets,
                         total=total,
                         ouverts=ouverts,
                         en_cours=en_cours,
                         resolus=resolus)


def _afficher_dashboard_client():
    """Afficher le tableau de bord client"""
    chambre_numero = session.get('chambre_numero')
    chambre = Chambre.query.filter_by(numero=chambre_numero).first()
    tickets = Ticket.query.filter_by(chambre_id=chambre.id).all() if chambre else []
    
    return render_template('dashboard_client.html', chambre=chambre, tickets=tickets)

# ==================== TICKETS - CLIENTS ====================

@tickets_bp.route('/creer', methods=['GET', 'POST'])
@login_required
def creer():
    """Créer un nouveau ticket"""
    form = TicketForm()
    chambre = None
    chambres = []
    
    # Déterminer la chambre selon le rôle
    if session.get('user_role') == 'admin':
        chambres = Chambre.query.all()
        if request.method == 'POST':
            chambre_id = request.form.get('chambre_id')
            if not chambre_id:
                flash('Sélectionnez une chambre', 'danger')
                return render_template('tickets/formulaire.html', form=form, chambres=chambres, is_admin=True)
            chambre = Chambre.query.get(int(chambre_id))
    else:
        chambre_numero = session.get('chambre_numero')
        chambre = Chambre.query.filter_by(numero=chambre_numero).first()
        chambres = [chambre] if chambre else []
    
    if not chambre:
        flash('Chambre non trouvée', 'danger')
        return redirect(url_for('main.accueil'))
    
    if form.validate_on_submit():
        try:
            ticket = Ticket(
                titre=form.titre.data,
                description=form.description.data,
                location=form.location.data,
                priorite=form.priorite.data,
                statut=StatusEnum.OUVERT.value,
                chambre_id=chambre.id,
                reporter_email=session.get('email', 'contact@village.fr'),
                createur_id=session.get('user_id') if session.get('user_id') and session.get('user_id') > 0 else None
            )
            db.session.add(ticket)
            db.session.commit()
            flash('✅ Ticket créé avec succès!', 'success')
            return redirect(url_for('main.accueil'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la création: {str(e)}', 'danger')
    
    return render_template('tickets/formulaire.html', form=form, chambre=chambre, chambres=chambres, is_admin=session.get('user_role')=='admin')

@tickets_bp.route('/<int:ticket_id>')
@login_required
def detail(ticket_id):
    """Voir un ticket (lecture seule pour client)"""
    ticket = Ticket.query.get_or_404(ticket_id)
    
    chambre_numero = session.get('chambre_numero')
    if ticket.chambre.numero != chambre_numero and session.get('user_role') != 'admin':
        flash('Accès refusé', 'danger')
        return redirect(url_for('main.accueil'))
    
    return render_template('tickets/detail.html', ticket=ticket)




# ==================== TICKETS - ADMIN ====================

# Alias attendus par les templates (compatibilité)
@tickets_bp.route('/liste')
@login_required
def liste():
    """Liste paginée utilisée par les templates. Accessible uniquement aux admins."""
    if session.get('user_role') != 'admin':
        flash('Accès refusé', 'danger')
        return redirect(url_for('main.accueil'))
    page = request.args.get('page', 1, type=int)
    statut_filter = request.args.get('statut', '', type=str)
    priorite_filter = request.args.get('priorite', '', type=str)

    try:
        if session.get('user_role') == 'admin':
            query = Ticket.query
            if statut_filter:
                query = query.filter_by(statut=statut_filter)
            if priorite_filter:
                query = query.filter_by(priorite=priorite_filter)
            tickets = query.order_by(desc(Ticket.date_creation)).paginate(page=page, per_page=10)
        else:
            # Client: lister ses tickets
            chambre_numero = session.get('chambre_numero')
            chambre = Chambre.query.filter_by(numero=chambre_numero).first()
            if not chambre:
                tickets = Ticket.query.filter_by(chambre_id=0).paginate(page=1, per_page=10)
            else:
                tickets = Ticket.query.filter_by(chambre_id=chambre.id).order_by(desc(Ticket.date_creation)).paginate(page=page, per_page=10)
    except OperationalError:
        tickets = []
        pagination_obj = type('obj', (object,), {
            'items': [],
            'page': 1,
            'pages': 1,
            'has_prev': False,
            'has_next': False,
            'prev_num': None,
            'next_num': None,
            'iter_pages': lambda: []
        })()
        tickets = pagination_obj

    return render_template('tickets/liste.html', tickets=tickets, statut_filter=statut_filter, priorite_filter=priorite_filter)


@tickets_bp.route('/nouveau')
def nouveau():
    """Alias vers la création de ticket (compatibilité templates)."""
    return redirect(url_for('tickets.creer'))


@tickets_bp.route('/<int:ticket_id>/update_status', methods=['GET', 'POST'])
@admin_required
def update_status(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    form = UpdateStatusForm(titre=ticket.titre, description=ticket.description, statut=ticket.statut)
    if form.validate_on_submit():
        # Vérifier si quelque chose a changé
        modifications = []
        if ticket.titre != form.titre.data:
            modifications.append("titre")
        if ticket.description != form.description.data:
            modifications.append("description")
        if ticket.statut != form.statut.data:
            modifications.append("statut")
        
        # Appliquer les modifications
        ticket.titre = form.titre.data
        ticket.description = form.description.data
        ticket.statut = form.statut.data
        
        # Marquer comme modifié par admin si des modifications ont été faites
        if modifications:
            ticket.modifie_par_admin = True
        
        # Ajouter les notes si présentes
        notes = request.form.get('notes')
        if notes and notes.strip():
            ticket.notes = (ticket.notes or '') + f"\n[{datetime.utcnow().strftime('%d/%m/%Y %H:%M')}] {notes.strip()}"
        
        db.session.commit()
        flash('✅ Ticket mis à jour avec succès!', 'success')
        return redirect(url_for('tickets.detail', ticket_id=ticket_id))
    return render_template('tickets/update_status.html', ticket=ticket, form=form)


@tickets_bp.route('/<int:ticket_id>/supprimer', methods=['POST'])
@admin_required
def supprimer(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash('✅ Ticket supprimé', 'success')
    return redirect(url_for('tickets.liste'))
