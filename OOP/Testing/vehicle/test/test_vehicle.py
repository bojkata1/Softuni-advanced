import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    horse_power = 115.5
    fuel = 3.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attributes_type(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_not_enough_fuel_raised(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_too_much_fuel_raised(self):
        self.vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_drive_successful(self):
        self.vehicle.drive(2)
        self.assertEqual(1, self.vehicle.fuel)

    def test_refuel_successful(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1.5)
        self.assertEqual(2.5, self.vehicle.fuel)

    def test_str(self):
        self.vehicle.fuel = 2.5

        expected =f"The vehicle has {self.horse_power} " \
               f"horse power with 2.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    unittest.main()
