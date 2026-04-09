#!/bin/bash
# démarrage app python flask
#
echo "------------- ip machine --------------"
ip a
echo
echo "------------- demarrage --------------"
pkill flask
source /root/scripts-python/projet-flask/env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
#flask run --host=0.0.0.0
nohup flask run --host=0.0.0.0 > /root/scripts-python/projet-flask/nohup.out 2>&1 &
sleep 2
echo "✓ Flask app démarrée sur http://0.0.0.0:5000"
