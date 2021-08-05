from wtforms import Form,StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class addcontent(Form):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
    type = StringField('Type', validators=[DataRequired()])
    add = SubmitField('Add')