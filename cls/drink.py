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

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):

        if value < 0:
            raise ValueError('O preço não pode ser negativo')

        self.__price = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):

        if value < 0:
            raise ValueError('O estoque não pode ser negativo')

        self.__stock = value