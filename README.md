# Movies_api
A CRUD and REST api with mongodb atlas.

## Setup
First import all the python dependencies in your virtual environment or globally by the following command <br>
`    pip install -r requirements.txt`

Now you can run the api server by running the run.py file <br>
`    python -m run`


## Documentation
The root has some information about the api <br>
- `   GET /` will show the following output
<img src='/images/1.png' width=750>


### Read
- `   GET /movies/` will list all movies <br>

<img src='/images/2-1.png' width=750><br>
<img src='/images/2-2.png' width=750><br>

- `   GET /movies/<movieId>` will return the movie with the given id <br>

<img src='/images/3.png' width=750><br>

### Create
- `   POST /createMovie/` will create the movie record with given information in the body and returns the movie<br>

<img src='/images/4-1.png' width=750><br>
<img src='/images/4-2.png' width=750><br>

### Update
- `   POST /movies/<movieId>` updates the information of the given movie and returns the updated movie<br>

<img src='/images/5.png' width=750><br>

### Delete
- `   DELETE /movies/<moviesId>` deletes the movie record with the given id and returns success<br>

<img src='/images/6.png' width=750><br>

#### Note
If in any of the requests, if the movieId doesn't exist then this will be returned <br>

<img src='/images/7.png' width=750><br>
