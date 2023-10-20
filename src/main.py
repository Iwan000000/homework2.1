from item import Item


if __name__ == '__main__':
     item1 = Item("Смартфон", 10000, 20)
     print(item1.__str__())
     print(item1.__repr__())
     assert repr(item1) == "Item('Смартфон', 10000, 20)"
     assert str(item1) == 'Смартфон'
