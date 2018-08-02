# This file contains the definition of the make_an_hour function.

def make_an_hour(initial_value):
    """
    This function returns a dict representation of an hour.

    Parameters:
        intial_value (any class) : The default value for the second.

    Returns:
        hour (dict) : includes 60 minutes, and every fifth second.
    """
    hour = {}
    for minute in range(60):
        hour[str(minute)] = {}
        for second in range(0, 60, 5):
            hour[str(minute)][str(second)] = initial_value

    return hour
