import pytest
from src.item import Item
from src.phone import Phone

def test_item_name_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.name == 'Смартфон'
    assert item.name != 'смартфон'


def test_item_price_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.price == 10.0
    assert item.price != "10.0"

def test_item_quantity_getter():
    item = Item('Смартфон', 10.0, 5)
    assert item.quantity == 5
    assert item.quantity != "5"

def test_item_name_setter():
    item = Item('name', 10.0, 5)
    item1 = Item('name', 10.0, 5)
    item2 = Item('name', 10.0, 5)
    item.name = 'СуперСмартфон'
    item1.name = 'Смартфон'
    item2.name = 'Смарт'
    assert item.name == 'СуперСмарт'
    assert item.name != 'суперсмарт'
    assert item1.name == 'Смартфон'
    assert item1.name != 'смартфон'
    assert item2.name == 'Смарт'
    assert item2.name != 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number("10.0") == 10.0
    assert Item.string_to_number("10.0") != "10.0"
    assert Item.string_to_number("10.0") == 10

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv('items.csv')
    assert len(items) == 5
    assert items[0].name == "Смартфон"
    assert items[0].price == 100.0
    assert items[0].quantity == 1
    assert items[1].name == "Ноутбук"
    assert items[1].price == 1000.0
    assert items[1].quantity == 3

def test_repr_method():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Смартфон", 10, 0)
    item3 = Item("Смартфон", -10000, -20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item1) != "Item 'Смартфон', 10000, 20"
    assert repr(item1) != "Item ('cмартфон', 10000, 20)"
    assert repr(item2) == "Item('Смартфон', 10, 0)"
    assert repr(item3) == "Item('Смартфон', -10000, -20)"
def test_str_method():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
    assert str(item1) != 'cмартфон'

def test_add_with_item():
    phone1 = Phone("iPhone", 999, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    total_quantity = item1 + phone1
    assert total_quantity == 30

def test_add_with_item():
    phone1 = Phone("iPhone", 999, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    total_quantity = item1 + phone1
    assert total_quantity != 10

def test_add_with_different_class():
    phone = Phone("Nokia", 299, 2, 1)
    with pytest.raises(TypeError):
        total_quantity = phone + 5

