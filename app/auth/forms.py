from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Email, Length, Regexp, EqualTo

from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Length(1, 64), Email()])
    password = PasswordField('Password')
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Length(1, 64), Email()])
    username = StringField('Username', validators=[
        Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                              'Usernames must have only letters, '
                              'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password')
    password = PasswordField('New password', validators=[
        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password')
    submit = SubmitField('Update Password')
