# This file contains the definition of the ant_gantt_helper function.

from ... Graph import Graph
from .... datum.Datum import Datum

def ant_line_helper(datum, graph, hr, min, sec):
    """
    This function processes one hour of one attribute's data.

    This function produces 720 (x,y) coordinates.
    60 sec/min x 60 min/hr = 3600 sec/hr
    3600 (sec/hr) * 1/5  data_points/sec = 720 data_points/hr

    Parameters:
        datum (Datum) : One hour of YTLA diagnostic information ~ 16-38 MB
        graph (Graph) : The object to be visualized.
        hr (int) : The hour in which the datum was recorded.
        min (int) : The minute in which the datum was recorded.
        sec (int) : The second in which the datum was recorded.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    moment = datum.timestamp.replace('_', ' ')
    moment += sec.zfill(2) # Add leading zero, if necessary.
    # Add the x coordinate of the (x,y) pair
    graph.x_values.append(moment)

    # for minute in hour:
    #     make string of min
    #     for five_second in range(0, 60, 5):
    #         make string of 5 second
    #         for antenna in range(0, 8):
    #             graph.y_values_per_antenna[antenna].\
    #             append(datum.antennas[antenna][graph_meta_data['attribute']]\
    #             [min][sec])

    return graph
