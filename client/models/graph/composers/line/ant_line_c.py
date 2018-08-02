# This file contains the definition of the ant_line_c function.

import time
from ... Graph import Graph
from .... datum.Datum import Datum

def ant_line_c(data, graph_meta_data, count, handicap = None):
    """
    This function processes data to be graphed as a multi-line plot.

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

        for antenna in range(0, 8):
            graph.y_values_per_antenna[antenna].\
            append(data[index].antennas[antenna][graph_meta_data['attribute']])

    return graph
