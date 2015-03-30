# Movie Trailer Website

## Description
Server-side python code to generate a HTML file which shows a bunch movies with some interesting info (obtained from an API) and their posters and
official trailers.

Check out a demo [here](http://guillermogfer.github.io/movie-trailer-website/)

## API
The Movie Database API v3 is used to grab movie's info. It's a cool and simple API that you can use for these purposes. You need to use an API_KEY to
access this API. To ease development, [tmdbsimple](https://github.com/celiao/tmdbsimple/) (a good python wrapper) is used.

In order to get your *API_KEY* visit [the moviedb api website](https://www.themoviedb.org/documentation/api).
Once you have it, open *'external_movie_data.py'* file and modify:

line #9 -> `tmdb.API_KEY = 'YOUR_TMDB_API_KEY'`

## How to use
The project is populated with some of my favourite movies. In order to display your selection, open *'entertainment_center.py'* and modify:

line #36 -> `movies_searchlist = ['the third man', 'modern times', 'cinema paradiso', 'the asphalt jungle', '12 angry men',
                                    "schindler's list", 'Les quatre cents coups ', 'el angel exterminador', 'midnight cowboy',
                                    'the lady from shanghai', 'double indemnity', 'shadow of a doubt', 'M' , 'citizen kane', 'dr strangelove']`

To run the script and build the HTML, open a console and type:

`$ python entertainment_center.py`

In you did set a valid *tmdb API_KEY*, an *'index.html'* would be generated.