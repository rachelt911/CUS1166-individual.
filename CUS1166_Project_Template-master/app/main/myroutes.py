import app.main
import bp
from flask import Flask, render_template, request, flash, redirect, url_for
import calendar
from app.models import *
import datetime

from flask_wtf import FlaskForm
from sqlalchemy.testing import db
from sqlalchemy.testing.pickleable import User
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired


@bp.route('/testroute', methods=['GET','POST'])
def testroute():
    users = db.session.query(User).all()
    my_user = db.session.query(User).get(0)

    """ appointment = Appointment(
        id = 0,
        start = datetime.datetime(2020, 2, 1),
        end = datetime.datetime(2020, 2, 1),
        name = "Sylvia Jones",
        location = "123 Deer Way, Bronx, NY"
    ) """

    return render_template("test.html", users=users)

    appointment_list = [None] * len(daylist)
    for day_index in range(len(daylist)):
        if daylist[day_index] != 0:
            day = datetime.datetime(year, month, daylist[day_index])
            appointment_list[day_index] = Event.query.filter(Event.start >= day, Appointment.start < day+day_delta, Event.attending_user.any(User.id==current_user_id)).all()
    return render_template("appointment-list.html", now=now, month_name=month_name, month=month, year=year, daylist=daylist, appointment_list=appointment_list)


class AppointmentsPageForm(object):
    pass

class AppointmentsForm(FlaskForm):
    name = StringField('Customer Name', validators=[DataRequired()])
    start = DateTimeField('Start Date/Time', validators=[DataRequired()])
    end = DateTimeField('End Date/Time', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Add Appointment')


@bp.route('/appointments_page', methods=['GET', 'POST'])
def appointments_page(AttendAppointment):
    form = AppointmentsPageForm()
    if form.validate_on_submit():
        appointment_id = request.form['appointment.id']
        attend = AttendAppointment(user_id=0, appointment_id=appointment_id)
        flash('Test')
    appointments = AppointmentsForm.query.all()
    return render_template('appointments-list.html', appointments=appointments, form=form)

@bp.route('/add_appointments', methods=['GET', 'POST'])
def add_appointments():
    appointments_form = AppointmentsForm()
    if appointments_form.validate_on_submit():
        appointment = AppointmentsForm(start=appointments_form.start.data, end=appointments_form.end.data, name=appointments_form.name.data, location=appointments_form.location.data)
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment Added.')
    return render_template('add_appointments.html', appointments_form=appointments_form)