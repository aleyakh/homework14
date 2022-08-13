from utils import get_movie_by_title, get_movie_year_to_year, get_movie_by_rating, get_movie_by_genre, \
    get_movie_by_options, get_two_actors
from flask import Flask, json

app = Flask(__name__)
#app.json.ensure_ascii = False

@app.get('/movie/<string:title>')
def movie_page(title):
    return get_movie_by_title(title)


@app.get('/movie/<int:year1>/to/<int:year2>')
def movie_year_to_year(year1, year2):
    return json.dumps(get_movie_year_to_year(year1, year2))


@app.get('/rating/<string:rating>')
def rating_page(rating):
    return json.dumps(get_movie_by_rating(rating), ensure_ascii=False)


@app.get('/genre/<string:genre>')
def genre_page(genre):
    return get_movie_by_genre(genre)


print('Шаг 6:')
print(get_movie_by_options('Movie', 2018, 'Action'))
print('Шаг (5 - 1):')
print(get_two_actors('Rose McIver', 'Ben Lamb'))
print('Шаг (5 - 2):')
print(get_two_actors('Jack Black', 'Dustin Hoffman'))
print('')


if __name__ == '__main__':
    app.run()
