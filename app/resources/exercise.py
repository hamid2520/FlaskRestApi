#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models.exercise import ExerciseModel
from app.util.logz import create_logger


class Exercise(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('name', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('duration', type=int, required=True,
                        help='Must enter the store id')
    parser.add_argument('count_set', type=int, required=True,
                        help='Must enter the store id')
    parser.add_argument('repetitions', type=int, required=True,
                        help='Must enter the store id')
    parser.add_argument('user_id', type=int, required=True,
                        help='Must enter the store id')

    def __init__(self):
        self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, name, user_id):
        item = ExerciseModel.find_by_name(name, user_id)
        self.logger.info(f'returning item: {item.json()}')
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name, user_id):
        self.logger.info(f'parsed args: {Exercise.parser.parse_args()}')

        if ExerciseModel.find_by_name(name, user_id):
            return {'message': "An exercise with name '{}' already exists.".format(
                name)}, 400
        data = Exercise.parser.parse_args()
        exercise = ExerciseModel(name, data['duration'], data['count_set'], data['repetitions'], data['user_id'])

        # try:
        exercise.save_to_db()
        # except:
        #     return {"message": "An error occurred inserting the exercise."}, 500
        return exercise.json(), 201

    @jwt_required()
    def delete(self, name, user_id):

        exercise = ExerciseModel.find_by_name(name, user_id)
        if exercise:
            exercise.delete_from_db()

            return {'message': 'exercise has been deleted'}


class ExerciseList(Resource):
    @jwt_required()
    def get(self):
        return {
            'items': [item.json() for item in ExerciseModel.query.all()]}
        ##return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
