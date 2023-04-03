#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class ScheduleModel(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    duration = db.Column(db.String(80))
    difficulty = db.Column(db.Integer)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=True)
    athlete = db.relationship('AthleteModel', backref='schedule', primaryjoin='ScheduleModel.athlete_id == AthleteModel.id')

    def __init__(self, name, duration, difficulty):
        self.name = name
        self.duration = duration
        self.difficulty = difficulty


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).last()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
