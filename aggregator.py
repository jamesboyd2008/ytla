#!/usr/bin/python

# This file contains the periodic aggregation script. It is meant to run
# continuously, in the background.

from client.models.aggregation.Aggregation import Aggregation
from client.models.graph.chart_picker import attribute_names
from client.models.datum.Datum import Datum
from client.models.graph.Graph import Graph
from client.models.search.search_route import searchy
import datetime
# from is_6_am import is_6_am
from mongoengine import *
import time

def main():
    """
    This function compiles a day's collections of (x,y) coordinates
    for quick visualization.
    """


    start = time.perf_counter()

    connect('ytla')

    # Determine dates (strings) to be used as query arguments.
    one_day = datetime.timedelta(days = 1)
    yesterdate = (datetime.datetime.now() - one_day).date()
    # yesterdate = datetime.date(2018, 8, 3)
    midnight = datetime.time(0, 0, 0)
    almost_midnight = datetime.time(23, 59, 59)
    begin = datetime.datetime.combine(yesterdate, midnight)
    end = datetime.datetime.combine(yesterdate, almost_midnight)
    begin = datetime.datetime.strftime(begin, "%Y-%m-%d_%H:%M")
    end = datetime.datetime.strftime(end, "%Y-%m-%d_%H:%M")

    attrs = attribute_names

    # Make a Graph object for every attribute.
    for i in range(len(attrs)):
        # Conduct a DB query of the past 24 hours
        try:
            graph = searchy(begin, end, attrs[i], True)
            aggr = Aggregation()
            aggr.timestamp = datetime.datetime.strftime(yesterdate, "%Y-%m-%d")
            aggr.attr = attrs[i]
            aggr.graph = graph
            aggr.save()
        except Exception as err:
            print(err)

        print('\r', end = '')
        print(f"Daily data aggregation is {(i / 21 * 100):.2f}% complete.")

    end = time.perf_counter()
    print()
    print(f"Time elapsed (seconds) for data aggregation: {end - start}")

if __name__ == '__main__':
    main()
