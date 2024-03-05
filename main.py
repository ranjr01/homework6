# main.py
from velocity_calculator import calculate_velocity

def get_previous_sprints_points():
    try:
        points_str = input("Enter previous sprint points (comma-separated): ")
        return list(map(int, points_str.split(',')))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_previous_sprints_points()

def main():
    print("Welcome to Sprint Calculator!")

    # Feature A: Calculate a sprint team’s velocity
    previous_sprints_points = get_previous_sprints_points()
    velocity = calculate_velocity(previous_sprints_points)
    print(f"Sprint Velocity: {velocity}")

if __name__ == "__main__":
    main()
