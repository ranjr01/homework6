# velocity_calculator.py
def calculate_velocity(previous_sprints_points):
    if not previous_sprints_points:
        return 0
    
    total_points = sum(previous_sprints_points)
    average_velocity = total_points / len(previous_sprints_points)
    return average_velocity
