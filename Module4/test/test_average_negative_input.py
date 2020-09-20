import unittest
from Module4.input_Validation.Average import average
def test_average_exception(self):
    with self.assertRaises(ValueError):
      result = average(-90, 89, 78)
