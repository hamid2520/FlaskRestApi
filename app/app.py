#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.resources.exercise import Exercise, ExerciseList
from app.resources.progress import Progress, ProgressList
from app.resources.user import UserRegister, User
from app.config import postgresqlConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"  # Change this!
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    from app.db import db
    db.init_app(app)
    db.create_all()

# jwt = JWT(app, authenticate, identity)  # Auto Creates /auth endpoint
api.add_resource(Exercise, '/exercise/<string:name>/<int:user_id>')
api.add_resource(ExerciseList, '/exercise')
api.add_resource(Progress, '/progress/<int:user_id>')
api.add_resource(ProgressList, '/progress')

api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')

if __name__ == '__main__':
    # TODO: Add swagger integration
    app.run(debug=True)  # important to mention debug=True
