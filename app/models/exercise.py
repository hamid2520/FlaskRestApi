#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class ExerciseModel(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    count_set = db.Column(db.Integer)
    repetitions = db.Column(db.Integer)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=False)
    schedule = db.relationship('ScheduleModel', backref='exercises', primaryjoin='ExerciseModel.schedule_id == ScheduleModel.id')

    def __init__(self, name, count_set, schedule_id, repetitions):
        self.name = name
        self.count_set = count_set
        self.schedule_id = schedule_id
        self.repetitions = repetitions


    @classmethod
    def find_by_name(cls, name, schedule_id):
        return cls.query.filter_by(name=name, schedule_id=schedule_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
