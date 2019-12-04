from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class AppointmentsForm(FlaskForm):
    name = StringField('Customer Name', validators=[DataRequired()])
    start = DateTimeField('Start Date/Time', validators=[DataRequired()])
    end = DateTimeField('End Date/Time', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Add Appointment')

class AppointmentsPageForm(FlaskForm):
    submit = SubmitField('Attend Appointment')
