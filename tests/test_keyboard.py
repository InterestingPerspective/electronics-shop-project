import pytest
from src.keyboard import Keyboard


@pytest.fixture
def coll():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(coll):
    assert coll.name == "Dark Project KD87A"
    assert coll.price == 9600
    assert coll.quantity == 5


def test_repr(coll):
    assert repr(coll) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_str(coll):
    assert str(coll) == "Dark Project KD87A"


def test_language(coll):
    assert str(coll.language) == "EN"


def test_change_lang(coll):
    coll.change_lang()
    assert coll.language == "RU"

    coll.change_lang()
    assert coll.language == "EN"

    coll.change_lang().change_lang()
    assert coll.language == "EN"
