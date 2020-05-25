import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


class users(UserMixin, db.Model):
     __tablename__ = "users"
     user_id = db.Column(db.String, primary_key=True)
     email = db.Column(db.String, nullable=False)
     DOB = db.Column(db.String, nullable=False)
     
     def get_id(self):
         return (self.user_id)

     def add_users(user_id, email, DOB):
        p = users(user_id=user_id,email=email, DOB=DOB)
        db.session.add(p)
        db.session.commit()

     
