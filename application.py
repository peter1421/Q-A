from flask import Flask, request, render_template, redirect, url_for, session
import database
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

# run the app.
if __name__ == "__main__":
    # app.debug = True
    t = database.DataBase()
    a=t.show('SELECT * FROM sys.Question;')
    print(a)
    app.run()
    
