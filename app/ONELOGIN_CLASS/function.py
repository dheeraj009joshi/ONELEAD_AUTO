
from datetime import datetime


def calculate_days_difference(given_date_str):
    # Step 1: Obtain the current date
    current_date =datetime.today()

    # Step 2: Determine the given date
    given_date = datetime.strptime(given_date_str, "%m/%d/%y").date()

    # Step 3: Calculate the difference in days
    days_difference = (current_date - given_date).days

    return days_difference

def time_difference_in_minutes(created_time_str, added_time_str):
    # Convert time strings to datetime objects
    created_time = datetime.strptime(created_time_str, '%m/%d/%y %I:%M %p')
    added_time = datetime.strptime(added_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Calculate the time difference in minutes
    time_difference = (added_time - created_time).total_seconds() / 60
    if time_difference<(44*60):
        return int(time_difference)
    else:
        return False

