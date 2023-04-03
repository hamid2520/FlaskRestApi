from app.db import db


class AthleteModel(db.Model):
    __tablename__ = 'athlete'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    family = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(11))
    gender = db.Column(db.Integer, nullable=True)
    nationalcode = db.Column(db.String(80))
    fathername = db.Column(db.String(80))


    def __init__(self, **data):
        data = data['data']
        self.name = data['name'][0]
        self.family = data['family'][0]
        self.age = int(data['age'][0])
        self.phone = data['phone'][0]
        self.gender = int(data['gender'][0])
        self.nationalcode = data['nationalcode'][0]
        self.fathername = data['fathername'][0]
        self.height = int(data['height'][0])
        self.weight = int(data['weight'][0])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()