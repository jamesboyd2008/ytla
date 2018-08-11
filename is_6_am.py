# This file contains the function definition for is_6_am

import datetime

def is_6_am(moment):
    """
    This function determines whether it's 6 A.M.

    Input:
        moment (datetime.datetime) : The instance of time in question.

    Returns:
        (bool) : Whether moment is 6 A.M.
    """

    if moment.hour == 6 and moment.minute == 0 and moment.second == 0:
        return True
    else:
        return False
