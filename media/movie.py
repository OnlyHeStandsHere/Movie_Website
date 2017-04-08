import webbrowser
from media import video

class Movie(video.Video):

    def __init__(self, title, length, storyline, category, poster_link, trailer_link, rating):
        video.Video.__init__(self, title, length, storyline, category)
        self.poster_link = poster_link
        self.trailer_link = trailer_link
        self.rating = 'PG-13'

    def show_trailer(self):
        if self.trailer_link is not None:
            webbrowser.open(self.trailer_link)
        else:
            print('Invalid Link')
