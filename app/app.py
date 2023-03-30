#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from flask import Flask, request, render_template
from flask_login import LoginManager
# from flask_jwt_extended import JWTManager
# from flask_restful import Api

from app.resources.exercise import Exercise, ExerciseList
from app.resources.progress import Progress, ProgressList
from app.resources.user import UserRegister, User
from app.config import postgresqlConfig

from app.views import index, signup, login, logout, athletes, create_athlete, schedule, create_schedule
from app.models.user import UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'

# Setup the Flask-login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))


@app.before_first_request
def create_tables():
    from app.db import db
    db.init_app(app)
    db.create_all()

app.add_url_rule('/', 'index', view_func=index)
app.add_url_rule('/login', 'login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/signup', 'signup', view_func=signup, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', view_func=logout)
app.add_url_rule('/athletes', 'athletes', view_func=athletes)
app.add_url_rule('/schedule', 'schedule', view_func=schedule)
app.add_url_rule('/create_athlete', 'create_athlete', view_func=create_athlete, methods=['GET', 'POST'])
app.add_url_rule('/create_schedule', 'create_schedule', view_func=create_schedule, methods=['GET', 'POST'])

if __name__ == '__main__':
    # TODO: Add swagger integration
    app.run(debug=True)  # important to mention debug=True
