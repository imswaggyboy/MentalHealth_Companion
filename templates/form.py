from flask_wtf import FlaskForm
import wtforms
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields.core import Label
from wtforms.validators  import DataRequired, Length, EqualTo, Email

class RegisterationForm(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='Email', validators=[DataRequired(),Email()]
    password = PasswordField(Label='Password', validators=[DataRequired(),Length(min=6, max=16)])
    submit = SubmitField(Label='Sign Up')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Email()]
    password = PasswordField(Label='Password', validators=[DataRequired(),Length(min=6, max=16)])
    submit = SubmitField(Label='Login')