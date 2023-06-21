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
