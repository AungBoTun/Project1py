import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class users(db.Model):
     __tablename__ = "users"
     user_id = db.Column(db.string, primary_key=True)
     email = db.Column(db.String, nullable=False)
     DOB = db.Column(db.String, nullable=False)
     Nationlaity = db.Column(db.Integer, nullable=False)
    
     def add_users(self, user_id, email, DOB,Nationlaity):
        p = user(user_id=user_id,email=email, DOB=DOB,Nationlaity=Nationlaity)
        db.session.add(p)
        db.session.commit()
