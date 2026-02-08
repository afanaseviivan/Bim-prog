class Smartphone:
    def __init__(self, name: str, batary_charge: int) -> None:
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param name: Название телефона
        :param batary_chargee: Заряд батареи телефона

        Примеры:
        >>> smartphone = Smartphone("Iphone 16 Pro", 52)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(batary_charge, int):
            raise TypeError("Значение должно быть типа int")
        if batary_charge < 0:
            raise ValueError("Значение должно быть неотрицательным")
        self.batary_charge = batary_charge

    def add_charge(self, charge: int) -> int:
        """
        Функция, которая добавляет заряд батареи

        :param charge: Заряд, добавляемый к батареи
        :raise ValueError: Если после добавления заряда значение батареи превышает максимальное значение, то вызываем ошибку
        :return: Актуальный заряд батареи, после добавления заряда

        Примеры:
        >>> smartphone = Smartphone("Iphone 16 Pro", 52)
        >>> smartphone.add_charge(20)
        """
        if not isinstance(charge, int):
            raise TypeError("Значение должно быть типа int")
        if charge < 0:
            raise ValueError("Значение должно быть неотрицательным")
        ...

    def rest_batary(self) -> int:
        """
        Функция, которая показывает остаток заряда батареи

        :return: Актуальный заряд батареи

        Примеры:
        >>> smartphone = Smartphone("Iphone 16 Pro", 52)
        >>> smartphone.rest_batary()
        """
        ...

    def use_batary(self, charge: int) -> int:
        """
        Функция, которая добавляет заряд батареи

        :param charge: Заряд, который будет затрачен
        :raise ValueError: Если количество траты заряда превышают актуальное значение батареи, то вызываем ошибку
        :return: Актуальный заряд батареи, после добавления заряда

        Примеры:
        >>> smartphone = Smartphone("Iphone 16 Pro", 52)
        >>> smartphone.use_batary(32)
        """
        if not isinstance(charge, int):
            raise TypeError("Значение должно быть типа int")
        if charge < 0:
            raise ValueError("Значение должно быть неотрицательным")
        ...


class BoxForCubes:
    def __init__(self, name: str, max_obj: int, actual_obj: int) -> None:
        """
        Создание и подготовка к работе объекта "Коробка для кубиков"

        :param name: Название коробки
        :param max_obj: Максимальное количество кубиков в коробке
        :param actual_obj: Сколько сейчас лежит в коробке

        Примеры:
        >>> box_1 = BoxForCubes("Желтые кубы", 10, 0)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(max_obj, int):
            raise TypeError("Значение должно быть типа int")
        if max_obj < 0:
            raise ValueError("Значение должно быть неотрицательным")
        self.max_obj = max_obj

        if not isinstance(actual_obj, int):
            raise TypeError("Значение должно быть типа int")
        if actual_obj < 0:
            raise ValueError("Значение должно быть неотрицательным")
        self.actual_obj = actual_obj

    def add_cubes(self, cubes: int) -> int:
        """
        Функция, которая добавляет кубики в коробку

        :param cubes: Количество кубиков
        :raise ValueError: Если после добавления кубика их количество в коробке превышает максимальное значение, то вызываем ошибку
        :return: Количество кубиков после добавления

        Примеры:
        >>> box_1 = BoxForCubes("Желтые кубы", 10, 0)
        >>> box_1.add_cubes(2)
        """
        if not isinstance(cubes, int):
            raise TypeError("Значение должно быть типа int")
        if cubes < 0:
            raise ValueError("Значение должно быть неотрицательным")
        ...

    def delete_cubes(self, cubes: int) -> int:
        """
        Функция, которая убирает кубик из коробки

        :param cubes: Количество кубиков
        :raise ValueError: Если после удаления кубки из коробки появляется отрицательное значениеБ вызывается ошибка
        :return: Количество кубиков после удаления

        Примеры:
        >>> box_1 = BoxForCubes("Желтые кубы", 10, 9)
        >>> box_1.delete_cubes(7)
        """
        if not isinstance(cubes, int):
            raise TypeError("Значение должно быть типа int")
        if cubes < 0:
            raise ValueError("Значение должно быть неотрицательным")
        ...

    def empty(self) -> bool:
        """
        Функция, которая проверяет является ли коробка пустой

        :return: Является ли коробка пустой

        Примеры:
        >>> box_1 = BoxForCubes("Желтые кубы", 10, 0)
        >>> box_1.empty()
        """
        ...


class Stone:
    def __init__(self, name: str, volume: (int, float), mass: (int, float)) -> None:
        """
        Создание и подготовка к работе объекта "Камень"

        :param name: Название камня
        :param volume: Объем камня
        :param mass: Масса камня

        Примеры:
        >>> stone_1 = Stone("Гранит", 0.25, 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(volume, (int, float)):
            raise TypeError("Значение должно быть типа int или float")
        if volume <= 0:
            raise ValueError("Значение должно быть натуральным")
        self.volume = volume

        if not isinstance(mass, (int, float)):
            raise TypeError("Значение должно быть типа int или float")
        if mass <= 0:
            raise ValueError("Значение должно быть натуральным")
        self.mass = mass

    def middle_density(self) -> int:
        """
        Функция, которая считает среднюю плотность камня

        :return: Средняя плотность камня

        Примеры:
        >>> stone_1 = Stone("Гранит", 0.25, 3)
        >>> stone_1.middle_density()
        """
        ...

    def true_density(self) -> int:
        """
        Функция, которая считает истинную плотность камня

        :return: Истинная плотность камня

        Примеры:
        >>> stone_1 = Stone("Гранит", 0.25, 3)
        >>> stone_1.true_density()
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod() # тестирование примеров, которые находятся в документации
    pass