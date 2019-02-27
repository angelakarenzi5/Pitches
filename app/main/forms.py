from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Pitch comment', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitchForm(FlaskForm):
    category = SelectField('Category:', choices=[('pickup-lines' , 'Pickup lines'),('Interview-pitch', 'Interview pitch'), ('Promotion-pitch','Promotion pitch')])
    content = TextAreaField ('Pitch', validators = [Required()])
    submit = SubmitField('SUBMIT')