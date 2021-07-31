from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . forms import NewQuestion, NewQuestionnaire, OpenQuestionForm, MandatoryQuestionForm
from . import quiz
from ..models import *
from .. import db


@quiz.route('/editor', methods=['GET', 'POST'])
@login_required
def editor():
    form = NewQuestion()
    if form.validate_on_submit():
        activable = False
        domanda = Domanda(form.question.data, form.activable.data)
    return render_template('editor.html', form=form)