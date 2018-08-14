# This file contains the definition of the quick_search function.

# from . search_imports import *
import datetime
from .. graph.graphers.plotter import plotter
from .. aggregation.Aggregation import Aggregation
from mongoengine import *
import time
import json

def quick_search(quick, refer):
    """
    This function searches the DB.

    This function searches the DB, making a plotly graph out of all items that
    match the contextually derived search criteria, which is attribute and
    a timestamp.

    Parameters:
        quick (str) : The date of interest --> '%Y-%m-%d_%H:%M'
        refer (str) : The attribute of interest, e.g., sel1x

    Returns:
        plottable (bool) : Whether the graph is plottable.
            or
        graph (Graph) : If this query originated from a periodic aggregation
                        script, then a coordinate cluster object (Graph) is
                        returned.
    """

    # assuming mongod is running on 'localhost' at port 27017
    # Connect to the DB
    connect('ytla')

    # Determine dates (strings) to be used as query arguments.
    one_day = datetime.timedelta(days = 1)
    day = datetime.datetime.strptime(quick, "%Y-%m-%d_%H:%M").date()
    midnight = datetime.time(0, 0, 0)
    almost_midnight = datetime.time(23, 59, 59)
    begin = datetime.datetime.combine(day, midnight)
    end = datetime.datetime.combine(day, almost_midnight)
    begin = datetime.datetime.strftime(begin, "%Y-%m-%d_%H:%M")
    end = datetime.datetime.strftime(end, "%Y-%m-%d_%H:%M")

    graph_meta_data = {
        # The user provided "begin", the beginning of the time range of interest
        'begin': begin,
        # The user provided "end", the ending of the time range of interest
        'end': end,
        # The user's choice from the dropdown
        'attribute': refer
    }
    # Clock the wait time
    query_start = time.perf_counter()

    # querry the DB
    try:

        graphs = []
        # Query the DB
        for aggr in Aggregation.objects:
            # Grab the relevant data from the DB.
            if aggr.timestamp == quick[0:10] and aggr.attr == refer:
                graphs.append(aggr)

        # The two lines below this line produce a good QuerySet, sans day one.
        # data = Datum.objects(timestamp__gte=graph_meta_data['begin'], \
        #                      timestamp__lte=graph_meta_data['end'])

    except Exception as err:
        print(err)

    # plot the graph
    plottable = plotter(graphs[0].graph, graph_meta_data)

    query_end = time.perf_counter()
    print(f"seconds elapsed before plotly: {query_end - query_start}")

    return plottable
