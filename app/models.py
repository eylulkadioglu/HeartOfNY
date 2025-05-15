from flask_sqlalchemy import SQLAlchemy
from app import db

class County(db.Model):
    county_id = db.Column(db.Integer, primary_key=True)
    county_name = db.Column(db.String(80), nullable=False)
    societies = db.relationship('Society', backref='county', lazy=True)

    def __repr__(self):
        return f'<County {self.county_name}>'

class Society(db.Model):
    society_id = db.Column(db.Integer, primary_key=True)
    society_name = db.Column(db.String(80), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('county.county_id'), nullable=False)
    website = db.Column(db.String(80), nullable=True)
    location = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Society {self.society_name}>'