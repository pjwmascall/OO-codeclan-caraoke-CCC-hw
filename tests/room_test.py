import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        # self.song_1 = Song("Highway to Hell", "AC/DC")
        # self.song_2 = Song("The Clansman", "Iron Maiden")
        # self.song_3 = Song("Ace of Spades", "Motorhead")

        # self.songs = [self.song_1, self.song_2, self.song_3]

        # self.jack = Guest("Jack", 20, self.song_1)
        # self.victor = Guest("Victor", 15, self.song_2)
        # self.isa = Guest("Isa", 100, self.song_3)

        # self.guests = [self.jack, self.victor, self.isa]

        # self.winston = Guest("Winston", 10, self.song_2)
        self.room = Room("Room 1", 20, 6)

    def test_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_has_till(self):
        self.assertEqual(0, self.room.till)

    def test_has_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    def test_has_max_guests(self):
        self.assertEqual(6, self.room.max_guests)

    def test_increase_till(self):
        self.room.increase_till(50)
        self.assertEqual(50, self.room.till)

    def test_add_song(self):
        song = Song("Creep", "Radiohead")
        self.room.add_song(song)
        self.assertEqual(1, len(self.room.songs))

    def test_can_add_guest_pass(self):
        guest = Guest("Phil", 60, Song("Creep", "Radiohead"))
        self.assertEqual(True, self.room.can_add_guest(guest))

    def test_can_add_guest_fail_max_capacity(self):
        while (len(self.room.guests) < self.room.max_guests):
            self.room.guests.append("guest")
        guest = Guest("Phil", 60, Song("Creep", "Radiohead"))
        self.assertEqual(False, self.room.can_add_guest(guest))

    def test_can_add_guest_fail_no_money(self):
        guest = Guest("John", 2, Song("My Sharona", "The Knack"))
        self.assertEqual(False, self.room.can_add_guest(guest))

    def test_add_guest(self):
        guest = Guest("Phil", 60, Song("Creep", "Radiohead"))
        self.room.add_guest(guest)
        self.assertEqual(1, len(self.room.guests))

    def test_remove_guest(self):
        guest = Guest("Phil", 60, Song("Creep", "Radiohead"))
        self.room.add_guest(guest)
        self.room.remove_guest(guest)
        self.assertEqual(0, len(self.room.guests))