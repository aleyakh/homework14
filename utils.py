import sqlite3


def get_movie_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
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


def get_movie_year_to_year():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT title, release_year FROM netflix WHERE release_year BETWEEN 2020 AND 2021 LIMIT 10')
        result = []
        for row in cursor.fetchall():
            sql_dict = {
                        "title": row[0],
                        "release_year": row[1]
                        }
            result.append(sql_dict)
        return result


def get_movie_by_rating(rating):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        if rating == 'children':
            cursor.execute("SELECT title, rating, description FROM netflix WHERE rating = 'G'")
        elif rating == 'family':
            cursor.execute("SELECT title, rating, description FROM netflix WHERE rating IN ('G', 'PG', 'PG-13')")
        elif rating == 'adult':
            cursor.execute("SELECT title, rating, description FROM netflix WHERE rating IN ('R', 'NC-17')")
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
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, description FROM netflix WHERE listed_in LIKE ? LIMIT 10", (genre,))
        result = []
        for row in cursor.fetchall():
            sql_dict = {
                        "title": row[0],
                        "description": row[1]
                        }
            result.append(sql_dict)
        return result