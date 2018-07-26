# This file contains the datum_helper(arg, arg, arg, ... ) function, which takes arg arg arg and opens an HTML document that displays a graph.

from .. search.search_imports import *
from .. graph.composers.gantt.ant_gantt_c \
        import ant_gantt_c
from .. graph.composers.gantt.one_gantt_c \
        import one_gantt_c
from .. graph.composers.line.ant_line_c \
        import ant_line_c
from .. graph.composers.line.one_line_c \
        import one_line_c

def datum_helper(datum, double_tuple):
    """
    Searches through all data attached to a specific timestamp, and returns a
    graph.

    Parameters:
        datum (Datum) : all YTLA data from Datum and Antenna_Snapshot attached
                       to a specific timestamp

        double_tuple (tuple) : the graph and associated metadata

    Returns:
        double_tuple (tuple) : An instance of Graph and a tuple of metadata
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]

    # parse a string (datum.timestamp) as a datetime.datetime
    timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")

    # TODO: check the accuracy of these timestamps
    # TODO: make this go _just_ past the end, so as to save a DB scrape

    # Check whether the element of consideration is within the time range of
    # interest.
    if (timestamp >= graph_meta_data['begin']) and (timestamp <= graph_meta_data['end']):
        if (graph_meta_data['attribute'] in gantt_chart_per_antenna):
            graph = ant_gantt_c(datum, double_tuple)
        elif (graph_meta_data['attribute'] in lone_gantt_chart):
            graph = one_gantt_c(datum, double_tuple)
        elif (graph_meta_data['attribute'] in line_chart_per_antenna):
            graph = ant_line_c(datum, double_tuple)
        else: # (graph_meta_data['attribute'] in lone_line_chart):
            graph = one_line_c(datum, double_tuple)

        graph.x_values.append(datum.timestamp)

    graph_meta_data['data_count'] += 1 # TODO: this must be in the time range, not the DB

    double_tuple = (graph, graph_meta_data)
    return double_tuple
