from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "13443423234234"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)



if __name__ == "__main__":
    app.run(debug=True)