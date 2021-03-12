import os
from flask import Flask, render_template, request, session
from pymongo import MongoClient
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = 'TjockSteffe'

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)         #host uri    
db = client.iSandwichDB                 # Select the database    
sandwich_collection = db.sandwiches     # Select the collection name  
categories_collection = db.categories   # Select the categorys collection
users_collection = db.users             # Select users

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

@app.route("/login_form", methods=['GET']) 
def login_form():
    return render_template("login_form.html")

@app.route("/login", methods=['POST']) 
def login():
    user_name = request.form["user_name"]
    password = request.form["password"]

    user = users_collection.find_one({"user_name":user_name, "password":password})
    if(user is not None):
        session['display_name'] = user.get("display_name")
        return render_template("profile.html")
    else:
        message = "Could not log in user, please try again!"
        return render_template("login_form.html", message=message)

@app.route("/signup_form") 
def signup_form():
    return render_template("signup_form.html")


@app.route("/signup", methods=['POST'])
def signup(): 
    #Adding a new user
    user_name = request.form["user_name"]
    password = request.form["password"]
    display_name = request.form["display_name"]

    # Check if username already exist
    if(users_collection.find_one({"user_name":user_name}) is not None):
        message = "The username is already taken, please choose another one!"
        return render_template("signup_form.html", message=message)
    else:
        users_collection.insert({ "user_name":user_name, "password":password, "display_name":display_name})
        message = "The registration went well, user " + display_name + " is now a member"
        return render_template("signup_form.html", message=message)


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/sandwich_form")
def sandwich_form():
    return render_template("sandwich_form.html")

@app.route("/add_sandwich", methods=['POST'])
def add_sandwich(): 
    #Adding a sandwich  
    sandwich_name = request.form["sandwich_name"]
    description = request.form["description"]
    category = request.form["category"]
    ingredients = request.form["ingredients"]
    instructions = request.form["instructions"]
    image = request.form["image"]
    sandwich_collection.insert({ "sandwich_name":sandwich_name, "description":description, "category":category, "ingredients":ingredients, "instructions":instructions, "image":image})    
    return render_template("sandwich_form.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
