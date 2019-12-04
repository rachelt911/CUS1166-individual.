from flask_sqlalchemy import SQLAlchemy

#from app import db
db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    name = db.Column(db.String)
    location = db.Column(db.String)
    categories = db.relationship('Category', secondary='appointmentCategory', back_populates="appointments")
    def conflicts_with_appointment(self, appointment):
        return self.start<=appointment.end and appointment.start<=self.end

class AppointmentCategory(db.Model):
    __tablename__ = 'appointmentCategory'
    event_id = db.Column(
     db.Integer,
     db.ForeignKey('appointment.id'),
     primary_key=True
    )
    category_id = db.Column(
     db.Integer,
     db.ForeignKey('category.id'),
     primary_key=True
    )

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    events = db.relationship('Appointment', secondary='appointmentCategory', back_populates="categories")

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    appointments = db.relationship('Appointment', secondary='attendAppointment', back_populates="attending_user")
    def attend_appointment(self, appointment):
        # checks if appointment conflicts with any other appointment
        #   adds appointment to the user's appointment list
        conflicts = False;
        userAttendAppointment = self.appointments
        print(userAttendAppointment)
        for x in userAttendAppointment:
            if x.conflicts_with_appointment(appointment):
                conflicts = True
        if conflicts:
            return False
        else:
            self.appointments.append(appointment)
            db.session.add(appointment)
            db.session.add(self)
            db.session.commit()
            return True


class AttendAppointment(db.Model):
    __tablename__ = 'attendAppointment'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), primary_key=True)