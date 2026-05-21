class Money:
    def __init__(self, value, quantity) -> None:
        self.__value = value
        self.__quantity = quantity

    def __str__(self) -> str:
        return f"{self.__value/100:.2f} {self.__quantity}"

    @property
    def value(self):
        return self.__value

    @property
    def quantity(self):
        return self.__quantity
