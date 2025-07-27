import random
from random import randint
from car import Car

class UnreliableCar(Car):
    """A special car that does not drive reliably"""

    def __init__(self,name, fuel, reliability):
        """Initialize an UnreliableCar with a random reliability percentage
        Args:
            name(str): name of car
            fuel(int): fuel of car
            reliability(int) : 0-100 percentage
        """
        super().__init__(name, fuel)
        self.reliability = reliability