from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from app.models.user import UserModel
from app.models.athlete import AthleteModel
from app.models.schedule import ScheduleModel
from app.models.exercise import ExerciseModel
from app.models.progress import ProgressModel
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


@app.route('/athletes')
@login_required
def athletes():
    athletes = AthleteModel.query.all()
    return render_template('athletes.html',athletes=athletes)

@app.route('/create')
@login_required
def create_athlete():
    if request.method == 'POST':
        print(type(request.form))
        athlete = AthleteModel(data=request.form.to_dict(flat=False))
        athlete.save_to_db()
        progress_count = request.form['progress_count']
        progress_count = int(progress_count)+1
        try : 
            for i in range(1,progress_count):
                update_date = request.form['update_date[%s]' % str(i)]
                weight = request.form['weight[%s]' % str(i)]
                fat_percentage = request.form['fat_percentage[%s]' % str(i)]
                progress = ProgressModel(update_date=update_date, weight=weight, athlete_id=athlete.id, fat_percentage=fat_percentage)
                progress.save_to_db()
        except Exception as e:
            print(str(e))
        return redirect('/athletes')
    return render_template('create.html')

@app.route('/schedule')
@login_required
def schedule():
    schedules = ScheduleModel.query.all()
    return render_template('schedule.html',schedules=schedules)

@app.route('/create_schedule')
@login_required
def create_schedule():
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        difficulty = request.form['difficulty']
        exercise_count = request.form['exercise_count']
        exercise_count = int(exercise_count)+1
        schedule = ScheduleModel(name=name, duration=duration, difficulty=difficulty)
        schedule.save_to_db()
        try : 
            for i in range(1,exercise_count):
                name = request.form['name[%s]' % str(i)]
                count_set = request.form['count_set[%s]' % str(i)]
                repetitions = request.form['repetitions[%s]' % str(i)]
                exercise = ExerciseModel(name=name, count_set=count_set, schedule_id=schedule.id, repetitions=repetitions)
                exercise.save_to_db()
        except Exception as e:
            print(str(e))


        return redirect('/schedule')
    return render_template('create_schedule.html')


