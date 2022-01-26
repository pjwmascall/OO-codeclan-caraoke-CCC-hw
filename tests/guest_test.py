import unittest
from src.bar import Bar
from src.drinks import Drink
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Phil", 60, Song("Creep", "Radiohead"))

    def test_has_name(self):
        self.assertEqual("Phil", self.guest.name)

    def test_has_wallet(self):
        self.assertEqual(60, self.guest.wallet)

    def test_has_favourite_song_name(self):
        self.assertEqual("Creep", self.guest.favourite_song.name)

    def test_has_favourite_song_artist(self):
        self.assertEqual("Radiohead", self.guest.favourite_song.artist)

    def test_has_sufficient_money_pass(self):
        self.assertEqual(True, self.guest.has_sufficient_money(5))

    def test_has_sufficient_money_fail(self):
        self.assertEqual(False, self.guest.has_sufficient_money(70))

    def test_reduce_wallet(self):
        self.guest.reduce_wallet(20)
        self.assertEqual(40, self.guest.wallet)

    def test_room_has_favourite_song_pass(self):
        song1 = Song("My Sharona", "The Knack")
        song2 = Song("Creep", "Radiohead")
        songs = [song1, song2]
        self.assertEqual("Whoo!", self.guest.cheer(songs))

    def test_room_has_favourite_song_fail(self):
        song1 = Song("My Sharona", "The Knack")
        song2 = Song("Dreams", "Fleetwood Mac")
        songs = [song1, song2]
        self.assertEqual(None, self.guest.cheer(songs))

    def test_buy_drink(self):
        bar = Bar()
        bar.add_drink(Drink("Cola", 3))
        self.guest.buy_drink(bar, "Cola")
        self.assertEqual(3, bar.till)
        self.assertEqual(57, self.guest.wallet)
        self.assertEqual(0, len(bar.drinks))