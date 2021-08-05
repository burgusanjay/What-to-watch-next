from datetime import datetime
from flask_app import db


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    watched = db.Column(db.String, nullable=False, default='False')

    def __repr__(self):
        return f"Movie('{self.title}', '{self.date_posted}')"


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    watched = db.Column(db.String, nullable=False, default='False')

    def __repr__(self):
        return f"Series ('{self.title}', '{self.date_posted}')"