# This file contains the function definition for timerator()

def timerator(time):
    """
    This function converts timestamps of one specific format to another format.

    Parameters:
        time (str) : a timestamp, formatted thusly: MM/DD/YYYY HH:MM AM

    Returns:
        time (str) : a timestamp, formatted thusly: YYYY/MM/DD_HH:MM:SS
    """

    meridian = slice(-2, 20)
    hour_str = slice(11, 13)

    # midnight
    if (time[meridian] == 'AM') and (time[hour_str] == '12'):
        # Make the hours 00 and toss the AM
        time = time[slice(0, 11)] + '00' + time[slice(13, -3)]
    # all non-noon pm
    elif (time[meridian] == 'PM') and (time[hour_str] != '12'):
        hours = time[hour_str]
        hours = int(hours) + 12
        # Add 12 to the hours and toss the PM
        time = time[slice(0, 11)] + str(hours) + time[slice(13, -3)]
    else:
        # Just toss the AM/PM
        time = time[slice(0, -3)]

    return time
