# main.py
from velocity_calculator import calculate_velocity
from effort_hour_calculator import calculate_effort_hour_capacity

def get_previous_sprints_points():
    try:
        points_str = input("Enter previous sprint points (comma-separated): ")
        return list(map(int, points_str.split(',')))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_previous_sprints_points()
    
def get_sprint_days_and_team_details():
    try:
        sprint_days = int(input("Enter the number of sprint days: "))
        team_size = int(input("Enter the number of team members: "))
        
        team_member_details = []
        for _ in range(team_size):
            member_details = {
                'days_off': int(input("Enter days off for a team member: ")),
                'committed_days': int(input("Enter days committed to Sprint ceremonies: ")),
                'available_hours': tuple(map(int, input("Enter available hours per day as a range (e.g., 6 8): ").split()))
            }
            team_member_details.append(member_details)

        return sprint_days, team_member_details
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_sprint_days_and_team_details()

def main():
    print("Welcome to Sprint Calculator!")

    # Feature A: Calculate a sprint team’s velocity
    previous_sprints_points = get_previous_sprints_points()
    velocity = calculate_velocity(previous_sprints_points)
    print(f"Sprint Velocity: {velocity}")

    # Feature B: Calculate Team Effort-Hour Capacity
    sprint_days, team_member_details = get_sprint_days_and_team_details()
    effort_hour_capacity = calculate_effort_hour_capacity(sprint_days, team_member_details)
    print(f"Effort Hour Capacity: {effort_hour_capacity} hours")


if __name__ == "__main__":
    main()