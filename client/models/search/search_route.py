# This file contains the definition of the searchy function, which handles user
# provided information from the client to yield the desired visualization.

from . search_imports import *
from .. datum.datum_helper import *
from .. graph.graphers.plotter import plotter

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
    connect('ytla')

    graph_meta_data = {
        # The user provided "begin", the beginning of the time range of interest
        'begin': begin,
        # The user provided "end", the ending of the time range of interest
        'end': end,
        # The user's choice from the dropdown
        'attribute': refer
    }

    # The object that will get graphed
    graph = Graph()

    # querry the DB
    try:
        # Get everything from the DB in the range of interest.
        query_start = time.perf_counter()
        data = Datum.objects(__raw__={\
        'timestamp': {"$gte": graph_meta_data['begin']}, \
        'timestamp': {"$lte": graph_meta_data['end']}})
        query_end = time.perf_counter()
        print(f"seconds elapsed for DB query: {query_end - query_start}")

        processing_start = time.perf_counter()
        # Process the data, depending on how it is to be visualized.
        if (graph_meta_data['attribute'] in gantt_chart_per_antenna):
            graph = ant_gantt_c(data, graph_meta_data)
        elif (graph_meta_data['attribute'] in lone_gantt_chart):
            graph = one_gantt_c(data, graph_meta_data)
        elif (graph_meta_data['attribute'] in line_chart_per_antenna):
            graph = ant_line_c(data, graph_meta_data)
        else: # (graph_meta_data['attribute'] in lone_line_chart):
            graph = one_line_c(data, graph_meta_data)

        processing_end = time.perf_counter()
        print(f"seconds elapsed for pre-plotly processing: {processing_end - processing_start}")

    except Exception as err:
        print(err)

    # plot the graph
    plottable = plotter(graph, graph_meta_data)
    return plottable
