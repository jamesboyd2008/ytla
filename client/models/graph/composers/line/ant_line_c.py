# This file contains the definition of the ant_line_c function.

from . ant_line_helper import ant_line_helper
from ... Graph import Graph
from .... datum.Datum import Datum

def ant_line_c(data, graph_meta_data, x_val_quant):
    """
    This function processes data to be graphed as a multi-line plot.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        x_val_quant (int) : The quantity of x coordinates available for graphing

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    # The object to be graphed.
    graph = Graph()
    # Grab the hour from the timestamp.
    hr = int(data[0].timestamp[11:13])
    # Grab the minute from the timestamp.
    min = int(data[0].timestamp[14:16])

    for datum in data:
        # process the DB document, a single hour's worth of diagnostic data.
        graph = ant_line_helper(datum, graph, graph_meta_data, hr, min)
        min, sec = 0, 0
    return graph
