from database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

class Power (db.Model, SerializerMixin):
    __tablename__="powers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))

    hero = db.relationship('Hero', back_populates="powers")

    def __repr__(self) -> str:
        return f"{self.id},{self.name}, {self.description}" 