class Bar:

    def __init__(self, till = 0):
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def has_drink(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return True
        return False

    def add_drink(self, drink):
        self.drinks.append(drink)

    def get_drink_price(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink.price

    def remove_drink(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                self.drinks.remove(drink)
