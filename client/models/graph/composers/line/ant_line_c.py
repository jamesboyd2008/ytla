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
    # Identify the hour at which to begin plotting and remove any leading '0'.
    hr = str(int(datum.timestamp[11:13]))
    # Identify the minute at which to begin plotting and remove any leading '0'.
    min = str(int(datum.timestamp[14:16]))
    sec = '0' # The user-facing GUI allows a maximum granularity of one minute.

    for datum in data:
        # process the DB document, a single hour's worth of diagnostic data.
        graph = ant_line_helper(datum, graph, hr, min, sec)

    return graph
