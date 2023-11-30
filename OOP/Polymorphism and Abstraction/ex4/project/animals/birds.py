from project.animals.animal import Bird
from project.food import *


class Owl(Bird):
    FOOD_COEF = 0.25
    FOOD_TYPE = [Meat]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    FOOD_COEF = 0.35
    FOOD_TYPE = [Meat, Vegetable, Seed, Fruit]

    def make_sound(self):
        return "Cluck"
