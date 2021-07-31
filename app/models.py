from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

'''
Concept:

TODO: la gestione del db è fatta in maniera da creare dei link tra
la tabella documenti e le domande salvate nel server come file .json
'''


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role: {self.name}>'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    quizzes = db.relationship('Questionario', backref='owner', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return f'<User: {self.username} with email: {self.email}>'


class Questionario(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    title = db.Column(db.String(64), default='No name')
    description = db.Column(db.Text, default='No description')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    questions = db.relationship('Domanda', backref='comprends', lazy='dynamic')
    answers = db.relationship('Risposta', backref='risposte', lazy='dynamic')  # TODO da rimuovere, è di test

    def __init__(self, title, timestamp, description):
        self.title = title
        self.description = description
        self.timestamp = timestamp

    def __repr__(self):
        return f'<Questionario: {self.title} with {self.id}, owned by: {self.owner_id}>'


class Domanda(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    activable = db.Column(db.Boolean, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    answers = db.relationship('Risposta', backref='risposta', lazy='dynamic')
    # category_id = db.Column(db.Integer, db.ForeignKey('questions_category.id'))
    # type_id = db.Column(db.Integer, db.ForeignKey('questions_type.id'))

    def __init__(self, text, activable):
        self.text = text
        self.activable = activable

    def __repr__(self):
        return f'<Domanda{self.id}: {self.text}>'


class Risposta(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    is_open = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.Text, nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))  # TODO da rimuovere, è una FK per test

    def __init__(self, is_open, text):
        self.text = text
        self.is_open = is_open

    def __repr__(self):
        return f'Risposta: {self.text}'


# callback function for flask_login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))