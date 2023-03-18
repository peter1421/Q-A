import os
from flask import Flask, request, render_template, redirect, url_for, session

from service.QuestionService import getQuestion
application = Flask(__name__, static_folder='static', static_url_path='')


@application.route("/")
def index():
    return render_template("index.html")
    # return render_template("index copy.html")


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

# run the app.
if __name__ == "__main__":
    # application.run()
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))