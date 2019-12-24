from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from flaskget1.Models import User

class RegistrationForm(FlaskForm):
    username =StringField('UserName',
                                validators=[DataRequired(),length(min=4 ,max=20)])
    email =StringField('Email',
                           validators=[DataRequired(),Email()])
    password =PasswordField('Password',
                                  validators=[DataRequired(),length(min=8 ,max=20)])
    confirm_password =PasswordField('ConfirmPassword',
                                  validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('This username is taken.Please choose a different name')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('This email is already used by  another user')

class LoginForm(FlaskForm):
    username =StringField('UserName',
                                     validators=[DataRequired(),length(min=4 ,max=20)] )
    email =StringField('Email',
                            validators=[DataRequired(),Email()])
    password =PasswordField('Password',
                                  validators=[DataRequired(),length(min=4 ,max=20)])
    remember = BooleanField('Remember me')                              
    submit = SubmitField('Login')
    

class UpdateAccountForm(FlaskForm):
    username =StringField('UserName',
                                validators=[DataRequired(),length(min=4 ,max=20)])
    email =StringField('Email',
                           validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('This username is taken.Please choose a different name')

    def validate_email(self,email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()

            if email:
                raise ValidationError('This email is already used by  another user')
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')