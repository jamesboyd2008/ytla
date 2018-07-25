# This file contains the definition for the begin_end function.

from SearchForm import SearchForm
import datetime
from timerator import timerator

def begin_end(form, which_var):
    """
    This function formats a timestamp from a SearchForm.

    Parameters:
        form (SearchForm) : a FlaskForm from an HTTP POST request.
        which_var (str) : "begin" or "end", the timestamp to format.

    Returns:
        time (str) : a timestamp formatted thusly -> YYYY-MM-DD_HH:MM:SS.
    """

    # format the timestamps
    if (form.hours_prior.raw_data[0]):
        hours = int(form.hours_prior.raw_data[0]) * -1
        begin = timerator(form.end.raw_data[0])
        # Get a datetime.datetime from a str.
        begin = datetime.datetime.strptime(begin, "%Y-%m-%d_%H:%M:%S")
        subtrahend = datetime.timedelta(hours = hours)
        begin += subtrahend
        # Get a str from a datetime.datetime
        begin = datetime.datetime.strftime(begin, "%Y-%m-%d_%H:%M:%S")
    else:
        begin = timerator(form.from_timestamp.raw_data[0])
    end = timerator(form.end.raw_data[0])

    if which_var == "begin":
        time = begin
    else:
        time = end

    return time
