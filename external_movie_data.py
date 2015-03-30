from datetime import datetime
import json
import tmdbsimple as tmdb

# Constants

# 'Themoviedatabase' API KEY
# Get yours in https://www.themoviedb.org/documentation/api
tmdb.API_KEY = 'YOUR_TMDB_API_KEY'
YOUTUBE_BASE_URL = 'https://www.youtube.com/watch?v='
# Sizes array: [u'w92', u'w154', u'w185', u'w342', u'w500', u'w780', u'original']
POSTER_SIZE = 'w342'
IMAGE_BASE_URL = 'http://image.tmdb.org/t/p/'


def get_movie_genres(movie):
    genres_list = []
    genres = movie.genres
    for genre in genres:
        # Get up to 2 genres
        if len(genres_list) < 2:
            genres_list.append(genre['name'])

    return genres_list


def get_movie_trailer_key(movie):
    videos = movie.videos()['results']
    video_trailer_key = ''
    for video in videos:
        if video['site'] == 'YouTube' and video['type'] == 'Trailer':
            video_trailer_key = video['key']
            break

    return video_trailer_key


def get_movie_id(movie_query):
    """Get 'Themoviedb' movie id, to be used to grab movie info.

    Args:
        movie_query (str): Movie title to query in 'Themoviedb'

    Returns:
        int: movie id. -1 if not movie matches.
    """
    search = tmdb.Search()
    search.movie(query=movie_query)
    # Return '-1' if no movie is matched
    id = -1
    # TODO: Improve the result choices catch.
    try:
        # We get the first result as the good one.
        id = search.results[0]['id']
    except Exception, e:
        raise e
    finally:
        return id


def get_movie_info(movie_id):
    """Get 'Themoviedb' movie info.

    Args:
        movie_id (id): 'Themoviedb' movie id

    Returns:
        json: movie info. Empty JSON object if no movie matches
    """
    # Get tmdbsimple movie object
    movie = tmdb.Movies(movie_id)
    movie_json = {}
    try:
        # Retrieve its info
        movie.info()

        # Build custom json
        movie_json['title'] = movie.original_title
        movie_json['tagline'] = movie.tagline
        movie_json['overview'] = movie.overview
        movie_json['runtime'] = movie.runtime
        movie_json['rating'] = movie.vote_average
        movie_json['genres'] = get_movie_genres(movie)

        # Check if grabs a date, otherwise 'strptime' will throw an exception
        release_date = movie.release_date
        movie_json['release_date'] = datetime.strptime(
            release_date, '%Y-%m-%d').strftime('%b %Y') if release_date else ''

        # Get movie trailer, return '' if no trailer is found
        movie_trailer = get_movie_trailer_key(movie)
        movie_json['video_trailer'] = YOUTUBE_BASE_URL + \
            movie_trailer if movie_trailer else ''

        # TODO: don't hard-code image_base_url (rarely changes), could use
        # tmdb.Configuration().info() to get it
        # Get poster image, return image placeholder if no poster is found
        poster_path = movie.poster_path
        movie_json['poster_image'] = IMAGE_BASE_URL + \
            POSTER_SIZE + poster_path if poster_path else 'http://placehold.it/220x342'
    except Exception, e:
        raise e
    finally:
        return json.dumps(movie_json, indent=2)

