#!/usr/bin/python

# This file contains the periodic aggregation script. It is meant to run
# continuously, in the background.

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from models.graph.chart_picker import attribute_names
from models.datum.Datum import Datum
from models.graph.Graph import Graph
from models.search.search_route import searchy
import datetime
from is_6_am import is_6_am
from mongoengine import *
import time

def main():
    """
    Daily, this function compiles collections of (x,y) coordinates
    for quick visualization.
    """

    days_running = 0
    one_day = datetime.timedelta(days = 1)

    while days_running < 1:
    # while True:

        # sleep one day
        # time.sleep(86400) # 60 s/min * 60 min/hr * 24 hr/day = 86400 s/day

        start = time.perf_counter()

        connect('ytla')
        # Determine whether the day has already been aggregated.
        # Find the most recent aggregation, if it exists.

        # Determine dates (strings) to be used as query arguments.
        # yesterdate = (datetime.datetime.now() - one_day).date()
        yesterdate = datetime.date(2018, 8, 3)
        midnight = datetime.time(0, 0, 0)
        almost_midnight = datetime.time(23, 59, 59)
        begin = datetime.datetime.combine(yesterdate, midnight)
        end = datetime.datetime.combine(yesterdate, almost_midnight)
        begin = datetime.datetime.strftime(begin, "%Y-%m-%d_%H:%M")
        end = datetime.datetime.strftime(end, "%Y-%m-%d_%H:%M")

        attrs = attribute_names

        # Make a Graph object for every attribute.
        for i in len(attrs):
            # Conduct a DB query of the past 24 hours
            try:
                graph = searchy(begin, end, attrs[i], True)
                aggr = Aggregation()
                aggr.timestamp = yesterday
                aggr.attr = attrs[i]
                aggr.graph = graph
                aggr.save()
            except Exception as err:
                print(err)

            print('\r', end = '')
            print(f"Daily data aggregation is {(i / 147 * 100):.2f}% complete.")

        end = time.perf_counter()
        print()
        print(f"Time elapsed (seconds) for data aggregation: {end - start}")
        days_running += 1

if __name__ == '__main__':
    main()
