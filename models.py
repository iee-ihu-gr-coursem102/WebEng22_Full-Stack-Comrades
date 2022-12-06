from flask_login import UserMixin
from . import database

class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True) 
    mail = database.Column(database.String(20))
    username = database.Column(database.String(16), unique=True)
    password = database.Column(database.String(32))

class Preferences(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey(User.id)) 
    city = database.Column(database.String(20))
    university = database.Column(database.String(45))
    department = database.Column(database.String(45))
    year = database.Column(database.Integer())