import unittest
from totalHours import calculate_total_hours

class TestCalculateTotalHours(unittest.TestCase):
    def test_positive_case(self):
        items = ['Item 1', 'Item 2', 'Item 3']
        attendances = [2, 3, 4]
        result = calculate_total_hours(attendances)
        self.assertEqual(result, 9)

    def test_negative_case_empty_lists(self):
        items = []
        attendances = []
        result = calculate_total_hours(attendances)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()