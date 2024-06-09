from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    second_name = StringField('Second name',
                              validators=[DataRequired()])
    email = StringField('E-mail',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired()])
    confirm_password = StringField('Confirm password',
                                   validators=[DataRequired(), EqualTo('password')])
