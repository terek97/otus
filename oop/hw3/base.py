from abc import ABC

from oop.hw3.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight = 700, fuel = 50, fuel_consumption = 7):
        """

        :param weight: kg
        :param fuel: liters
        :param fuel_consumption: liters/100km
        """
        self._weight = weight
        self._started = False
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def start(self):
        if not self._started:
            if self._fuel > 0:
                self._started = True
            else:
                raise LowFuelError

    def move(self, distance):
        necessary_field = distance * self._fuel_consumption / 100
        if necessary_field > self._fuel:
            raise NotEnoughFuel
        self._fuel -= necessary_field