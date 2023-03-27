#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models.progress import ProgressModel
from app.util.logz import create_logger


class Progress(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('weight', type=int, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('fat_percentage', type=int, required=True,
                        help='Must enter the store id')
    parser.add_argument('update_date', type=int, required=True,
                        help='Must enter the store id')
    parser.add_argument('user_id', type=int, required=True,
                        help='Must enter the store id')

    def __init__(self):
        self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self, user_id):
        progress = ProgressModel.find_by_name(user_id)
        self.logger.info(f'returning item: {progress.json()}')
        if progress:
            return progress.json()
        return {'message': 'Progress not found'}, 404

    @jwt_required()
    def post(self, user_id):
        self.logger.info(f'parsed args: {Progress.parser.parse_args()}')
        data = Progress.parser.parse_args()
        exercise = ProgressModel(data['weight'], data['fat_percentage'], data['update_date'], data['user_id'])

        try:
            exercise.save_to_db()
        except:
            return {"message": "An error occurred inserting the progress."}, 500
        return exercise.json(), 201

    @jwt_required()
    def delete(self, user_id):

        progress = ProgressModel.find_by_name(user_id)
        if progress:
            progress.delete_from_db()

            return {'message': 'progress has been deleted'}


class ProgressList(Resource):
    @jwt_required()
    def get(self):
        return {
            'items': [item.json() for item in ProgressModel.query.all()]}
        ##return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
