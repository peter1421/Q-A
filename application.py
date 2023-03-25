import os
import json
from flask import Flask, request, render_template, redirect, url_for, session
from database import init
from service.AnswerService import addAnswerService
from model.Answer import Answer
from model.Question import Question
from model.Client import Client
from service.ClientService import  checkClientService

from service.QuestionService import  addQuestionService, getQuestionService
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

# @application.route("/api/temp")
# def userData():
#     return render_template("userData.html")



@application.route("/api/question")
def getAllQuestion():
    return getQuestionService()
    # return redirect(url_for('index'))

@application.route("/api/sendAnswer", methods=['POST'])
def sendAnswer():
    try:
        requestApi = request.get_json()
        if(checkClientService(requestApi.get('ip'))):
            answer=Answer(id=requestApi.get('id'),answer=requestApi.get('answer'))
            addAnswerService(answer)
            return {'state':200}
        return {'state':500}
    except Exception as e:
        return {'state':400,'message':e}
@application.route("/api/addQuestion", methods=['POST'])
def addQuestion():
    try:
        requestApi = request.get_json()
        if(checkClientService(requestApi.get('ip'))):
            question=Question(content=requestApi.get('content'),email=requestApi.get('email'))
            if(question.content and question.email and '@' in question.email):
                if(addQuestionService(question.content,question.email)):
                    return {'state':200}
        return {'state':500}
    except Exception as e:
        return {'state':400,'message':e}

# run the app.
if __name__ == "__main__":
    # application.run()
    # application.run(debug=True, host="0.0.0.0", port=8080)
    init()
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8081)))