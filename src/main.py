from src.item import Item
from src.phone import Phone


# if __name__ == '__main__':
#      item1 = Item("Смартфон", 10000, 20)
#      print(item1.__str__())
#      print(item1.__repr__())
#      assert repr(item1) == "Item('Смартфон', 10000, 20)"
#      assert str(item1) == 'Смартфон'

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    print(phone1.__repr__())
    print(item1.__repr__())
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    phone1.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
