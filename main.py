from utils import get_movie_by_title, get_movie_year_to_year, get_movie_by_rating, get_movie_by_genre
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get('/movie/<string:title>')
def movie_page(title):
    return get_movie_by_title(title)


@app.get('/movie/year/to/year')
def movie_year_to_year():
    return get_movie_year_to_year()


@app.get('/rating/<string:rating>')
def rating_page(rating):
    return get_movie_by_rating(rating)


@app.get('/genre/<string:genre>')
def genre_page(genre):
    return get_movie_by_genre(genre)


if __name__ == '__main__':
    app.run()

