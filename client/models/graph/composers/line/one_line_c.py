# This file contains the definition of the one_line_c function.

from . one_line_helper import one_line_helper
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
    # Grab the hour at which to begin graphing.
    hr = int(graph_meta_data['begin'][11:13])
    # Grab the minute at which to begin graphing.
    min = int(graph_meta_data['begin'][14:16])
    # The number of days in data
    quant = data.count()

    # Iterate over the 24 hour blocks of data.
    for i in range(quant):
        # Determine whether this is the last day in the set of relevant days.
        if i == quant - 1: # It's the last day.
            end_hr = int(graph_meta_data['end'][11:13])
            end_min = int(graph_meta_data['end'][14:16])
        else: # It's not the last day, yet.
            end_hr = 23
            end_min = 59

        # process the DB document, a single day's worth of diagnostic data.
        graph = one_line_helper(
            data[i], graph, graph_meta_data, hr, min, end_hr, end_min)
        hr, min = 0, 0

    return graph
