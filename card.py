class Card:
    def __init__(self, color, value):
        self.__color = color
        self.__value = value

    def __str__(self):
        return f"{self.__value} de {self.__color}"

    def get_color(self):
        return self.__color

    def get_value(self):
        return self.__value

    def get_card(self):
        return f"{self.__value} de {self.__color}"

