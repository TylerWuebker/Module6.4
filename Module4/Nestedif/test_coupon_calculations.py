import unittest
import calc
from Module4.Nestedif.coupon_calculations import calculate_price

class TestCalc(unittest.TestCase):
    def test_price(self):
        result = calculate_price(100.00, 5.00, 10.00)
        self.assertEqual(result, 90.63)

    def price_under_10(self):
        result = calculate_price(9, 5, 10)
        self.assertEqual(result)
        result = calculate_price(5, 5, 15)
        self.assertEqual(result)
        result = calculate_price(4, 5, 20)
        self.assertEqual(result)
        result = calculate_price(1, 10, 10)
    def price_under_between_10_30(self):
        result = calculate_price(20, 5, 10)
        self.assertEqual(result)
        result = calculate_price(25, 5, 15)
        self.assertEqual(result)
        result = calculate_price(11, 5, 20)
        self.assertEqual(result)
        result = calculate_price(15, 10, 10)
    def price_under_between_30_50(self):
        result = calculate_price(35, 5, 10)
        self.assertEqual(result)
        result = calculate_price(30, 5, 15)
        self.assertEqual(result)
        result = calculate_price(40, 5, 20)
        self.assertEqual(result)
        result = calculate_price(45, 10, 10)
    def price_under_over_50(self):
        result = calculate_price(100, 5, 10)
        self.assertEqual(result)
        result = calculate_price(200, 5, 15)
        self.assertEqual(result)
        result = calculate_price(50, 5, 20)
        self.assertEqual(result)
        result = calculate_price(51, 10, 10)
if __name__ == '__main__':
    unittest.main()

