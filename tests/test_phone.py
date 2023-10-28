import pytest
from src.phone import Phone

def test_number_of_sim():
    phone = Phone("iPhone", 999, 10, 2)
    assert phone.number_of_sim == 2

def test_set_number_of_sim():
    phone = Phone("Samsung", 799, 5, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_set_invalid_number_of_sim():
    phone = Phone("Sony", 599, 3, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = -1

def test_repr():
    phone = Phone("Nokia", 299, 2, 1)
    assert repr(phone) == "Phone('Nokia', 299, 2, 1)"

def test_str():
    phone = Phone("Motorola", 199, 1, 1)
    assert str(phone) == "Motorola"

def test_add_phones():
    phone1 = Phone("iPhone", 999, 10, 1)
    phone2 = Phone("Samsung", 799, 5, 1)
    total_quantity = phone1 + phone2
    assert total_quantity == 15

def test_add_phone_with_different_class():
    phone = Phone("Nokia", 299, 2, 1)
    with pytest.raises(TypeError):
        total_quantity = phone + 5
