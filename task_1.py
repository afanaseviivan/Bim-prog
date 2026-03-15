if __name__ == "__main__":
    class Car:
        def __init__(self, name: str, mass: int, power: int) -> None:
            """
            Создание и подготовка к работе объекта "Автомобиль"

            :param name: Название автомобиля
            :param mass: Масса автомобиля
            :param power: Мощность двигателя автомобиля

            Атрибуты name, mass, power непубличны, так как их изменение пользователем не подразумевается
            Примеры:
            >>> car_1 = Car("Lada Granta", 1560, 90)  # инициализация экземпляра класса
            """
            self._name = name
            self._mass = mass
            self._power = power

        @property
        def name(self) -> str:
            return self._name

        @property
        def mass(self) -> int:
            return self._mass

        @property
        def power(self) -> int:
            return self._power

        def registration(self, number: int) -> None:
            """
            Функция, которая регистрирует номер автомобиля

            :param number: Регистрируемый номер
            :raise ValueError: Если номер не уникальный, то вызываем ошибку
            :raise TypeError: Если тип номера не int, то вызываем ошибку

            Примеры:
            >>> car_1 = Car("Lada Granta", 1560, 90)
            >>> car_1.registration(21045)
            """
            ...

        def __str__(self) -> str:
            return f"Автомобиль {self.name} массой {self.mass} кг., мощностью {self.power} л.с."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, mass={self.mass!r}, power={self.power!r})"


    class PassengerCar(Car):
        """
        Создание и подготовка к работе объекта "Легковой автомобиль"

        :param name: Название автомобиля
        :param mass: Масса автомобиля
        :param power: Мощность двигателя автомобиля
        :param capacity_people: Вместимость человек в автомобиле
        :param color: Цвет автомобиля

        Атрибут capacity_people непубличен, так как его изменение пользователем не подразумевается
        Примеры:
        >>> car_1 = PassengerCar("Exeed RX", 2237, 267, 7, "red")  # инициализация экземпляра класса
        """
        def __init__(self, name: str, mass: int, power: int, capacity_people: int, color: str) -> None:
            super().__init__(name, mass, power)
            self._capacity_people = capacity_people
            self.color = None
            self.init_color(color)

        def init_color(self, color: str) -> None:
            if not isinstance(color, str):
                raise TypeError("Цвет должно быть типа str")
            self.color = color

        @property
        def capacity_people(self) -> int:
            return self._capacity_people

        def __str__(self) -> str:
            return f"Легковой автомобиль {self.name} массой {self.mass} кг., мощностью {self.power} л.с., вместимостью {self.capacity_people} чел. цвета {self.color}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, mass={self.mass!r}, power={self.power!r}, capacity_people={self.capacity_people}, color={self.color})"


    class CargoCar(Car):
        """
        Создание и подготовка к работе объекта "Грузовой автомобиль"

        :param name: Название автомобиля
        :param mass: Масса автомобиля
        :param power: Мощность двигателя автомобиля
        :param volume: Рабочий объем автомобиля
        :param light_board: Световая вывеска на лобовом стекле

        Атрибут volume непубличен, так как его изменение пользователем не подразумевается
        Примеры:
        >>> car_1 = CargoCar("Hyundai HD78", 2540, 150, 3907, "я король дороги")  # инициализация экземпляра класса
        """
        def __init__(self, name: str, mass: int, power: int, volume: int, light_board: str) -> None:
            super().__init__(name, mass, power)
            self._volume = volume
            self.light_board = None
            self.init_light_board(light_board)

        def init_light_board(self, light_board: str) -> None:
            if not isinstance(light_board, str):
                raise TypeError("Текст на вывеске должен быть типа str")
            self.light_board = light_board

        @property
        def volume(self) -> int:
            return self._volume

        def registration(self, number: str) -> None:
            """
            Функция, которая регистрирует номер автомобиля

            :param number: Регистрируемый номер
            :raise ValueError: Если номер не уникальный, то вызываем ошибку
            :raise TypeError: Если тип номера не str, то вызываем ошибку

            Метод перегружается, так как номер для легкового автомобиля состоит из цифр, а грузового из букв
            Примеры:
            >>> car_1 = CargoCar("Hyundai HD78", 2540, 150, 3907, "я король дороги")
            >>> car_1.registration("GRUZK")
            """
            ...

        def __str__(self) -> str:
            return f"Грузовой автомобиль {self.name} массой {self.mass} кг., мощностью {self.power} л.с., рабочим объемом {self.volume} л. и вывеской на лобовом стекле с текстом {self.light_board}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, mass={self.mass!r}, power={self.power!r},volume={self.volume}, light_board={self.light_board})"
    pass