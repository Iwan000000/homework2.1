from src.item import Item
class MixinLang:
    """
    Класс для изменения языка
    """
    def __init__(self):
        """
        Инициализация класса MixinLang
        """
        self.lang_list = ['EN', 'RU']
        self.language = 'EN'

    def change_lang(self):
        """
        Метод для изменения языка
        :return:Метод проверяет текущий язык и переключает его
        на следующий язык из списка lang_list
        """
        if self.language == self.lang_list[0]:
            self.language = self.lang_list[1]
        else:
            self.language = self.lang_list[0]


class MixinLang(Item, MixinLang):
    """
    Класс Keyboard.
    Класс представляет объект клавиатуры и наследует
    функциональность класса Item и класса MixinLang
    """
    def __init__(self, name, price, discount=0, language="EN"):
        """
        Инициализация класса Keyboard
        :param name: Название клавиатуры
        :param price: Цена клавиатуры
        :param discount: Скидка на клавиатуру
        :param language: Язык клавиатуры
        """
        super().__init__(name, price, discount)
        self._language = language

    @property
    def language(self):
        """
        Получение текущего языка клавиатуры
        :return: Текущий язык клавиатуры
        """
        return self._language

    @language.setter
    def language(self, new_lang):
        """
        Установка нового языка клавиатуры
        :param new_lang:Новый язык клавиатуры
        :return:Выполняет операцию присваивания нового значения языку клавиатуры
        """
        if new_lang in ["EN", "RU"]:
            self._language = new_lang

    def __str__(self):
        """
        Возвращает строковое представление объекта Keyboard
        :return: Строковое представление объекта Keyboard
        """
        return super().__str__()
