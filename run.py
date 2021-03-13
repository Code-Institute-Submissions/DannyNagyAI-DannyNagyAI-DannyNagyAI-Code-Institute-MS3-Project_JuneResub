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


# ------------------------------------------------------------------------------------------------------------
# login
# ------------------------------------------------------------------------------------------------------------

@app.route("/login_form", methods=['GET']) 
def login_form():
    return render_template("login_form.html")

@app.route("/login", methods=['POST']) 
def login():
    # 1. Get the username and password provided from the loginform
    user_name = request.form["user_name"]
    password = request.form["password"]

    # 2. Try to find a matching user from the given username/pwd
    user = users_collection.find_one({"user_name":user_name, "password":password})
    if(user is not None):
        # User is now loged in, setting som session variables (might wanna replace later on)
        session['display_name'] = user.get("display_name")
        session['user_name'] = user.get("user_name")

        # We also want to provide the profile page with the current loged in users sandwiches
        user_sandwiches = sandwich_collection.find({"user_name":user.get("user_name")})

        # Then we send the loged in user to his profile page with his sandwiches to go :-) 
        return render_template("profile.html", user_sandwiches=user_sandwiches)
    else:
        message = "Could not log in user, please try again!"
        return render_template("login_form.html", message=message)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user_name', None)
   session.pop('display_name', None)
   message = "You have been logged out"
   return render_template("login_form.html", message=message)


# ------------------------------------------------------------------------------------------------------------
# Signup
# ------------------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------------------
# Profile Page
# ------------------------------------------------------------------------------------------------------------
@app.route("/profile")
def profile():
    # 1. Get the current loged in user 
    user_name = session["user_name"]     # Note: add som error handeling!

    # We also want to provide the profile page with the current loged in users sandwiches
    user_sandwiches = sandwich_collection.find({"user_name": user_name})

    # Then we send the loged in user to his profile page with his sandwiches to go :-) 
    return render_template("profile.html", user_sandwiches=user_sandwiches)

@app.route("/edit_sandwich")    
def edit_sandwich():    
    #Deleting a Task with various references    
    #key=request.values.get("_id")    
    #sandwich_collection.remove({"_id":ObjectId(key)})    
    return render_template("profile.html")


@app.route("/delete_sandwich")    
def delete_sandwich():    
    #Deleting a Task with various references    
    #key=request.values.get("_id")    
    #sandwich_collection.remove({"_id":ObjectId(key)})    
    return render_template("profile.html")


# ------------------------------------------------------------------------------------------------------------
# Sandwich Page
# ------------------------------------------------------------------------------------------------------------
@app.route("/sandwich_form")
def sandwich_form():
    return render_template("sandwich_form.html")


@app.route("/add_sandwich", methods=['POST'])
def add_sandwich(): 
    # 1. Get the form data for the new sandwich  
    sandwich_name = request.form["sandwich_name"]
    description = request.form["description"]
    category = request.form["category"]
    ingredients = request.form["ingredients"]
    instructions = request.form["instructions"]
    image = request.form["image"]

    # 2. Save the new sandwich to database
    sandwich_collection.insert({ "sandwich_name":sandwich_name, "description":description, "category":category, "ingredients":ingredients, "instructions":instructions, "image":image, "user_name":session['user_name']})    
 
    # 3. Send the user back to profile page with a success-message and a list of the users sandwiches
    message = "Sandwich successfully added"
    user_sandwiches = sandwich_collection.find({"user_name": session["user_name"]})

    return render_template("profile.html", message = message, user_sandwiches = user_sandwiches)

# ------------------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
