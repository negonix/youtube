from flask import Flask
from flask_cors import CORS
from os import path

BASEDIR = path.dirname(path.dirname(path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

if app.config["ENV"] == "development":
    app.config.from_object("app.config.DevelopmentConfig")
else:
    app.config.from_object("app.config.ProductionConfig")

from app import views
