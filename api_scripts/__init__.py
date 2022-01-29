from flask import Flask
from flask_mongoengine import MongoEngine

DEV = True

# our flask app
app = Flask(__name__)

# This is the address of the free mongodb atlas databse I created
DB_URI = "mongodb+srv://pratyush:puhwJMc2kQTDBfz@cluster0.fxawg.mongodb.net/testDb?retryWrites=true&w=majority"

if DEV:
    app.config['DEBUG'] = True

app.config['MONGODB_SETTINGS'] = {
    "host":DB_URI,
    "db":"testDb",
    "username":"pratyush",
    "password":"puhwJMc2kQTDBfz",
}

db = MongoEngine(app)

# we need to import the routes after creating the flask app
from api_scripts import routes