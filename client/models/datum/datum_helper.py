# This file contains the datum_helper(arg, arg, arg, ... ) function, which takes arg arg arg and opens an HTML document that displays a graph.

from .. search.search_imports import *
from .. graph.composers.gantt.ant_gantt_c import ant_gantt_c
from .. graph.composers.gantt.one_gantt_c import one_gantt_c
from .. graph.composers.line.ant_line_c import ant_line_c
from .. graph.composers.line.one_line_c import one_line_c

def datum_helper(data, graph_meta_data):
    """
    Searches through all data attached to a specific timestamp, and returns a
    graph.

    Parameters:
        data (mongoengine.QuerySet) : DB records returned from a query

        graph_meta_data (dict) : user-provided information about the graph

    Returns:
        graph (Graph) : data that whill be graphed
    """

    # The object that will get graphed
    graph = Graph()

    # To ensure that no more than 500 points are plotted.
    count = data.count()
    # TODO: pick handicap more smartlier
    if count > 1000:
        if count > 100000000:
            handicap = 8000000
        elif count > 10000000:
            handicap = 800000
        elif count > 1000000:
            handicap = 80000
        elif count > 100000:
            handicap = 8000
        elif count > 10000:
            handicap = 800
    else:
        handicap = 1
    print(f"big data.count() --> {data.count()}")
    # Choose appropriate visualization
    if (graph_meta_data['attribute'] in gantt_chart_per_antenna):
        graph = ant_gantt_c(data, graph_meta_data, handicap)
    elif (graph_meta_data['attribute'] in lone_gantt_chart):
        graph = one_gantt_c(data, graph_meta_data, handicap)
    elif (graph_meta_data['attribute'] in line_chart_per_antenna):
        graph = ant_line_c(data, graph_meta_data, count, handicap)
    else: # (graph_meta_data['attribute'] in lone_line_chart):
        graph = one_line_c(data, graph_meta_data, handicap)

    return graph
