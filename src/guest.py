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

    def buy_drink(self, bar, drink_name):
        if bar.has_drink(drink_name):
            price = bar.get_drink_price(drink_name)
            if self.has_sufficient_money(price):
                self.reduce_wallet(price)
                bar.increase_till(price)
                bar.remove_drink(drink_name)