from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NormForm(FlaskForm):
    title = StringField('Input title for the clothes', validators=[Required()])
    submit = SubmitField('Submit')
