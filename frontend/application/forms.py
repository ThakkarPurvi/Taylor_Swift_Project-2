from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class CreateUserProfileForm(FlaskForm):
    name = StringField('Type your Name', validators=[DataRequired()])

    submit = SubmitField('Submit your name to share your song')


class CreateSongForm(FlaskForm):
    song_category = SelectField('Select Song Category', validators=[DataRequired()],
                                choices=[
                                    ("EX", "Ex partner"),
                                    ("CP", "Current partner"),
                                    ("ND", "Never dated but...")
                                ]
                                )
    song_description = StringField('Type your Song', validators=[DataRequired()])
    userprofile = SelectField('Select your Name', validators=[DataRequired()], choices=[])

    submit = SubmitField('Submit Song')