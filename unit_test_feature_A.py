import unittest
from velocity_calculator import calculate_velocity

class TestFeatureA(unittest.TestCase):
    def test_calculate_velocity_happy_path(self):
        # Test happy path scenario
        points_completed = [3, 5, 8, 13]
        expected_average_velocity = 7.25
        self.assertEqual(calculate_velocity(points_completed), expected_average_velocity)

    def test_calculate_velocity_empty_input(self):
        # Test for empty input
        points_completed = []
        self.assertEqual(calculate_velocity(points_completed), 0)

    def test_calculate_velocity_single_point(self):
        # Test scenario with only one point completed
        points_completed = [5]
        self.assertEqual(calculate_velocity(points_completed), 5.0)

    def test_calculate_velocity_zero_points(self):
        # Test scenario with all zero points completed
        points_completed = [0, 0, 0, 0]
        self.assertEqual(calculate_velocity(points_completed), 0)

    def test_calculate_velocity_negative_points(self):
        # Test scenario with negative points completed
        points_completed = [-1, -3, -5]
        self.assertEqual(calculate_velocity(points_completed), -3.0)

if __name__ == '__main__':
    unittest.main()
