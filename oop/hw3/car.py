"""
создайте класс `Car`, наследник `Vehicle`
"""
from oop.hw3.base import Vehicle
from oop.hw3.engine import Engine


class Car(Vehicle):
    def __init__(self, weight = 700, fuel = 50, fuel_consumption = 7):
        super().__init__(weight, fuel, fuel_consumption)
        self._engine = None

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self._engine = engine
        else:
            raise ValueError
