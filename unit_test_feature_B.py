#Unit Test for Feature B
import unittest
from effort_hour_calculator import calculate_effort_hour_capacity

class TestFeatureB(unittest.TestCase):
    def test_calculate_effort_hour_capacity_happy_path(self):
        # Test happy path scenario
        sprint_days = 10
        team_member_details = [
            {'days_off': 1, 'committed_days': 1, 'available_hours': (6, 8)},
            {'days_off': 2, 'committed_days': 0, 'available_hours': (7, 9)}
        ]
        expected_effort_hours_team = (10 - 1 - 1) * 6 + (10 - 2 - 0) * 7
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), expected_effort_hours_team)

    def test_calculate_effort_hour_capacity_negative_sprint_days(self):
        # Test for negative sprint days
        sprint_days = -5
        team_member_details = [{'days_off': 1, 'committed_days': 1, 'available_hours': (6, 8)}]
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

    # Add more test cases to cover other scenarios

if __name__ == '__main__':
    unittest.main()
