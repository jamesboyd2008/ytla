# This file contains the definition of the one_line_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_line_c(data, graph_meta_data, count, handicap = None):
    """
    This function processes data to be graphed as a single-line line chart.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        count (int) : The quantity of elements in data.
        handicap (int) : records with indicies divisible by this number will be
                         included in the graph. Others will not be included.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = Graph()

    for index in range(0, count, handicap):
        # Add the x coordinate of the (x,y) pair
        graph.x_values.append(data[index].timestamp.replace('_', ' '))
        # Add the y coordinate of the (x,y) pair
        graph.lone_y_values.append(data[index][graph_meta_data['attribute']])

    return graph
