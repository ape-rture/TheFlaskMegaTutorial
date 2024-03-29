#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

#database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#user login
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models