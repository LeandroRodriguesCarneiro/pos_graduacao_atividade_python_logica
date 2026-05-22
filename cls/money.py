class Money:
    def __init__(self, value, quantity) -> None:
        self.__value = value
        self.__quantity = quantity

    def __str__(self) -> str:
        return (
            f'Nota/Moeda: R$ {self.__value/100:<6.2f} | '
            f'Quantidade: {self.__quantity:<3}'
        )

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity