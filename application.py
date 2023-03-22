import os
import json
from flask import Flask, request, render_template, redirect, url_for, session
import requests
import bs4

from service.QuestionService import addQuestion, getQuestion
application = Flask(__name__, static_folder='static', static_url_path='')

def get():
    url = "https://forum.gamer.com.tw/C.php?bsn=36730&snA=33353"
    response = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
    root = bs4.BeautifulSoup(response.text, "html.parser")
    print(response)
    # print(root)
    return root

def content(root):
    count = 0
    floor = root.find_all(class_="c-article__content")
    for x in floor:
        count = count+1
        if(count % 2 == 0 and x.text != 'None'):
            lis.append(x.text)

lis = []

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

@application.route("/api/temp")
def temp():
    content(get())
    return lis
    # return redirect(url_for('index'))

@application.route("/api/addQuestion", methods=['POST'])
def addData():
    try:
        requestApi = request.get_json()
        content = requestApi.get('content')
        email = requestApi.get('email')
        print(content)
        print(email)
        if(content and email and '@' in email):
            if(addQuestion(content,email)):
                return redirect("/")
        print('????????')
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        print(data)
        return redirect("/")
# run the app.
if __name__ == "__main__":
    # application.run()
    # application.run(debug=True, host="0.0.0.0", port=8080)
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8081)))