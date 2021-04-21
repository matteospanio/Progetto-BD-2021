"""
In questo modulo si trovano tutte le route riguardandi l'autenticazione nel sito
"""
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("index.html")


@auth.route('/signup')
def sign_up():
    return render_template("index.html")
