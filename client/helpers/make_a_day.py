# This file contains the definition of the make_a_day function.

def make_a_day(initial_value):
    """
    This function returns a dict representation of a day.

    Parameters:
        intial_value (any class) : The default value for the second.

    Returns:
        day (dict) : includes hours, minutes, and every other second.
    """
    day = {}
    for hour in range(24):
        day[str(hour)] = {}
        for minute in range(60):
            day[str(hour)][str(minute)] = {}
            for second in range(0, 60, 2):
                day[str(hour)][str(minute)][str(second)] = initial_value

    return day
