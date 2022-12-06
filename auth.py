from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import database
from . import db_controller

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login_post():
    mail = request.form.get('mail')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(mail = mail).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 

    login_user(user, remember = remember)
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

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
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(mail = mail, username = username, password = generate_password_hash(password, method='sha256'))

    database.session.add(new_user)
    database.session.commit()

    db_controller.insert_user(mail, username, password)

    return redirect(url_for('auth.login'))