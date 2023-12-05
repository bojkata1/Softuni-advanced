import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal("TestName", "TestType", "TestSound")

    def test_correct_initialization(self):
        self.assertEqual("TestName", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("TestSound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_function(self):
        result = self.mammal.info()
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", result)


if __name__ == "__main__":
    unittest.main()
