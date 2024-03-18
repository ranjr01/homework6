#Acceptance Test for Feature A
import unittest
from unittest.mock import patch
from main import get_previous_sprints_points, calculate_velocity

class TestFeatureAAcceptance(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['3,5,8,13'])
    def test_feature_a_acceptance_happy_path(self, mock_input):
        # Test happy path scenario
        self.assertEqual(calculate_velocity(get_previous_sprints_points()), 7.25)
    @patch('builtins.input', side_effect=[''])
    def test_calculate_velocity_empty_input(self, mock_input):
        # Test scenario with empty input
        self.assertEqual(calculate_velocity([]), 0)

    @patch('builtins.input', side_effect=['abc', '10, 20, xyz'])
    def test_calculate_velocity_invalid_input(self, mock_input):
        # Test scenario with invalid input (non-numeric values)
        self.assertEqual(calculate_velocity([]), 0)

    # Add more test cases to cover other scenarios

if __name__ == '__main__':
    unittest.main()
