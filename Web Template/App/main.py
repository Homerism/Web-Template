from flask_cors import CORS
from flask import Flask
from App.database import db, create_db
from importlib import import_module
from App.models import models
from App.views import views

''' Begin boilerplate code '''

def add_views(app):
    for view in views:
        app.register_blueprint(view)

def add_models(app):
    for model_name in models:
        module = import_module(f'App.models.{model_name}')

def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  CORS(app)
  db.init_app(app)
  add_views(app)
  add_models(app)
  create_db(app)
  app.app_context().push()

  return app

''' End Boilerplate Code '''


# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8080, debug=True)
