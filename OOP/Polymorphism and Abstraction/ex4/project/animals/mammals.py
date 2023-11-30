from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):
    FOOD_COEF = 0.10
    FOOD_TYPE = [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    FOOD_COEF = 0.40
    FOOD_TYPE = [Meat]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    FOOD_COEF = 0.30
    FOOD_TYPE = [Meat, Vegetable]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    FOOD_COEF = 1.00
    FOOD_TYPE = [Meat]

    def make_sound(self):
        return "ROAR!!!"
