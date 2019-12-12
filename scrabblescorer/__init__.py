from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfbslk327yy23i471'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.filters['zip'] = zip
db = SQLAlchemy(app)
db.drop_all()

from scrabblescorer import routes
