from flask import request
from api_scripts import app
from api_scripts.models import Movie
import json

@app.route('/')
def main():
    return "Welcome to the Movies api!\nThe movie id is the string in the id attribute of a movie"

@app.route('/movies/')
def get_movies():
    # returns the list of all the movies
    movies = {'movies':json.loads(Movie.objects.to_json())}
    return movies

@app.route('/movies/<movieId>', methods=['GET'])
def get_movie(movieId):
    # returns the movie with the given id
    movie = Movie.objects(id=movieId).first()
    if movie == None:
        # returns error if wrong movieId
        return {'error':'no such movie found'}
    else:
        return json.loads(movie.to_json())

@app.route('/createMovie/', methods=['POST'])
def create_movie():
    # creates a movie with data in the post request body as json
    new_movie = Movie(
        name=request.json['name'],
        Imdb=request.json['Imdb'],
        director=request.json['director'],
        language = request.json['language'],
        actors = request.json['actors'],
    )
    a = new_movie.save()
    return json.loads(a.to_json())

@app.route('/movies/<movieId>', methods=['POST'])
def update_movie(movieId):
    # updating movie data from post request body as json
    movie = Movie.objects(id=movieId).first()
    if movie == None:
        # returns error if wrong movieId
        return {'error':'no such movie found'}
    else:
        if 'name' in request.json.keys():
            movie.name = request.json['name'] 

        if 'Imdb' in request.json.keys():
            movie.Imdb = request.json['Imdb']

        if 'director' in request.json.keys():
            movie.director = request.json['director']

        if 'language' in request.json.keys():
            movie.language = request.json['language']

        if 'actors' in request.json.keys():
            movie.actors = request.json['actors']

        a = movie.save()
        return json.loads(a.to_json())

@app.route('/movies/<movieId>', methods=['DELETE'])
def delete_movie(movieId):
    # deletes movie with given id
    movie = Movie.objects(id=movieId).first()
    if movie == None:
        # returns error if wrong movieId
        return {'error':'no such movie found'}
    else:
        movie.delete()
        return {'status':'success'}