#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo,InputRequired


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=6, max=35)])
    email = StringField("Email", validators=[Email()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, max=35),EqualTo("confirm",message='Passwords must match')])
    confirm = PasswordField("confirm", validators=[InputRequired()])
    submit =  SubmitField("ok")