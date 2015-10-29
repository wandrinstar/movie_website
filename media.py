import webbrowser


class Movie():
    """ This is a class of movies.
    """
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, game):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.game = game
