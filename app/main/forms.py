from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EditProfileForm(FlaskForm):
    first_name = StringField('Nome', validators=[Length(0, 64)])
    last_name = StringField('Cognome', validators=[Length(0, 64)])
    location = StringField('Località', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Salva')
