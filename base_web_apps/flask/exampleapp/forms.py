from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class AddDataForm(FlaskForm):
    print('running add data form')
    data = StringField('data', validators=[Required()])
    submit = SubmitField('Add data')
