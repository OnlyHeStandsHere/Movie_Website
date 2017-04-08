class Video():
    """Video Class used to group common elements of a tv-show, movie, or other video together."""

    def __init__(self, title, length, storyline, category):
        """Constructor Creates a new Video Object"""
        self.title = title
        self.length = length
        self.storyline = storyline
        self.category = category

