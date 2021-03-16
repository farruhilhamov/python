from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "Hello im flask"

@app.route("/login/<name>")
def login(name=None):
    return "Hello im "+name+"!"

@app.route("/site/<name>")
def site(name = "noname"):
    return render_template("index.html",name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()