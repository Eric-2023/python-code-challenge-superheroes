from database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

class Hero (db.Model, SerializerMixin):
    __tablename__="heros"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    powers = db.relationship('Power', back_populates='hero')

    def __repr__(self) -> str:
        return f"{self.id},{self.name}, {self.super_name}" 