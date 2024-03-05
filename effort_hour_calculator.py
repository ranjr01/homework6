# effort_hour_calculator.py
def calculate_effort_hour_capacity(sprint_days, team_member_details):
    if sprint_days <= 0:
        return 0

    total_effort_minutes_team = 0

    for member_details in team_member_details:
        days_off = member_details.get('days_off', 0)
        committed_days = member_details.get('committed_days', 0)
        available_minutes_range = tuple(map(lambda hours: hours * 60, member_details.get('available_hours', (0, 0))))

        available_minutes = min(available_minutes_range)
        total_effort_minutes_person = (sprint_days - days_off - committed_days) * available_minutes
        print(f"Available Effort-Minutes for {member_details}: {total_effort_minutes_person} minutes")

        total_effort_minutes_team += total_effort_minutes_person

        # total_effort_hours += (sprint_days - days_off - committed_days) * available_hours
    print(f"Total Available Effort-Minutes for Team: {total_effort_minutes_team} minutes")
    return total_effort_minutes_team
