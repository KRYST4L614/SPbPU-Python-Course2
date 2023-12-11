import doctest
from typing import Union


class Person:
    def __init__(self, first_name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param first_name: Имя
        :param age: Возраст

        Примеры:
        >>> glass = Person("John", 32)  # инициализация экземпляра класса
        """
        if not isinstance(first_name, str):
            raise TypeError("First name must be str")
        self.first_name = first_name

        if not isinstance(age, int):
            raise TypeError("Age must be integer")
        if age < 0:
            raise ValueError("Age must be positive integer")
        self.age = age

    def is_adult(self) -> bool:
        """
        Функция которая проверяет является ли человек совершеннолетним

        :return: Является ли человек совершеннолетним

        Примеры:
        >>> glass = Person("John", 32)  # инициализация экземпляра класса
        >>> glass.is_adult()  # вызов метода
        True
        """
        return self.age >= 18

    def increment_age(self) -> None:
        """
        Добавить к возрасту один год.

        Примеры:
        >>> john = Person("John", 32)
        >>> john.increment_age()
        """
        self.age += 1


class Rectangle:
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param width: Ширина
        :param height: Высота

        Примеры:
        >>> rectangle = Rectangle(5, 3)  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Width name must be int or float")
        elif width < 0:
            raise ValueError("Width must be positive int or float")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Height must be integer or float")
        if height < 0:
            raise ValueError("Height must be positive integer or float")
        self.height = height

    def get_perimeter(self) -> float:
        """
        Функция которая высчитывает и возвращает периметр прямоугольгика

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(5, 3)  # инициализация экземпляра класса
        >>> rectangle.get_perimeter()  # вызов метода
        16
        """
        return self.width * 2 + self.height * 2

    def get_area(self) -> float:
        """
        Функция которая высчитывает и возвращает площадь прямоугольгика

        :return: Площадь прямоугольгика

        Примеры:
        >>> rectangle = Rectangle(5, 3)  # инициализация экземпляра класса
        >>> rectangle.get_area()  # вызов метода
        15
        """
        return self.width * self.height


class BankAccount:
    def __init__(self, start_sum: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Банковский счёт"

        :param start_sum: Начальное кол-во денег

        Примеры:
        >>> bank_account = BankAccount(5000)  # инициализация экземпляра класса
        """
        if not isinstance(start_sum, (int, float)):
            raise TypeError("Start sum of money must be int or float")
        elif start_sum < 0:
            raise ValueError("Start sum of money must be positive int or float")
        self.sum = start_sum

    def get_current_sum(self) -> Union[int, float]:
        """
        Функция которая возвращает кол-во денег в настоящий момент времени

        :return: Кол-во денег в настоящий момент времени

        Примеры:
        >>> bank_account = BankAccount(5000)  # инициализация экземпляра класса
        >>> bank_account.get_current_sum()  # вызов метода
        5000
        """
        return self.sum

    def add_money(self, money: Union[int, float]) -> None:
        """
        Функция которая начисляет указанную сумму на счёт

        Примеры:
        >>> bank_account = BankAccount(5000)  # инициализация экземпляра класса
        >>> bank_account.add_money(2500)  # вызов метода
        >>> bank_account.get_current_sum()
        7500
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Money must be int or float")
        elif money < 0:
            raise ValueError("Money must be positive int or float")
        self.sum += money

    def take_money(self, money: Union[int, float]) -> None:
        """
        Функция которая начисляет указанную сумму на счёт

        Примеры:
        >>> bank_account = BankAccount(5000)  # инициализация экземпляра класса
        >>> bank_account.take_money(2500)  # вызов метода
        >>> bank_account.get_current_sum()
        2500
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Money must be int or float")
        elif money < 0:
            raise ValueError("Money must be positive int or float")
        self.sum -= money


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
