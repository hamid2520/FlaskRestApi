#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class ExerciseModel(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    count_set = db.Column(db.Integer)
    repetitions = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='exercises', primaryjoin='ExerciseModel.user_id == UserModel.id')

    def __init__(self, name, duration, count_set, user_id, repetitions):
        self.name = name
        self.duration = duration
        self.count_set = count_set
        self.user_id = user_id
        self.repetitions = repetitions


    def json(self):
        return {'name': self.name, 'count_set': self.count_set, 'repetitions': self.repetitions,
                'duration': self.duration, 'user_id': self.user_id}

    @classmethod
    def find_by_name(cls, name, user_id):
        return cls.query.filter_by(name=name, user_id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
