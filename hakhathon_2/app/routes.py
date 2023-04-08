import flask
from flask import flash, request, redirect
from sqlalchemy import func

from app import flask_app
from .forms import MyForm
from .models import Question, Player
from app import db


@flask_app.route("/", methods=["GET", "POST"])
def main_page():
    form = MyForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        player = Player.query.filter_by(name=name).first()
        if player:
            return redirect(flask.url_for("user_exist", player_id=player.id))
        else:
            new_player = Player(name=name, password=password)
            db.session.add(new_player)
            db.session.commit()
            flash("New player created successfully!", "success")
            return redirect(flask.url_for("start_game"))

    return flask.render_template("homepage.html", form=form)


@flask_app.route("/start_game")
def start_game():
    return flask.render_template("base.html")


@flask_app.route('/room1', methods=['GET', 'POST'])
def room1():
    questions = Question.query.filter(Question.id.between(1, 5)).all()
    if request.method == 'POST':
        total_correct = 0
        for question in questions:
            answer = request.form.get(str(question.id))
            if answer == question.correct_answer:
                total_correct += 1
        if total_correct >= 3:
            return flask.render_template('winner.html')
        else:
            return flask.render_template('try_again.html')
    return flask.render_template('room1.html', questions=questions)


@flask_app.route('/room2', methods=['GET', 'POST'])
def room2():
    questions = Question.query.filter(Question.id.between(6, 10)).all()
    if request.method == 'POST':
        total_correct = 0
        for question in questions:
            answer = request.form.get(str(question.id))
            if answer == question.correct_answer:
                total_correct += 1
        if total_correct >= 3:
            return flask.render_template('winner.html')
        else:
            return flask.render_template('try_again.html')
    return flask.render_template('room2.html', questions=questions)


# @flask_app.route('/submit', methods=['POST'])
# def submit():
#     total_correct = 0
#     for question in request.form:
#         user_answer = request.form[question]
#         correct_answer = Question.query.filter_by(id=question).first().correct_answer
#         if user_answer == correct_answer:
#             total_correct += 1
#     return f'You got {total_correct} out of {len(request.form)} questions correct!'


@flask_app.route("/user_exist/<int:player_id>")
def continue_game(player_id):
    player = Player.query.get_or_404(player_id)
    return flask.render_template("base.html", player=player)


if __name__ == '__main__':
    flask_app.run(debug=True)
