import pytest
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard("Keyboard", 50, language="EN")


def test_keyboard_initial_values(keyboard):
    assert keyboard.name == "Keyboard"
    assert keyboard.price == 50
    assert keyboard.language == "EN"


def test_keyboard_change_language(keyboard):
    assert keyboard.language == "EN"

    keyboard.change_lang()
    assert keyboard.language == "RU"

    keyboard.change_lang()
    assert keyboard.language == "EN"


def test_keyboard_set_language(keyboard):
    assert keyboard.language == "EN"

    keyboard.language = "RU"
    assert keyboard.language == "RU"

    keyboard.language = "FR"
    assert keyboard.language == "RU"
