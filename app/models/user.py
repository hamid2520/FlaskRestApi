#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db
from werkzeug.security import hmac


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    # pid
    # phone
    # gender
    # date_reg


    def __init__(self, username, password, age, height, weight):
        self.username = username
        self.password = password
        self.age = age
        self.height = height
        self.weight = weight


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return hmac.compare_digest(self.password, password)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

