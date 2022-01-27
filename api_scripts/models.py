from api_scripts import db

# our Movie collection
class Movie(db.Document):
    # the id column will be created by mongodb automatically
    name = db.StringField()
    Imdb = db.IntField()
    director = db.StringField()
    language = db.StringField()
    actors = db.ListField()
