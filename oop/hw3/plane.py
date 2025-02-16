"""
создайте класс `Plane`, наследник `Vehicle`

В модуле plane создайте класс Plane:
Класс Plane должен быть наследником Vehicle.
Добавьте атрибуты cargo и max_cargo классу Plane.
Добавьте max_cargo в инициализатор (переопределите родительский).
Объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload.
Объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления.
"""
from oop.hw3.base import Vehicle
from oop.hw3.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, max_cargo, weight=700, fuel=50, fuel_consumption=7):
        super().__init__(weight, fuel, fuel_consumption)
        self._cargo = 0
        self._max_cargo = max_cargo

    def load_cargo(self, cargo_to_load: int):
        cargo_sum = cargo_to_load + self._cargo
        if cargo_sum <= self._max_cargo:
            self._cargo = cargo_sum
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        self._cargo, result = 0, self._cargo
        return result
