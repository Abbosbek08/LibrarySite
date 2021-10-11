from flask import *
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
login_manager=LoginManager()

def setup_db(app):
  db.app=app
  db.init_app(app)
  login_manager.init_app(app)
  # db.drop_all()
  db.create_all()
@login_manager.user_loader
def load_user(user_id):
    from .models import User
    print(user_id)
    return User.query.filter_by(id=user_id).first()

def create_app():
  app=Flask(__name__)

  app.config["SECRET_KEY"]=os.urandom(32)
  app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///db.sqlite3'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

  login_manager.init_app(app)
  
  from .view import view
  app.register_blueprint(view,url_prefix='/')
  from .auth import auth
  app.register_blueprint(auth,url_prefix='/auth/')
  from .book import book
  app.register_blueprint(book,url_prefix='/book/')

  @app.errorhandler(401)
  def unauthorized(e):
    return redirect('/auth/login')

  return app