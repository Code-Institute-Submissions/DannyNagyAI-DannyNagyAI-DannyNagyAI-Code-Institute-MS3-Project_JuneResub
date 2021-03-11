import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sandwiches")
def sandwiches():
    return render_template("sandwiches.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
