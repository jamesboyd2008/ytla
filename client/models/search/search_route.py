# This file contains the definition of the searchy function, which handles user
# provided information from the client to yield the desired visualization.

from . search_imports import *
from .. datum.datum_helper import datum_helper
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

    # TODO: use hash to rename visualizaiton.html

    # querry the DB
    try:
        # Get everything from the DB in the range of interest.
        query_start = time.perf_counter()

        # Query the DB, returning only the field of interest.
        data = Datum.objects(timestamp__gte=graph_meta_data['begin'], \
                             timestamp__lte=graph_meta_data['end']).\
                                     only( timestamp, refer,  )
        # If you later need the missing fields, just call reload() on document.

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
