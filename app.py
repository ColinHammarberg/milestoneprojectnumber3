
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
                # The choosen password does not exist (function)
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # The choosen username does not exist (function)
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))


    return render_template("signin.html")


# Viewing your own bookings (function)

@app.route("/appointments/", methods=["GET"])
def user_appointments():
    if request.method == "GET":
        appointments = list(mongo.db.appointments.find())
        return render_template("appointments.html", appointments=appointments)


# Logs out the user (function)

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))

# Lets the user/client schedule a meeting (function)

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
        mongo.db.appointments.insert_one(appointments)
        flash("Your requested therapy session has been registered")
        return redirect(url_for("love_therapy"))

    return render_template("add_appointment.html")

    # The application will find the username from the mongo database

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if 'user' in session:
        return render_template("profile.html", username=user['username'], user=user)

    return redirect(url_for("signin"))

    # Lets the user/client contact and registers the email sent (by the form) directly into the database (function)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        emails = {
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "message": request.form.get("message"),
            "made_by": session["user"]
        }
        mongo.db.emails.insert_one(emails)
        flash("Your email was successfully sent")
        return redirect(url_for("love_therapy"))

    return render_template("contact.html")


    # Activates the button to bring the user/client to the terms & condition page

@app.route("/terms", methods=["GET", "POST"])
def terms():
    if request.method == "POST":
        return redirect(url_for("terms"))

    return render_template("terms.html")

    # Deletes the user from the database

@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("We are sad to see you leave, but you have successfully deleted your account")
    session.pop("user")
    return redirect(url_for("register"))

    # Deletes appointment/booking from the database (Not yet completed)

@app.route("/delete_appointment/<appointment_id>")
def delete_appointment(appointment_id):
    mongo.db.appointments.remove({"_id": ObjectId(appointment_id)})
    flash("Your booking has been cancelled")
    return redirect(url_for("add_appointment"))

    # The user/client should be able to change his booking (24 hours before
    #  the set time/date)

@app.route("/edit_appointment/<appointment_id>", methods=["GET", "POST"])
def edit_appointment(appointment_id):
    if request.method == "POST":
        submit = {
            "meeting_type": request.form.get("meeting_type"),
            "meeting_description": request.form.get("meeting_description"),
            "meeting_reflection": request.form.get("meeting_reflection"),
            "requested_date": request.form.get("requested_date"),
            "digital_meeting": digital_meeting,
            "made_by": session["user"]
        }
        mongo.db.appointments.update({"_id": ObjectId(appointment_id)}, submit)    
        flash("You have successfully updated your booking. Your therapist will contact you shortly.")

    appointment = mongo.db.appointments.find_one({"_id": ObjectId(appointment_id)})
    return render_template("edit_appointment.html", appointment=appointment)


        
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
