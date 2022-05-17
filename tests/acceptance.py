import unittest

from src.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cal = Calculator()

    def test_posix_calculator_valid_inputs(self):

        self.assertEqual(self.cal.calc("5 2 /"), 2)

        self.assertEqual(self.cal.calc("3 7 *"), 21)

        self.assertEqual(self.cal.calc("4 7 + 2 *"), 22)

        self.assertEqual(self.cal.calc("5 2 %"), 1)

        self.assertEqual(self.cal.calc("2 3 * 11 14 * +"), 160)

    def test_postfix_calculator_invalid_inputs(self):

        # Empty input
        with self.assertRaises(ValueError):
            self.cal.calc("")

        # Invalid text input
        with self.assertRaises(ValueError):
            self.cal.calc("a 3 * 11 14 * +")

        # Invalid operator input
        with self.assertRaises(ValueError):
            self.cal.calc("2 3 ^ 11 14 * +")

        # Divided by 0 during division
        with self.assertRaises(ValueError):
            self.cal.calc("1 3 + 0 /")

        with self.assertRaises(NotImplementedError):
            self.cal.calc("1 + 1", method='infix')


if __name__ == '__main__':
    unittest.main()
