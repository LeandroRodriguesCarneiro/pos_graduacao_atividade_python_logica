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
        
        return None

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

    def __calc_change(self, value: int, price: int):
        change = value - price

        if change < 0:
            print('Não é possível comprar')
            return False
        
        if change == 0:
            print('\nCompra realizada sem troco.')
            return True

        response = (
            f'\nTroco: R$ {change/100:.2f}\n'
        )

        temp_change = change
        temp_result = []

        for money in self.__money_bank:
            if temp_change >= money.value:
                qtd_necessaria = temp_change // money.value

                qtd_used = min(
                    qtd_necessaria,
                    money.quantity
                )

                if qtd_used > 0:
                    temp_result.append((money, qtd_used))
                    temp_change -= qtd_used * money.value

                    response += (
                        f'- R$ {money.value/100:>6.2f} '
                        f'x {qtd_used:<3} '
                        f'= R$ {(qtd_used * money.value)/100:.2f}\n'
                    )

        if temp_change > 0:
            print('\nNão foi possível fornecer o troco completo.')
            print(f'Faltam R$ {temp_change/100:.2f}')
           
            return False

        for money, qtd_used in temp_result:
            money.quantity -= qtd_used

        print(response)

        return True

    def buy_drink(self, drink):
        try:
            print(drink)
            if drink.stock <= 0:
                print('\nProduto sem estoque!')
                return

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

            result = self.__calc_change(payment, drink.price)

            if result:
                drink.stock -= 1

                print('\nCompra realizada com sucesso!')
        except Exception as e:
            print(e)