from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired



class PropertyForm(FlaskForm):
    title= StringField('Property Title', validators=[DataRequired()])
    description= TextAreaField('Description', validators=[DataRequired()])
    rooms=StringField('Number of Rooms', validators=[DataRequired()])
    bathrooms=StringField('Number of Bathrooms', validators=[DataRequired()])
    price= StringField('Price', validators=[DataRequired()])
    myChoices=('House','Apartment')
    proptype=SelectField( 'Property Type',choices= myChoices, validators= [DataRequired()])
    location= StringField('Location', validators=[DataRequired()])
    photo=FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
    submit= SubmitField('Add Property')
