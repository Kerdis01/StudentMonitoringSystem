import unittest
from totalHours import app
from totalHours import calculate_total_hours

class TestCalculateTotalHours(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_positive_case(self):
        attendances = [2, 3, 4]
        result = calculate_total_hours(attendances)
        self.assertEqual(result, 9)

    def test_negative_case_empty_lists(self):
        attendances = []
        result = calculate_total_hours(attendances)
        self.assertEqual(result, 0)

    def test_endpoint_availability(self):
        response = self.client.get('/calculate_total_hours')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('total_hours', data)

if __name__ == '__main__':
    unittest.main()