import pytest
from src.item import Item


@pytest.fixture
def coll():
    return Item("Смартфон", 10000, 20)


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


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("4.7") == 4
    assert Item.string_to_number("4.0") == 4

    item1 = Item.all[0]
    assert item1.quantity == 1
    item5 = Item.all[4]
    assert item5.quantity == 5
