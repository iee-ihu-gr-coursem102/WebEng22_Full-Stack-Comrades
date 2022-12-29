from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

database = SQLAlchemy()

def create_app():
   app = Flask(__name__)
   
   app.config['SECRET_KEY'] = 'secret-key-goes-here'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nikolai/Downloads/Github/WebEng22_Full-Stack-Comrades/db.sqlite'
   #sqlite:///C:\\Users\\Stella\\Documents\\GitHub\\WebEng22_Full-Stack-Comrades\\db.sqlite

   #from . import db
   database.init_app(app)

   login_manager = LoginManager()
   login_manager.login_view = 'auth.login'
   login_manager.init_app(app)

   from .models import User

   @login_manager.user_loader
   def load_user(id):
      return User.query.get(int(id))

   #with app.app_context():
   #   database.create_all()

   # blueprint for auth routes in our app
   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint)

   # blueprint for non-auth parts of app
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   return app