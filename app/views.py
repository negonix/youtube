from flask import render_template
from app import app, db
from app.models import Video
from datetime import datetime

@app.route("/")
def index():
    video = Video.query.filter_by(id=id).first()
    return render_template("index.html", video=video)

@app.route("/add", methods=["POST"])
def add():
    video = Video(name = "my video", date_added = datetime.now())
    db.session.add(video)
    db.session.commit()