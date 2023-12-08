from project.trip import Trip
from unittest import TestCase, main


class TripTest(TestCase):

    def test_init_no_family(self):
        t1 = Trip(1500.0, 1, False)
        self.assertEqual(1500.0, t1.budget)
        self.assertEqual(1, t1.travelers)
        self.assertEqual(False, t1.is_family)
        self.assertEqual({}, t1.booked_destinations_paid_amounts)

    def test_init_invalid_family(self):
        t1 = Trip(1500.0, 1, True)
        self.assertEqual(1500.0, t1.budget)
        self.assertEqual(1, t1.travelers)
        self.assertEqual(False, t1.is_family)
        self.assertEqual({}, t1.booked_destinations_paid_amounts)

    def test_init_valid_family(self):
        t1 = Trip(1500.0, 2, True)
        self.assertEqual(1500.0, t1.budget)
        self.assertEqual(2, t1.travelers)
        self.assertEqual(True, t1.is_family)
        self.assertEqual({}, t1.booked_destinations_paid_amounts)

    def test_invalid_travellers_raises(self):
        with self.assertRaises(ValueError) as ve:
            t1 = Trip(1500.0, 0, False)
        self.assertEqual('At least one traveler is required!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            t1 = Trip(1500.0, -1, False)
        self.assertEqual('At least one traveler is required!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            t1 = Trip(1500.0, 0, True)
        self.assertEqual('At least one traveler is required!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            t1 = Trip(1500.0, -1, True)
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_book_trip_invalid_destination(self):
        t1 = Trip(1500.0, 1, False)
        res = t1.book_a_trip("InvalidLocation")
        self.assertEqual('This destination is not in our offers, please choose a new one!', res)
        t1 = Trip(1500.0, 2, True)
        res = t1.book_a_trip("InvalidLocation")
        self.assertEqual('This destination is not in our offers, please choose a new one!', res)

    def test_book_trip_not_enough_money(self):
        t1 = Trip(1500.0, 1, False)
        t2 = Trip(1500.0, 2, True)
        t3 = Trip(1500.0, 2, False)

        res = t1.book_a_trip("New Zealand")
        self.assertEqual(res, 'Your budget is not enough!')
        self.assertEqual(1500.0, t1.budget)
        self.assertEqual({}, t1.booked_destinations_paid_amounts)
        res = t2.book_a_trip("New Zealand")
        self.assertEqual(res, 'Your budget is not enough!')
        self.assertEqual(1500.0, t2.budget)
        self.assertEqual({}, t2.booked_destinations_paid_amounts)
        res = t3.book_a_trip("New Zealand")
        self.assertEqual(res, 'Your budget is not enough!')
        self.assertEqual(1500.0, t3.budget)
        self.assertEqual({}, t3.booked_destinations_paid_amounts)

    def test_book_trip_no_discount(self):
        t1 = Trip(1500.0, 1, False)
        t2 = Trip(1500.0, 2, False)
        t3 = Trip(1500.0, 1, True)
        res = t1.book_a_trip("Bulgaria")
        self.assertEqual(1000.0, t1.budget)
        self.assertEqual({"Bulgaria": 500.0}, t1.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 1000.00', res)
        res = t2.book_a_trip("Bulgaria")
        self.assertEqual(500.0, t2.budget)
        self.assertEqual({"Bulgaria": 1000.0}, t2.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 500.00', res)
        res = t3.book_a_trip("Bulgaria")
        self.assertEqual(1000.0, t3.budget)
        self.assertEqual({"Bulgaria": 500.0}, t3.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 1000.00', res)

    def test_book_trip_with_discount(self):
        t1 = Trip(1500.0, 2, True)
        res = t1.book_a_trip("Bulgaria")
        self.assertEqual(600.0, t1.budget)
        self.assertEqual({"Bulgaria": 900.0}, t1.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 600.00', res)

    def test_book_multiple_trips(self):
        t1 = Trip(25000.0, 1, False)
        t2 = Trip(25000.0, 2, True)
        res = t1.book_a_trip("Brazil")
        self.assertEqual(18800.0, t1.budget)
        self.assertEqual({'Brazil': 6200}, t1.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Brazil! Your budget left is 18800.00', res)
        res = t1.book_a_trip("Bulgaria")
        self.assertEqual(18300.0, t1.budget)
        self.assertEqual({'Brazil': 6200, 'Bulgaria': 500}, t1.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 18300.00', res)
        res = t2.book_a_trip("New Zealand")
        self.assertEqual(11500.0, t2.budget)
        self.assertEqual({'New Zealand': 13500.}, t2.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination New Zealand! Your budget left is 11500.00', res)
        res = t2.book_a_trip("Australia")
        self.assertEqual(1240.0, t2.budget)
        self.assertEqual({'New Zealand': 13500.0, "Australia": 10260.0}, t2.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Australia! Your budget left is 1240.00', res)

    def test_booking_status_when_no_bookings(self):
        t1 = Trip(25000.0, 1, False)
        t2 = Trip(25000.0, 2, True)
        res = t1.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 25000.00', res)
        res = t2.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 25000.00', res)

    def test_booking_status(self):
        t1 = Trip(25000.0, 1, False)
        t1.book_a_trip("Brazil")
        t1.book_a_trip("Bulgaria")
        res = t1.booking_status()
        self.assertEqual("""Booked Destination: Brazil
Paid Amount: 6200.00
Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 18300.00""", res)
        t2 = Trip(25000.0, 2, True)
        t2.book_a_trip("New Zealand")
        t2.book_a_trip("Australia")
        res = t2.booking_status()
        self.assertEqual("""Booked Destination: Australia
Paid Amount: 10260.00
Booked Destination: New Zealand
Paid Amount: 13500.00
Number of Travelers: 2
Budget Left: 1240.00""", res)

    if __name__ == "__main__":
        main()