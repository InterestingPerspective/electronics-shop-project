import pytest
from src.phone import Phone


@pytest.fixture
def coll():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(coll):
    assert coll.name == "iPhone 14"
    assert coll.price == 120000
    assert coll.quantity == 5
    assert coll.sim == 2


def test_repr(coll):
    assert repr(coll) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(coll):
    with pytest.raises(ValueError):
        coll.number_of_sim = 0

    coll.number_of_sim = 2
    assert coll.sim == 2
