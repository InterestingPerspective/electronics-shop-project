import os
import pytest
import csv
from src.item import Item, InstantiateCSVError


@pytest.fixture
def coll():
    return Item("Смартфон", 10000, 20)


def instantiate_from_csv_test_1():
    with open("tests/test_1.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if len(row) != 3 or None in row.keys() or None in row.values():
                raise InstantiateCSVError("Файл item.csv поврежден")


def instantiate_from_csv_test_2():
    with open("tests/test_2.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if len(row) != 3 or None in row.keys() or None in row.values():
                raise InstantiateCSVError("Файл item.csv поврежден")


def test_calculate_total_price(coll):
    assert coll.calculate_total_price() == 200000


def test_apply_discount(coll):
    Item.pay_rate = 0.8
    coll.apply_discount()
    assert coll.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    item5 = Item.all[4]

    assert item1.name == "Смартфон"
    assert item5.name == "Клавиатура"

    assert len(Item.all) == 5

    item1.name = "СуперСмартфон"
    assert item1.name == "СуперСмарт"

    with pytest.raises(FileNotFoundError):
        path = os.path.dirname(__file__)
        file = os.path.join(path, "nonexistent.csv")
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)

    with pytest.raises(InstantiateCSVError):
        instantiate_from_csv_test_1()

    with pytest.raises(InstantiateCSVError):
        instantiate_from_csv_test_2()


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("4.7") == 4
    assert Item.string_to_number("4.0") == 4

    item1 = Item.all[0]
    assert item1.quantity == 1
    item5 = Item.all[4]
    assert item5.quantity == 5


def test_repr(coll):
    assert repr(coll) == "Item('Смартфон', 10000, 20)"
    assert repr(Item.all[4]) == "Item('Клавиатура', 75.0, 5)"


def test_str(coll):
    assert str(coll) == "Смартфон"
    assert str(Item.all[4]) == "Клавиатура"


class Auto:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item5 = Item("Клавиатура", 75, 5)
    auto1 = Auto("Машина", 200000, 3)

    assert item1 + item5 == 25
    with pytest.raises(ValueError):
        item1 + auto1
