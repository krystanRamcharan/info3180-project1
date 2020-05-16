from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,RadioField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location =StringField('location'), validators=[DataRequired()])
    Gender= RadioField('Gender', choices=[('F','Female'),('M','Male')])
    
    
    class MyFile(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])


