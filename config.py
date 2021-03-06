"""
Il modulo config è un file di configurazione per le variabili d'ambiente dell'applicazione flask.
All'interno del modulo vengono definite diverse classi per diversificare le variabili a seconda del contesto:

- Config è la classe genitore che contiene alcune variabili comuni a tutti i setup
- DevelopmentConfig è il setup per far eseguire l'applicazione flask in locale
- TestingConfig è il setup per utilizzare un DB SQLite, rapido da creare per fare dei test
- ProductionConfig è la configurazione per il porting online della webapp
"""

import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    QUIZ_MAIL_SUBJECT_PREFIX = '[Quiz4All]'
    QUIZ_MAIL_SENDER = 'Quiz4All Admin <pbaudo15@gmail.com>'
    QUIZ_ADMIN = os.environ.get('QUIZ_ADMIN')
    SSL_REDIRECT = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SQLALCHEMY_RECORD_QUERIES = True
    SESSION_PERMANENT = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # per far girare il DB locale collegato a flask si deve cambiare la url con
    # 'postgresql://<pg_username>:<pg_password>@localhost/<db_name>'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'postgresql://matteo:password@localhost/progetto'


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'postgresql://hrjnlfmdczlyel:1ae6b2d20d995627e46b8f13ec4653fed8abdb0c636e809a4cd4c081d44de52d@ec2-54-164-238-108.compute-1.amazonaws.com:5432/d11v0u9nldbf99'


class HerokuProdConfig(Config):
    DEBUG = False
    # la variabile HEROKU_DATABASE_URL è stata settata nell'ambiente di Heroku
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_DATABASE_URL')
    SSL_REDIRECT = True if os.environ.get('DYNO') else False


config = {
    'development': DevelopmentConfig,
    'production': HerokuProdConfig,
    'test': TestingConfig,

    # a seconda delle necessità si può cambiare il valore della chiave 'default'
    # per un setup rapido è già settato a TestingConfig
    'default': TestingConfig
}
