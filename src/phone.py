from src.item import Item

class Phone(Item):
    """
    Класс, представляющий телефон.
    Наследуется от класса Item.
    """
    def __init__(self, name, price, quantity, sim_count):
        """
        Создает новый экземпляр класса Phone.
        :param name: название телефона
        :param price: цена телефона
        :param quantity: количество телефонов
        :param sim_count: количество SIM-карт
        """
        super().__init__(name, price, quantity)
        self.__sim_count = sim_count

    @property
    def number_of_sim(self):
        """
        Возвращает количество SIM-карт.
        :return: количество SIM-карт
        """
        return self.__sim_count

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Устанавливает количество SIM-карт.
        :param value: количество SIM-карт
        :return:
        """
        if isinstance(value, int) and value >= 0:
            self.__sim_count = value
        else:
            raise ValueError("Количество SIM-карт должно быть больше нуля.")

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки
        :return: Выводит строку с названием товара, ценой, колличеством и колличеством сим карт
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__sim_count})"

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Выводит название товара
        """
        return f"{self.name}"


    def __add__(self, other):
        """
        Магический метод, который позволяет прибавлять к экземпляру класса объект произвольного типа данных
        :param other: Принимает остаток товара Phone и складывает с общим остатком товара в магазине
        :return: Выводит общие колличество
        """
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Phone' и чем-то другим.")
