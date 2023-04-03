#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from app.db import db


class ProgressModel(db.Model):
    __tablename__ = 'progress'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    fat_percentage = db.Column(db.Integer)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=False)
    athlete = db.relationship('AthleteModel', backref='progress', primaryjoin='ProgressModel.athlete_id == AthleteModel.id')
    update_date = db.Column(db.String(80))

    def __init__(self, update_date, weight, fat_percentage, athlete_id):
        self.update_date = update_date
        self.weight = weight
        self.fat_percentage = fat_percentage
        self.athlete_id = athlete_id


    @classmethod
    def find_by_name(cls, athlete_id):
        return cls.query.filter_by(athlete_id=athlete_id).last()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
