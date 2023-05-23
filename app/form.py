from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, RadioField, SelectField,
    SelectMultipleField, TextAreaField)
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import ValidationError, DataRequired, Length, Optional
from app.models import Voter


class SurveyForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(max=100)])

    email = EmailField('Email', validators=[DataRequired()])

    age = IntegerField('Age', validators=[Optional()])

    gender = RadioField('Gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('neutral', 'Neutral'),
        ('undisclosed', 'No preference'),
    ], validators=[Optional()])

    path = SelectField(
        'Which web development path do you identify yourself with?',
        choices=[
            # ('', 'Select your path'),
            ('front', 'Front End'),
            ('back', 'Back End'),
            ('full', 'Full Stack'),
        ])

    language = SelectMultipleField(
        'What programming languages do you use?',
        choices=[
            ('js', 'JavaScript'),
            ('ts', 'TypeScript'),
            ('py', 'Python'),
            ('csharp', 'C#'),
            ('java', 'Java'),
            ('other', 'Other'),
        ],
        option_widget=CheckboxInput(),
        widget=ListWidget())

    text_area = TextAreaField('comments')

    submit = SubmitField('Submit')

    def validate_email(self, email):
        voter = Voter.query.filter_by(email=email.data).first()
        if voter is not None:
            raise ValidationError('Email already submitted!')
