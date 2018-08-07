# This file contains the definition of the make_a_day function.

def make_a_day(initial_value):
    """
    This function returns a dictionary representation of a day.

    Parameters:
        intial_value (any class) : The default value for every minute.

    Returns:
        day (dict) : includes 24 hours, each with 60 minutes.
    """
    day = {}
    for hour in range(24):
        day[str(hour)] = {}
        for minute in range(0, 60):
            day[str(hour)][str(minute)] = initial_value

    return day
