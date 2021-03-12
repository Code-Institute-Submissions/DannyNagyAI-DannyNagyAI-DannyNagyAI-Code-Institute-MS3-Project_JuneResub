import os
from flask import Flask, render_template
from pymongo import MongoClient
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)         #host uri    
db = client.iSandwichDB                 # Select the database    
sandwich_collection = db.sandwiches     # Select the collection name  
categories_collection = db.categories   # Select the categorys collection

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sandwiches")
def sandwiches():
    sandwiches_1 = sandwich_collection.find()
    catogories_1 = categories_collection.find()
    return render_template("sandwiches.html", sandwiches=sandwiches_1, categories=catogories_1)



@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/createsandwich")
def createsandwich():
    return render_template("createsandwich.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
