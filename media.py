import webbrowser


class Movie():

    """This class provides a way to store movie related information"""    

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                 tagline, genres, release_date, runtime, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.tagline = tagline
        self.genres = genres
        self.release_date = release_date
        self.runtime = runtime
        self.rating = rating        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
