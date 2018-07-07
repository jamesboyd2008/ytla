# This program crops a list of timestamps.
import time
import datetime

# times_cropper(orignal_list, begin, end) crops down a list of timestamps.
# input:
#   original_list: a list of timestamps, formatted thusly: 2018-06-27 16:02:38
#   begin: a timestamp of the same format, the inclusive beginning of the
#   probably shorter list of timestamps the function will return.
#   end: a timestamp of the same format, the inclusive endning of the
#   probably shorter list of timestamps the function will return.
# output:
#   A list of all the timestamps in the original_list between begin and end,
#   inclusively.  If no timestamps in the original_list are between begin and
#   end, an empty list is returned.
def times_cropper(original_list, begin, end):
    new_list = []
    for time in original_list:
        if (time >= begin) and (time <= end):
            new_list.append(time)
    return new_list

str_times = [
    "2018-06-27 16:02:38",
    "2018-06-27 16:03:37",
    "2018-06-27 16:03:38",
    "2018-06-27 16:12:57"
]

times = []
for time in str_times:
    sometime = datetime.datetime.\
    strptime(time, "%Y-%m-%d %H:%M:%S")
    times.append(sometime)

print(
    times_cropper(
        times,
        datetime.datetime.strptime("2018-06-27 16:02:40", "%Y-%m-%d %H:%M:%S"),
        datetime.datetime.strptime("2018-06-27 16:03:39", "%Y-%m-%d %H:%M:%S")
    )
)
