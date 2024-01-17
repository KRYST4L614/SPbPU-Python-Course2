class Car:
    def __init__(self, model: str, hp: int, weight: int):
        """
        Создание и подготовка к работе объекта "Машина"
        :param model: Модель
        :param hp: Лошадинные силы
        :param weight: Вес
        Примеры:
        >>> car = Car("Volvo XC 90", 250, 2000)  # инициализация экземпляра класса
        """
        if not isinstance(hp, int):
            raise TypeError("Hp must be int. Received: {0}".format(type(hp)))
        if not isinstance(weight, int):
            raise TypeError("Weight must be int. Received: {0}".format(type(weight)))
        if not isinstance(model, str):
            raise TypeError("Model must be string. Received: {0}".format(type(model)))
        if hp < 0:
            raise ValueError("Hp must be greater than zero")
        if weight < 0:
            raise ValueError("Weight must be greater than zero")
        self.hp = hp
        self.weight = weight
        self.model = model

    def check_weight(self, max_weight) -> bool:
        """
        Функция которая проверяет допустимый вес машины (например, для проверки того, какой эвакуатор ей нужен)
        :return: Подходит ли машина по весу
        Примеры:
        >>> car = Car("Volvo XC 90", 250, 2000)  # инициализация экземпляра класса
        >>> car.check_weight(2300)  # вызов метода
        True
        """
        return self.weight < max_weight

    def check_hp(self, max_hp) -> bool:
        """
        Функция которая проверяет подходит ли машина под ограничения по л/с (например, для расчёта налога)
        :return: Подходит ли машина по л/с
        Примеры:
        >>> car = Car("Volvo XC 90", 250, 2000)  # инициализация экземпляра класса
        >>> car.check_hp(300)  # вызов метода
        True
        """
        return self.hp < max_hp

    def __str__(self):
        return f"Модель машины {self.model}. Л/с: {self.hp}. Вес: {self.weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, hp={self.hp!r}, weight={self.weight!r})"

class PassengerCar(Car):
    def __init__(self, model: str, hp: int, weight: int):
        """
        Создание и подготовка к работе объекта "Легковая машина"
        :param model: Модель
        :param hp: Лошадинные силы
        :param weight: Вес
        Примеры:
        >>> p_car = PassengerCar("Volvo S 90", 250, 1600)  # инициализация экземпляра класса
        """
        super().__init__(model, hp, weight)

class Truck(Car):
    def __init__(self, model: str, hp: int, weight: int, payload: int):
        """
        Создание и подготовка к работе объекта "Грузовик"
        :param model: Модель
        :param hp: Лошадинные силы
        :param weight: Вес
        :param payload: Максимальная грузоподъёмность
        Примеры:
        >>> truck = Truck("Volvo FH", 460, 7000, 12000)  # инициализация экземпляра класса
        """
        if not isinstance(payload, int):
            raise TypeError("Payload must be int. Received: {0}".format(type(payload)))
        if payload < 0:
            raise ValueError("Payload must be greater than zero")
        super().__init__(model, hp, weight)
        self.payload = payload
        self._current_payload = 0

    @property
    def current_payload(self):
        return self._current_payload

    def add_cargo(self, cargo) -> None:
        """
        Функция которая добавляет груз, если груз не превышает максимального
        :return: Подходит ли машина по л/с
        Примеры:
        >>> truck = Truck("Volvo FH", 460, 7000, 12000)  # инициализация экземпляра класса
        >>> truck.add_cargo(4000)  # вызов метода
        """
        if (self.payload - self.current_payload < cargo):
            raise ValueError
        self._current_payload += cargo

    def check_weight(self, max_weight) -> bool: #Перегрузка нужна так как необходимо учитывать вес самой машины + вес груза
        """
        Функция которая проверяет допустимый вес машины (например, для проверки того, какой эвакуатор ей нужен)
        :return: Подходит ли машина по весу
        Примеры:
        >>> truck = Truck("Volvo FH", 460, 7000, 12000)  # инициализация экземпляра класса
        >>> truck.check_weight(4000)  # вызов метода
        False
        """
        return max_weight >= (self.weight + self.current_payload)

    def __str__(self):
        return f"Модель машины {self.model}. Л/с: {self.hp}. Вес: {self.weight}. Грузоподъемность: {self.payload}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, hp={self.hp!r}, weight={self.weight!r}, payload={self.payload!r})"

if __name__ == "__main__":
    pass
