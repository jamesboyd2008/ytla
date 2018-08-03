# This file contains the function definition for timerator()

def timerator(time):
    """
    This function converts a timestamp from one format to another.

    Parameters:
        time (str) : a timestamp, formatted thusly: MM/DD/YYYY HH:MM AM
                                         or thusly: MM/DD/YYYY H:MM AM

    Returns:
        time (str) : a timestamp, formatted thusly: YYYY-MM-DD_HH:MM
    """

    # Ensure the hour is being represented with two characters
    if (time[12] == ':'):
        # prepend the single hour character with a "0"
        time = time[slice(0, 11)] + "0" + time[slice(11, 18)]

    #############  Begin handling of AM/PM confusion #############
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
    #############  End   handling of AM/PM confusion #############

    # Move numbers around. Add underscore. Add hyphens.
    time = time[slice(6, 10)]  + '-' + time[slice(0, 2)]   + '-' +\
           time[slice(3, 5)]   + '_' + time[slice(11, 13)] + ':' +\
           time[slice(14, 16)]

    return time
