from app import db

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Text, primary_key = True)
    name = db.Column(db.Text)
    date_added = db.Column(db.DateTime)

db.create_all()