from item import Item


if __name__ == '__main__':
    items = Item.instantiate_from_csv('items.csv')

    for item in items:
        print(f"Наименование: {item.name}, Стоимость: {item.price}, Колличество: {item.quantity}")

