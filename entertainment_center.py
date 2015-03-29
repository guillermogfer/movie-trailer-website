import external_movie_data
import fresh_tomatoes
import json
import media


def validate_movie_info(movie_info):
    # TODO: Aritmethic Error handling
    # Convert and round rating range
    rating = round(movie_info['rating'] * 5 / 10, 1)

    # TODO: Supply the list to the view and loop through it
    # Check if genres list is empty
    genres_list = movie_info['genres'] if movie_info['genres'] else ['Uncategorized']

    # Check if genres list is empty
    overview = movie_info['overview'] if movie_info['overview'] else 'No overview available'

    # Check if tagline is empty
    tagline = movie_info['tagline'] if movie_info['tagline'] else '--'

    return rating, genres_list, overview, tagline


def construct_movie(movie_info, movies_list):
    # Obtain validated movie's info
    rating, genres_list, overview, tagline = validate_movie_info(movie_info)

    # Create a custom media 'Movie' object and populate a list of movies
    movie = media.Movie(movie_info['title'].encode('utf-8'), overview.encode('utf-8'), movie_info['poster_image'],
                        movie_info['video_trailer'], tagline, genres_list, movie_info['release_date'],
                        movie_info['runtime'], rating)
    movies_list.append(movie)

# List of favourite movies, fill in with yours
movies_searchlist = ['the third man', 'modern times', 'cinema paradiso', 'the asphalt jungle', '12 angry men',
                                    "schindler's list", 'Les quatre cents coups ', 'el angel exterminador', 'midnight cowboy',
                                    'the lady from shanghai', 'double indemnity', 'shadow of a doubt', 'M' , 'citizen kane', 'dr strangelove']
# Empty list to be populated with media 'Movie' objects
movies = []

print str(len(movies_searchlist)) + " movies found"
print "Connecting 'themoviedb' to get some movie data.."

# Loop through movies to grab some cool info
for index, movie in enumerate(movies_searchlist):
    index += 1
    movie_id = external_movie_data.get_movie_id(movie)
    if movie_id != -1:
        movie_json = external_movie_data.get_movie_info(movie_id)
        print 'Movie #' + str(index) + ' fetched!'
        # Create own 'Movie' object and append to list
        construct_movie(json.loads(movie_json), movies)

# Call the helper function to build dynamically an static HTML page
fresh_tomatoes.open_movies_page(movies)
