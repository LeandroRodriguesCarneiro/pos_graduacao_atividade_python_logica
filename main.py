from random import randint

from cls import Drink, VendingMachine, Money
from utils import start

coca_cola = Drink(1, 'Coca-cola', 375, 2)
pepsi = Drink(2, 'Pepsi', 367, 5)
monster = Drink(3, 'Monster', 996, 1)
cafe = Drink(4, 'cafe', 125, 100)
red_bull = Drink(5, 'Red Bull', 1399, 2)

vending_machine = VendingMachine()
vending_machine.add_drink(coca_cola)
vending_machine.add_drink(pepsi)
vending_machine.add_drink(monster)
vending_machine.add_drink(cafe)
vending_machine.add_drink(red_bull)

wallet = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

for money in wallet:
    vending_machine.add_money(
        Money(money, randint(1, 10))
    )

start(vending_machine)