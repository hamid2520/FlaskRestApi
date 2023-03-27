#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class ProgressModel(db.Model):
    __tablename__ = 'progress'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    fat_percentage = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='progress', primaryjoin='ProgressModel.user_id == UserModel.id')
    update_date = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'weight': self.weight, 'fat_percentage': self.fat_percentage, 'update_date': self.update_date,
                'user_id': self.user_id}

    @classmethod
    def find_by_name(cls, user_id):
        return cls.query.filter_by(user_id=user_id).last()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
