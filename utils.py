import json
import sqlite3


def sql_connect():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
    return cursor


def get_movie_by_title(title):
    cursor = sql_connect()
    cursor.execute('SELECT title, country, release_year, listed_in, description FROM netflix WHERE title = ?', (title,))
    row = list(cursor.fetchone())
    print(row)
    sql_dict = {
                "title": row[0],
                "country": row[1],
                "release_year": row[2],
                "genre": row[3],
                "description": row[4]
                }
    return sql_dict


def get_movie_year_to_year(year1, year2):
    cursor = sql_connect()
    cursor.execute(f'SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year1} AND {year2} LIMIT 10')
    result = []
    for row in cursor.fetchall():
        sql_dict = {
                    "title": row[0],
                    "release_year": row[1]
                    }
        result.append(sql_dict)
    return result


def get_movie_by_rating(rating):
    cursor = sql_connect()
    if rating == 'children':
        cursor.execute("SELECT title, rating, description FROM netflix WHERE rating = 'G' LIMIT 10")
    elif rating == 'family':
        cursor.execute("SELECT title, rating, description FROM netflix WHERE rating IN ('G', 'PG', 'PG-13')  LIMIT 10")
    elif rating == 'adult':
        cursor.execute("SELECT title, rating, description FROM netflix WHERE rating IN ('R', 'NC-17')  LIMIT 10")
    else:
        return 'Ошибка запроса!'
    result = []
    for row in cursor.fetchall():
        sql_dict = {
                    "title": row[0],
                    "rating": row[1],
                    "description": row[2]
                    }
        result.append(sql_dict)
    return result


def get_movie_by_genre(genre):
    cursor = sql_connect()
    cursor.execute("SELECT title, description FROM netflix WHERE listed_in LIKE '%{s}%' ORDER BY release_year DESC LIMIT 10".format(s=genre))
    result = []
    for row in cursor.fetchall():
        sql_dict = {
                    "title": row[0],
                    "description": row[1]
                    }
        result.append(sql_dict)
        json_result = json.dumps(result)
    return json_result


def get_two_actors(actor_one, actor_two):
    cursor = sql_connect()
    cursor.execute('SELECT "cast" FROM netflix WHERE "cast" LIKE "%{one}%" AND "cast" LIKE "%{two}%"'.format(one=actor_one, two=actor_two))
    count = 0
    result_list = []
    for row_one in cursor.fetchall():
        for row_two in row_one:
            result_one = set(row_two.split(', '))
            result_one = result_one.symmetric_difference([actor_one, actor_two])
            count += 1
        if count > 1:
            result = result.intersection(result_one)
        else:
            result = result_one.copy()
    return result


def get_movie_by_options(kind, year, genre):
    cursor = sql_connect()
    cursor.execute("SELECT title, description FROM netflix WHERE type LIKE '%{t}%' AND release_year = '{y}' AND listed_in LIKE '%{g}%'".format(t=kind, y=year, g=genre))
    result = []
    for row in cursor.fetchall():
        sql_dict = {
                    "title": row[0],
                    "description": row[1]
                    }
        result.append(sql_dict)
        json_result = json.dumps(result)
    return json_result
