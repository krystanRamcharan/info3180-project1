from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER']='./uploads'




db= SQLAlchemy(app)
migrate= Migrate(app, db)

from app import views
