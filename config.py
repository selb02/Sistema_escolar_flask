import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sefd.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# mysql://<username>:<password>@<host>/<db_name>

db = SQLAlchemy(app)    