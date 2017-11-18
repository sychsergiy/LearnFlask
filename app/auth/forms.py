from flask_wtf import Form

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Length


class LoginForm(Form):
    email = StringField('Email', validators=[Length(1, 64), Email()])
    password = PasswordField('Password')
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
