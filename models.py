from flask_login import UserMixin
from . import database

class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True) 
    mail = database.Column(database.String(20))
    username = database.Column(database.String(16), unique=True)
    password = database.Column(database.String(32))

class Dashboard(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey(User.id)) 
    base = database.Column(database.String(45))
    department = database.Column(database.String(45))
    year = database.Column(database.String(4))
    school = database.Column(database.String(45))