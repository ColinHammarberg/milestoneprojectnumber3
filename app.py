
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/love_therapy")
def love_therapy():
    therapy = list(mongo.db.therapy.find())
    return render_template("lovetherapy.html", therapy=therapy)

        # register function will create a user and add the user details into the database (Mongodb)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # This check if the user already exists in the databse
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("register.html")

        # signin function will log in the user if it matches any of the users in the database

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # app will check if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "account", username=session["user"]))
            else:
                # Password doesn't match any user in the database
                flash("Incorrect Username")
                return redirect(url_for("signin"))

        else:
            # username doesn't match any user in the database
            flash("Incorrect Username")
            return redirect(url_for("signin"))

    return render_template("signin.html")
            


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
