import os

class Config:
    """Configuration de base"""
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'tickets.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev-key-change-in-production'
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Configuration de développement"""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    """Configuration de production"""
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
