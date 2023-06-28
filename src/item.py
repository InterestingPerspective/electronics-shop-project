import csv
import math
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        path = os.path.dirname(__file__)
        with open(os.path.join(path, "items.csv")) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                __name, price, quantity = row["name"], float(row["price"]), cls.string_to_number(row["quantity"])
                item = cls(__name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(string_number):
        """Переводит строку в число с плавающей точкой, а затем округляет в меньшую сторону"""
        return math.floor(float(string_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
