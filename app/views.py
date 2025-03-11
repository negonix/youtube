from flask import render_template
from app import app
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")