from flask import Flask
from flask_mongoengine import MongoEngine

# our flask app
app = Flask(__name__)

# This is the address of the free mongodb atlas databse I created
DB_URI = "mongodb+srv://pratyush:puhwJMc2kQTDBfz@cluster0.fxawg.mongodb.net/testDb?retryWrites=true&w=majority"

app.config['MONGODB_SETTINGS'] = {
    "host":DB_URI,
    "db":"testDb",
    "username":"pratyush",
    "password":"puhwJMc2kQTDBfz",
}

db = MongoEngine(app)

# we need to import the routes after creating the flask app
from api_scripts import routes