from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, sim_count):
        super().__init__(name, price, quantity)
        self.__sim_count = sim_count

    @property
    def number_of_sim(self):
        return self.__sim_count

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value >= 0:
            self.__sim_count = value
        else:
            raise ValueError("Количество SIM-карт должно быть больше нуля.")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__sim_count})"

    def __str__(self):
        return f"{self.name}"


    def __add__(self, other):
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Phone' и чем-то другим.")
