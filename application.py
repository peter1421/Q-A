from flask import Flask, request, render_template, redirect, url_for, session
import database
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


# run the app.
if __name__ == "__main__":
    application.debug = True
    t = database.DataBase()
    a = t.show('SELECT * FROM sys.Question;')
    print(a)
    application.run(port=5500)
