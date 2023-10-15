import pytest
from src.item import Item


def test_item_name_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.name == 'Смартфон'


def test_item_price_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.price == 10.0

def test_item_quantity_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.quantity == 5


def test_item_name_setter():
    item = Item('name', 10.0, 5)
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'

def test_string_to_number():
    assert Item.string_to_number("10.0") == 10.0

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv('items.csv')
    assert len(items) == 5
    assert items[0].name == "Смартфон"
    assert items[0].price == 100.0
    assert items[0].quantity == 1
    assert items[1].name == "Ноутбук"
    assert items[1].price == 1000.0
    assert items[1].quantity == 3