class Drink:
    def __init__(self, id: int, name: str, price: float, stock: int) -> None:
          self.__id = id
          self.__name = name
          self.__price = price
          self.__stock = stock

    def __str__(self) -> str:
          return (
              f'Código: {self.__id:<3} | '
              f'Produto: {self.__name:<15} | '
              f'Preço: R$ {self.__price/100:>6.2f} | '
              f'Estoque: {self.__stock:>3}'
          )

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock