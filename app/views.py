from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from app.models.user import UserModel
from app.forms import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserModel(username=username, password=password)
        user.save_to_db()
        login_user(user)
        return redirect('/')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserModel.query.filter_by(username=username).first()
        if user.check_password(password):
            login_user(user)
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/exercise')
@login_required
def exercise():
    return render_template('create.html')

