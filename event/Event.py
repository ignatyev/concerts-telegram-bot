class Event:
    def __init__(self, time, place, artist, price):
        self.time = time
        self.place = place
        self.artist = artist
        self.price = price
        self.sent_to = []
