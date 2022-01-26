import unittest
from src.bar import Bar
from src.drinks import Drink

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar()

    def test_has_till(self):
        self.assertEqual(0, self.bar.till)

    def test_increase_till(self):
        self.bar.increase_till(2)
        self.assertEqual(2, self.bar.till)

    def test_add_drink(self):
        drink = Drink("Cola", 3)
        self.bar.add_drink(drink)
        self.assertEqual("Cola", self.bar.drinks[0].name)

    def test_get_drink_price(self):
        drink = Drink("Cola", 3)
        self.bar.add_drink(drink)
        self.assertEqual(3, self.bar.drinks[0].price)

    def test_has_drink_pass(self):
        drink = Drink("Cola", 3)
        self.bar.add_drink(drink)
        self.assertEqual(True, self.bar.has_drink("Cola"))

    def test_has_drink_fail(self):
        drink = Drink("Cola", 3)
        self.bar.add_drink(drink)
        self.assertEqual(False, self.bar.has_drink("Lemonade"))

    def test_remove_drink(self):
        drink = Drink("Cola", 3)
        self.bar.add_drink(drink)
        self.bar.remove_drink("Cola")
        self.assertEqual(0, len(self.bar.drinks))