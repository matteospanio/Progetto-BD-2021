"""
In questo modulo si trovano tutte le route riguardandi l'autenticazione nel sito
"""
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . forms import LoginForm, RegistrationForm
from . import auth
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid email or password.')
    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    TODO: creare pagina html corretta e gestire gli input salvandoli nel database,
          eventualmente mandando email di conferma
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats. You are registered!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)