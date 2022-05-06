
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'wififlyfly'

class Question1(FlaskForm):
    answer = StringField('Type 1, 2 or 3', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Question2(FlaskForm):
    answer = StringField('Type 1, 2 or 3', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Question3(FlaskForm):
    answer = StringField('Type 1, 2 or 3', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Question4(FlaskForm):
    answer = StringField('Type 1 or 2', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template("TS_Home.html")

@app.route("/q1", methods=["GET", "POST"])
def question_1_page():
    answer = 0
    form = Question1()
    message = ""
    if form.validate_on_submit():
        answer = form.answer.data
        if answer == "3":
            return redirect("/q2")
    return render_template("TS_Project_Q1.html", answer=answer, form=form, message=message)

@app.route("/q2", methods=["GET", "POST"])
def question_2_page():
    answer = 0
    form = Question2()
    message = ""
    # if form.validate_on_submit():
    #     answer = form.answer.data
    #     if answer == "1":
    #         return redirect("/q2")
    return render_template("TS_Project_Q2.html", answer=answer, form=form, message=message)

@app.route("/q3", methods=["GET", "POST"])
def question_3_page():
    answer = 0
    form = Question3()
    message = ""
    # if form.validate_on_submit():
    #     answer = form.answer.data
    #     if answer == "1":
    #         return redirect("/q2")
    return render_template("TS_Project_Q3.html", answer=answer, form=form, message=message)

@app.route("/q4", methods=["GET", "POST"])
def question_4_page():
    answer = 0
    form = Question4()
    message = ""
    # if form.validate_on_submit():
    #     answer = form.answer.data
    #     if answer == "1":
    #         return redirect("/q2")
    return render_template("TS_Project_Q4.html", answer=answer, form=form, message=message)

if __name__ == "__main__":
    app.run()
