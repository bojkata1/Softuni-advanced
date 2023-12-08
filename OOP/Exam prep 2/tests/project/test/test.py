from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTests(TestCase):

    def test_init(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        self.assertEqual("TestModel", c1.model)
        self.assertEqual("TestType", c1.car_type)
        self.assertEqual(100_000, c1.mileage)
        self.assertEqual(20_000.50, c1.price)
        self.assertEqual([], c1.repairs)

    def test_invalid_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            c1 = SecondHandCar("TestModel", "TestType", 100_000, 0.0)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            c2 = SecondHandCar("TestModel", "TestType", 100_000, -1.5)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_invalid_mileage_raises(self):
        with self.assertRaises(ValueError) as ve:
            c1 = SecondHandCar("TestModel", "TestType", 0, 20_000.5)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            c1 = SecondHandCar("TestModel", "TestType", -10, 20_000.5)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promo_price_invalid_new_price_raises(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        with self.assertRaises(ValueError) as ve:
            c1.set_promotional_price(20000.50)
        self.assertEqual(20000.50, c1.price)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            c1.set_promotional_price(200000)
        self.assertEqual(20000.50, c1.price)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successful(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        res = c1.set_promotional_price(10_000.5)
        self.assertEqual(10_000.5, c1.price)
        self.assertEqual(res, 'The promotional price has been successfully set.')

    def test_need_repair_returns_impossible_repair(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        res = c1.need_repair(15000.0, "TestRepair")
        self.assertEqual('Repair is impossible!', res)
        self.assertEqual(c1.repairs, [])
        self.assertEqual(c1.price, 20_000.50)

    def test_need_repair_successful(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        res = c1.need_repair(10000.0, "TestRepair")
        self.assertEqual(c1.price, 30000.50)
        self.assertEqual(c1.repairs, ["TestRepair"])
        self.assertEqual(res, 'Price has been increased due to repair charges.')
        res = c1.need_repair(5000.5, "TestRepair 2")
        self.assertEqual(c1.price, 35001.0)
        self.assertEqual(c1.repairs, ["TestRepair", "TestRepair 2"])
        self.assertEqual(res, 'Price has been increased due to repair charges.')

    def test___gt__when_types_mismatch(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        c2 = SecondHandCar("TestModel", "TestType2", 100_000, 20_000.50)
        res = c1 > c2
        self.assertEqual('Cars cannot be compared. Type mismatch!', res)

    def test__gt__(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        c2 = SecondHandCar("TestModel", "TestType", 100_000, 10_000.0)
        res = c1 > c2
        self.assertTrue(res)

    def test__str__(self):
        c1 = SecondHandCar("TestModel", "TestType", 100_000, 20_000.50)
        res = str(c1)
        self.assertEqual(f"""Model TestModel | Type TestType | Milage 100000km
Current price: 20000.50 | Number of Repairs: 0""", res)
        c1.need_repair(10000, "test rep")
        res = str(c1)
        self.assertEqual(f"""Model TestModel | Type TestType | Milage 100000km
Current price: 30000.50 | Number of Repairs: 1""", res)

    if __name__ == "__main__":
        main()