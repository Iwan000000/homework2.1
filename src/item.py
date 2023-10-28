import csv


class Item:
    """
     Класс для представления товара в магазине.
    """

    all = []

    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.__price = price
        self.__quantity = quantity


    @property
    def name(self):
        """
        Наименование товара
        """
        return self.__name

    @property
    def price(self):
        """
        Стоимость товара
        """
        return self.__price

    @property
    def quantity(self):
        """
        Колличество товара
        """
        return self.__quantity

    @name.setter
    def name(self, value):
        """
        Название товара с ограничением в 10 символов
        :param value: Название товара
        :return: Урезанное название до 10 символов
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value


    @staticmethod
    def string_to_number(string):
        """
        возвращающий число из числа-строки
        :param string: Число строки
        :return: Число с плавающей точкой
        """
        return float(string)

    @classmethod
    def instantiate_from_csv(cls, file_path):
        """
        Создает объекты item из CSV-файла.
        :param file_path: Имя файла
        :return:  Список товара
        """

        items = []
        with open(file_path, 'r', encoding="cp1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                items.append(item)
        cls.all = items
        return items


    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки
        :return: Выводит строку с названием товара, ценой и колличеством
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Выводит название товара
        """
        return f"{self.name}"

    def __add__(self, other):
        """
        Магический метод, который позволяет прибавлять к экземпляру класса объект произвольного типа данных
        :param other: Принимает остаток товара в магазине и складывает с определённым товаром
        :return: Выводит общие колличество
        """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Item' и чем-то другим.")
