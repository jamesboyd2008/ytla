# This file contains the definition of the one_line_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_line_c(data, graph_meta_data, x_val_quant):
    """
    This function processes data to be graphed as a single-line line chart.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        x_val_quant (int) : The quantity of x coordinates available for graphing
    Returns:
        graph (Graph) : Data that will be graphed.
    """

    # The object to be graphed.
    graph = Graph()
    # Establish the seconds to be graphed, which aren't chosen by the user.
    # TODO: implement the incrementing of this value for max. gran. of 5 sec.
    sec = '0'

    for datum in data:
        # replace underscore for plotly processing
        moment = datum.timestamp.replace('_', ' ')
        # Add the x coordinate of the (x,y) pair
        graph.x_values.append(moment)
        # Grab the minute from the timestamp sans leading zero.
        # TODO: increment of this value for max. gran. of 5 sec
        min = str(int(moment[14:16]))
        # Add the y coordinate of the (x,y) pair
        graph.lone_y_values.append(datum[graph_meta_data['attribute']][min][sec])

    return graph
