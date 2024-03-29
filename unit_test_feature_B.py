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
        # Calculate the expected total available effort-minutes for the team
        expected_effort_minutes_team = (10 - 1 - 1) * (6 * 60) + (10 - 2 - 0) * (7 * 60)
        
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), expected_effort_minutes_team)

    def test_calculate_effort_hour_capacity_negative_sprint_days(self):
        # Test for negative sprint days
        sprint_days = -5
        team_member_details = [{'days_off': 1, 'committed_days': 1, 'available_hours': (6, 8)}]
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

    def test_calculate_effort_hour_capacity_empty_team(self):
        # Test scenario with an empty team
        sprint_days = 10
        team_member_details = []
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

    def test_calculate_effort_hour_capacity_zero_sprint_days(self):
        # Test scenario with zero sprint days
        sprint_days = 0
        team_member_details = [
            {'days_off': 1, 'committed_days': 1, 'available_hours': (6, 8)},
            {'days_off': 2, 'committed_days': 0, 'available_hours': (7, 9)}
        ]
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

    def test_calculate_effort_hour_capacity_zero_effort_members(self):
        # Test scenario with team members having zero available hours
        sprint_days = 10
        team_member_details = [
            {'days_off': 1, 'committed_days': 1, 'available_hours': (0, 0)},
            {'days_off': 2, 'committed_days': 0, 'available_hours': (0, 0)}
        ]
        self.assertEqual(calculate_effort_hour_capacity(sprint_days, team_member_details), 0)

if __name__ == '__main__':
    unittest.main()
