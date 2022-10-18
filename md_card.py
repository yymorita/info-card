"""
Provides markdown header card.
"""


class Card:
    """Basic game informaiton"""
    name: str
    cover: str
    artworks: list[str]

    def __init__(self, title, cover, artworks):
        self.name = title
        self.cover = cover
        self.artworks = artworks
