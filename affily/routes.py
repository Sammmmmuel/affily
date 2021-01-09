from flask import render_template, url_for, flash, redirect
from affily import app
from affily.forms import RegistrationForm, LoginForm
from affily.models import User, Post

        

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", 'success')
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
