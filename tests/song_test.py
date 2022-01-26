import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Creep", "Radiohead")

    def test_song_has_name(self):
        self.assertEqual("Creep", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Radiohead", self.song.artist)