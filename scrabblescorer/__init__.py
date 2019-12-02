from flask import Flask
from flask_sqlalchemy import SQLAlchemy

with open('secret_code.txt', 'r') as f:
    message = f.read()

app = Flask(__name__)
app.config['SECRET_KEY'] = message
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.filters['zip'] = zip
db = SQLAlchemy(app)

from scrabblescorer import routes
