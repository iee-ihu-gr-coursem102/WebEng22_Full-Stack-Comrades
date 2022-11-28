from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import re, os

db = SQLAlchemy()

def create_app():
   app = Flask(__name__)

   app.config['SECRET_KEY'] = 'secret-key-goes-here'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

   db.init_app(app)

   # blueprint for auth routes in our app
   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint)

   # blueprint for non-auth parts of app
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   return app


#if __name__ == '__main__':
#   create_app().run(debug=True)







   