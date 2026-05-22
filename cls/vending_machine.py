from .drink import Drink
from .money import Money

class VendingMachine:
    def __init__(self):
        self.__drinks = []
        self.__money_bank = []

    def add_drink(self, drink: Drink):
        self.__drinks.append(drink)

    def get_drink(self, drink_id: int):
        for drink in self.__drinks:
            if drink.id == drink_id:
                return drink
        else:
            Exception(f"Drink with id {drink_id} not found")

    def remove_drink(self, drink_id):
        drink = self.get_drink(drink_id)
        if not drink is None:
            self.__drinks.remove(drink)

    def show_drinks(self):
        for drink in self.__drinks:
            print(drink)

    def add_money(self, money: Money):
        self.__money_bank.append(money)

    def get_money(self, money_value):
        for money in self.__money_bank:
            if money.value == money_value:
                return money
        else:
            Exception(f"Money with value {money_value} not found")
    
    def remove_money(self, money_value):
        money = self.get_money(money_value)
        if not money is None:
            self.__money_bank.remove(money)

    def show_money(self):
        for money in self.__money_bank:
            print(money)

    def __calc_change(self, value: float, price: float):
        change = value - price

        if change < 0:
            print('Não é possivel comprar')
        
        for money in self.__money_bank:
            if change >= money.value:
                qtd_necessaria = change // money.value
                qtd_usada = min(qtd_necessaria, money.quantity)
                valor_total = qtd_usada * money.value
                print(
                    f'R$ {money.value/100:.2f} '
                    f'- {qtd_usada}'
                    f'= R$ {valor_total/100:.2f}'
                )
                change -= valor_total

        if change > 0:
            print(f"\nNão foi possível fornecer o troco completo.")
            print(f"Faltam R$ {change/100:.2f}")

    def buy_drink(self, drink_id):
        try:
            drink = self.get_drink(drink_id)

            if drink.stock <= 0:
                print('\nProduto sem estoque!')

            print(
                f'\nProduto selecionado: {drink.name}'
                f'\nValor: R$ {drink.price/100:.2f}'
            )

            payment = int(
                float(
                    input(
                        '\nDigite o valor pago: R$ '
                        ).replace(',', '.')
                    ) * 100
            )

            if payment < drink.price:
                print('\nValor insuficiente! Compra cancelada')
                return

            result = self.__calc_change(drink.price, payment)

            if not result:
                print('\nNão foi possível fornecer o troco.')
                print('Compra cancelada!')

            print('\nTroco entregue:')

            for money, qtd in result:
                print(
                    f'R$ {money.value/100:.2f} '
                    f'x {qtd}'
                )

            drink.stock -= 1

            print('\nCompra realizada com sucesso!')
        except Exception as e:
            print(e)