#!/usr/bin/python3
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField,SubmitField,EmailField,SelectField,ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    username=StringField(label='用户名',validators=[DataRequired(),Length(max=8,min=3)])
    password=PasswordField(label='密码',validators=[DataRequired(),])
    password2=PasswordField(label='确认密码',validators=([DataRequired(),EqualTo('password')]))
    email=EmailField(label="E-mail",validators=[DataRequired()])
    language = SelectField('Programming Language',choices=[('cpp','C++'),('py','python'),('text','Plain Text')],validators=[DataRequired()])
    submit=SubmitField(label='提交',)
# 下面函数会自动运行
    def validate_username(self,username):
        print("validate",username)
        if username.data=="lbsystem":
            raise ValidationError('The username is exsit')
    # recaptcha=RecaptchaField()


