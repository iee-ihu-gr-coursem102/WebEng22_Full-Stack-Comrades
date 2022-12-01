from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
import sqlite3 as sql
from . import database
from . import db_controller

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    mail = request.form.get('mail')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(mail=mail).first() 

    if user:
        return redirect(url_for('auth.signup'))

    new_user = User(mail = mail, username = username, password = generate_password_hash(password, method='sha256'))

    database.session.add(new_user)
    database.session.commit()

    db_controller.insert_user(mail, username, password)

    return redirect(url_for('auth.login'))
