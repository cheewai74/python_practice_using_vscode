from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

# @app.route("/")
# @app.route("/index")
# def index():
#     return "<h1>Hello World!</h1>"

from app import routes