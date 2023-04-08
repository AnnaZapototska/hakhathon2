from app import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    answer1 = db.Column(db.String(255))
    answer2 = db.Column(db.String(255))
    answer3 = db.Column(db.String(255))
    correct_answer = db.Column(db.String(255))

