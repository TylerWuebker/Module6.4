import unittest

from Module4.input_Validation.Average import average


class TestCalc(unittest.TestCase):

    def test_average(self):
        result = average(90, 89, 78)
        self.assertEqual(result, 85.66666666666667)

if __name__ == '__main__':
    unittest.main()
