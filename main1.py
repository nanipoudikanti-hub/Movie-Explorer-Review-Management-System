from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Movie API"}


movies = [
    {
        "id": 1,
        "name": "Inception",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 9
    }
]


@app.get("/movies")
def get_movies():
    return movies


@app.get("/movies/filter")
def filter_movies(genre: str = None, language: str = None, rating: int = None):

    filtered_movies = movies

    if genre:
        filtered_movies = [movie for movie in filtered_movies if movie["genre"] == genre]

    if language:
        filtered_movies = [movie for movie in filtered_movies if movie["language"] == language]

    if rating is not None:
        filtered_movies = [movie for movie in filtered_movies if movie["rating"] == rating]

    return filtered_movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return {"message": "Movie not found"}


@app.post("/movie")
def add_movie(data: dict):

    for movie in movies:
        if movie["id"] == data["id"]:
            return {"message": "Movie ID already exists"}

    movies.append(data)

    return {"message": "Movie added successfully"}


@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, data: dict):

    for movie in movies:

        if movie["id"] == movie_id:

            movie["name"] = data["name"]
            movie["genre"] = data["genre"]
            movie["language"] = data["language"]
            movie["rating"] = data["rating"]

            return {"message": "Movie updated successfully"}

    return {"message": "Movie not found"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    for movie in movies:

        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted successfully"}

    return {"message": "Movie not found"}