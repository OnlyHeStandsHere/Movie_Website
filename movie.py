import webbrowser
import video


class Movie(video.Video):
    '''Movie Class used as a data container for storing information about movies - Inherits from Video'''

    def __init__(self, title, length, storyline, category, poster_link, trailer_link, rating):
        """Constructor Creates a new Movie Object - Inherits from Video"""
        video.Video.__init__(self, title, length, storyline, category)
        self.poster_link = poster_link
        self.trailer_link = trailer_link
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_link)
