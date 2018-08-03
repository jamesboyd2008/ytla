# This file contains the definition of the one_line_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_line_c(data, graph_meta_data):
    """
    This function processes data to be graphed as a single-line line chart.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = Graph()

    for datum in data:
        # Add the x coordinate of the (x,y) pair
        graph.x_values.append(datum.timestamp.replace('_', ' '))
        # Add the y coordinate of the (x,y) pair
        graph.lone_y_values.append(datum[graph_meta_data['attribute']])

    return graph
