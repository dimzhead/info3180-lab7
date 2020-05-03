from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired



class UploadForm(FlaskForm):
    description = StringField('Biographhy', widget=TextArea())
    photo = FileField('Your photo', validators=[
        FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])