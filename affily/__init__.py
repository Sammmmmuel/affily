from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SECRET_KEY"] = "13443423234234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from affily import routes