import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.food = Drink("Cola", 3)
    
    def test_food_has_name(self):
        self.assertEqual("Cola", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(3, self.food.price)