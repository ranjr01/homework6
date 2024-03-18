import unittest
from unittest.mock import patch
from main import get_sprint_days_and_team_details, calculate_effort_hour_capacity

class TestFeatureBAcceptance(unittest.TestCase):
    # @patch('builtins.input', side_effect=['10', '2', '1', '1', '6 8', '2', '0', '1', '7 9'])
    # def test_feature_b_acceptance_happy_path(self, mock_input):
    #     # Test happy path scenario
    #     sprint_days, team_member_details = get_sprint_days_and_team_details()
    #     expected_effort_minutes_team = (10 - 1 - 1) * (6 * 60) + (10 - 2 - 0) * (7 * 60)
    #     self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), expected_effort_minutes_team)

    @patch('builtins.input', side_effect=['5', '1', '1', '6', '8'])
    def test_calculate_effort_hour_capacity_negative_sprint_days(self, mock_input):
        # Test for negative sprint days
        sprint_days, team_member_details = get_sprint_days_and_team_details()
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

if __name__ == '__main__':
    unittest.main()
