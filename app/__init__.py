from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

if app.config["ENV"] == "development":
    app.config.from_object("app.config.DevelopmentConfig")
else:
    app.config.from_object("app.config.ProductionConfig")

db = SQLAlchemy(app)

from app import views
