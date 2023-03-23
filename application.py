import os
import json
from flask import Flask, request, render_template, redirect, url_for, session
from service.AnswerService import addAnswerService
from model.Answer import Answer
from model.Question import Question

from service.QuestionService import addQuestion, getQuestion
application = Flask(__name__, static_folder='static', static_url_path='')


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/dashboard")
def login():
    return render_template("index copy.html")


@application.route("/products")
def products():
    return render_template("products.html")


@application.route("/accounts")
def accounts():
    return render_template("accounts.html")

@application.route("/api/question")
def getAllQuestion():
    return getQuestion()
    # return redirect(url_for('index'))

@application.route("/api/sendAnswer", methods=['POST'])
def sendAnswer():
    try:
        requestApi = request.get_json()
        answer=Answer(id=requestApi.get('id'),answer=requestApi.get('answer'))
        addAnswerService(answer)
        return {'state':200}
    except Exception as e:
        return {'state':400,'message':e}
@application.route("/api/addQuestion", methods=['POST'])
def addData():
    try:
        requestApi = request.get_json()
        question=Question(content=requestApi.get('content'),email=requestApi.get('email'))
        if(question.content and question.email and '@' in question.email):
            if(addQuestion(question.content,question.email)):
                return {'state':200}
        return {'state':500}
    except Exception as e:
        return {'state':400,'message':e}
    
# run the app.
if __name__ == "__main__":
    # application.run()
    # application.run(debug=True, host="0.0.0.0", port=8080)
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8081)))