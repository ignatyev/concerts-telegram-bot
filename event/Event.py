class Event:
    def __init__(self, time, place, artist, price, genres):
        self.time = time
        self.place = place
        self.artist = artist
        self.price = price
        self.sent_to = []
        self.genres = genres
