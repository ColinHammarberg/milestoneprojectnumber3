
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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # This check if the user already exists in the databse
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
            
        if existing_user:
            flash("Username already exists. Please choose another username.")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists. Please choose another email address.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("love_therapy", username=session["user"]))

    return render_template("register.html")



@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
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
                            "love_therapy", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))

@app.route("/add_appointment", methods=["GET", "POST"])
def add_appointment():
    if request.method == "POST":
        digital_meeting = "yes" if request.form.get("digital_meeting") else "no"
        appointments = {
            "meeting_type": request.form.get("meeting_type"),
            "meeting_description": request.form.get("meeting_description"),
            "meeting_reflection": request.form.get("meeting_reflection"),
            "requested_date": request.form.get("requested_date"),
            "digital_meeting": digital_meeting,
            "made_by": session["user"]
        }
        mongo.db.book.insert_one(appointments)
        flash("Your requested therapy session has been registered")
        return redirect(url_for("love_therapy"))

    return render_template("add_appointment.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
