from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy_utils import IntRangeType
import enum
# from website.auth import login
# from flask import redirect, url_for, request
# from flask_admin.contrib import sqla

# class MicroBlogModelView(sqla.ModelView):
#
#     def is_accessible(self):
#         return login.current_user.is_authenticated
#
#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))


class Gender(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Active(enum.Enum):
    lightly = 'Lightly Active'
    moderately = 'Moderately Active'
    very = 'Very Active'

class Age(enum.Enum):
    teens = 'Teen'
    twenties = '20s'
    thirties = '30s'
    forties = '40s'
    above_50 = 'Above 50'

class Regime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_height = db.Column(db.Float)
    to_height = db.Column(db.Float)
    from_weight = db.Column(db.Float)
    to_weight = db.Column(db.Float)
    gender = db.Column(db.Enum(Gender))
    age = db.Column(db.Enum(Age))
    active = db.Column(db.Enum(Active))
    diet = db.relationship('Diet')
    exercise = db.relationship('Exercise')
    # diet = db.Column(db.String(10000))
    # exercise = db.Column(db.String(10000))


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    regime_id = db.Column(db.Integer, db.ForeignKey('regime.id'))

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    regime_id = db.Column(db.Integer, db.ForeignKey('regime.id'))

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    street = db.Column(db.String(10000))
    zip = db.Column(db.String(10000))
    city = db.Column(db.String(10000))
    country = db.Column(db.String(10000))
    long = db.Column(db.Float)
    lat = db.Column(db.Float)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
