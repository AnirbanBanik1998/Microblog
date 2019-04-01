from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Anirban"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "The weather is so cool today!"
        },
        {
            "author": {"username": "Susan"},
            "body": "Python is great, flask is awesome!"
        }
    ]
    return render_template("index.html", user=user, title="Home", posts=posts)


