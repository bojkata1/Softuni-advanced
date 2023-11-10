class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horsepower):
        self.fuel = fuel
        self.horse_power = horsepower
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        consumption = self.fuel_consumption * kilometers
        if self.fuel >= consumption:
            self.fuel -= consumption
