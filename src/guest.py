class Guest:
    
    def __init__(self, name, wallet, song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = song

    def has_sufficient_money(self, cost):
        return self.wallet >= cost

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def cheer(self, songs):
        for song in songs:
            if song.name == self.favourite_song.name:
                if song.artist == self.favourite_song.artist:
                    return "Whoo!"
        return None