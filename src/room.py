class Room:

    def __init__(self, name, entry_fee, max_guests):
        self.name = name
        self.till = 0
        self.entry_fee = entry_fee
        self.max_guests = max_guests
        self.songs = []
        self.guests = []

    def increase_till(self, amount):
        self.till += amount

    def add_song(self, song):
        self.songs.append(song)

    def can_add_guest(self, guest):
        if len(self.guests) < self.max_guests:
            if guest.has_sufficient_money(self.entry_fee):
                return True
        return False

    def add_guest(self, guest):
        if self.can_add_guest(guest):
            guest.reduce_wallet(self.entry_fee)
            self.increase_till(self.entry_fee)
            self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)