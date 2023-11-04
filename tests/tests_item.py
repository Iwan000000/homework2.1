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
    item3 = Item('name', 10.0, 5)
    item4 = Item('name', 10.0, 5)
    item.name = 'СуперСмартфон'
    item1.name = 'Смартфон'
    item2.name = 'Смарт'
    item3.name = 'суперсмарт'
    item4.name = 'супер смарт'
    assert item.name == 'СуперСмарт'
    assert item.name != 'суперсмарт'
    assert item1.name == 'Смартфон'
    assert item1.name != 'смартфон'
    assert item2.name == 'Смарт'
    assert item2.name != 'Смартфон'
    assert item3.name == 'суперсмарт'
    assert item4.name == 'супер смар'

def test_string_to_number():
    assert Item.string_to_number("10.2") == 10.2
    assert Item.string_to_number("10.0") != "10.0"
    assert Item.string_to_number("10") == 10.0
    assert Item.string_to_number("-5.5") == -5.5
    assert Item.string_to_number("0") == 0.0

def test_string_to_number_with_invalid_string():
    try:
        Item.string_to_number("abc")
        assert False
    except ValueError:
        assert True

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
    item1 = Item("Смартфон", 10000, 20)
    with pytest.raises(TypeError):
        remaining_quantity = item1 - 5

def test_instantiate_csv_error_with_exclamation_mark():
    with pytest.raises(InstantiateCSVError) as excinfo:
        raise InstantiateCSVError('file!.csv')
    assert str(excinfo.value) == 'file!.csv повреждён'


def test_instantiate_csv_error_with_normal_filename():
    with pytest.raises(InstantiateCSVError) as excinfo:
        raise InstantiateCSVError('file.csv')
    assert str(excinfo.value) == 'file.csv повреждён'


def test_instantiate_csv_error_with_empty_filename():
    with pytest.raises(InstantiateCSVError) as excinfo:
        raise InstantiateCSVError('')
    assert str(excinfo.value) == ' повреждён'


def test_instantiate_from_csv_success():
    filename = 'valid_file.csv'
    # Заглушка для чтения из файла
    rows = [
        {'name': 'item1', 'price': '10.5', 'quantity': '20'},
        {'name': 'item2', 'price': '15.0', 'quantity': '10'},
    ]
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        # Заменяем rows на заглушку для проверки функциональности чтения csv
        mock_csv.DictReader.return_value = rows
        items = InstantiateCSVError.instantiate_from_csv(filename)
    assert items == ['item1', 'item2']


def test_instantiate_from_csv_file_not_found():
    filename = 'missing_file.csv'
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = InstantiateCSVError.instantiate_from_csv(filename)
    assert result == f'Отсутствует файл {filename}'


def test_instantiate_from_csv_corrupted_file():
    filename = 'corrupted_file.csv'
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        # Заглушка для чтения из файла
        rows = [
            {'name': 'item1', 'price': '10.5', 'quantity': '20'},
            {'name': 'item2', 'price': '15.0', 'quantity': '10'},
        ]
        # Добавляем строку с "повреждённым" именем
        corrupted_row = {'name': 'item!', 'price': '5.0', 'quantity': '5'}
        rows.append(corrupted_row)
        mock_csv.DictReader.return_value = rows
        result = InstantiateCSVError.instantiate_from_csv(filename)
    assert str(result) == 'item! повреждён'
