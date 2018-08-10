# This file contains the definition of the searchy function, which handles user
# provided information from the client to yield the desired visualization.

# from . search_imports import *
import datetime
from .. datum.Datum import Datum
from .. datum.datum_helper import datum_helper
from .. graph.graphers.plotter import plotter
from mongoengine import *
import time

def searchy(begin, end, refer):
    """
    This function searches the DB.

    This function searches the DB, making a plotly graph out of all items that
    match the contextually derived search criteria, which is attribute and
    a range of timestamps.

    Parameters:
        begin (str) : The beginning of the time range of interest.
        end (str) : The end of the time range of interest.
        refer (str) : The attribute of interest, e.g., sel1x

    Returns:
        plottable (bool) : Whether the graph is plottable.
    """

    # assuming mongod is running on 'localhost' at port 27017
    # Connect to the DB
    connect('mytla')

    graph_meta_data = {
        # The user provided "begin", the beginning of the time range of interest
        'begin': begin,
        # The user provided "end", the ending of the time range of interest
        'end': end,
        # The user's choice from the dropdown
        'attribute': refer
    }

    # querry the DB
    try:
        # Get everything from the DB in the range of interest.
        query_start = time.perf_counter()

        # Query the DB for all dates within the user-provided time range
        data = []
        for datum in Datum.objects:
            day_beginning = datetime.datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")
            day_date = day_beginning.date()
            almost_midnight = datetime.time(23, 59, 59)
            day_ending = datetime.datetime.combine(day_date, almost_midnight)
            search_start = datetime.datetime.strptime(begin, "%Y-%m-%d_%H:%M")
            search_end = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M")

            # Grab the first relevant day from the DB.
            if day_beginning <= search_start and search_start <= day_ending:
                data.append(datum)
            # Grab the last relevant day from the DB.
            elif day_beginning <= search_end and search_end <= day_ending:
                data.append(datum)
            # Grab the in-between days from the DB.
            elif search_start <= day_beginning and day_beginning <= search_end:
                data.append(datum)

        # The two lines below this line produce a good QuerySet, sans day one.
        # data = Datum.objects(timestamp__gte=graph_meta_data['begin'], \
        #                      timestamp__lte=graph_meta_data['end'])

        query_end = time.perf_counter()
        print(f"seconds elapsed for DB query: {query_end - query_start}")
    except Exception as err:
        print(err)

    processing_start = time.perf_counter()
    graph = datum_helper(data, graph_meta_data)
    processing_end = time.perf_counter()
    print(f"seconds elapsed for pre-plotly processing: {processing_end - processing_start}")

    # plot the graph
    plottable = plotter(graph, graph_meta_data)
    return plottable
