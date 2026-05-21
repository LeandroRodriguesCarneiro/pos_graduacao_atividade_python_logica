from .drink import Drink

class VendingMachine:
    def __init__(self):
        self.__drinks = []

    def add_drink(self, drink: Drink):
        self.__drinks.append(drink)

    def get_drink(self, drink_id):
        for drink in self.__drinks:
            if drink.id == drink_id:
                return drink
        else:
            print(f"Drink with id {drink_id} not found")

    def remove_drink(self, drink_id):
        drink = self.get_drink(drink_id)
        if not drink is None:
            self.__drinks.remove(drink)

    def show_drinks(self):
        for drink in self.__drinks:
            print(drink)
