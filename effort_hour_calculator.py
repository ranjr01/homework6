# effort_hour_calculator.py
def calculate_effort_hour_capacity(sprint_days, team_member_details):
    if sprint_days <= 0:
        return 0

    total_effort_hours = 0

    for member_details in team_member_details:
        days_off = member_details.get('days_off', 0)
        committed_days = member_details.get('committed_days', 0)
        available_hours_range = member_details.get('available_hours', (0, 0))

        available_hours = min(available_hours_range)
        total_effort_hours += (sprint_days - days_off - committed_days) * available_hours

    return total_effort_hours
