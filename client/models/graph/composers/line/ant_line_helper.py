# This file contains the definition of the ant_line_helper function.

from ... Graph import Graph
from .... datum.Datum import Datum

def ant_line_helper(datum, graph, graph_meta_data, hr, min, end_hr, end_min):
    """
    This function processes one day of one attribute's data.

    60 data_points/hr * 24 hr/day= 1440 data_points/day

    Parameters:
        datum (Datum) : One hour of YTLA diagnostic information ~ 1 - 3 MB
        graph (Graph) : The object to be visualized.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        hr (int) : The hour in which to begin graphing.
        min (int) : The minute in which to begin graphing.
        end_hr (int) : The hour in which to end graphing.
        end_min (int) : The minute in which to end graphing.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    moment = datum.timestamp.replace('_', ' ')

    # Iterate over all hours, beginning with the first recoded hour of the day.
    for h in range(hr, end_hr + 1):
        # Determine whether it's the final hour.
        if h == end_hr: # it's the last hour in range
            end = end_min + 1
        else:
            end = 60
        # Iterate over all minutes within the hour, starting at first recorded.
        for m in range(min, end):
            hr_str = str(h)
            min_str = str(m)
            padded_hr_str = hr_str.zfill(2)
            padded_min_str = min_str.zfill(2)
            # replace hours and minutes in moment.
            moment = moment[0:11]
            moment += padded_hr_str + ':' + padded_min_str
            # Add the x coordinate of the (x,y) pair
            graph.x_values.append(moment)
            for antenna in range(0, 8):
                # Add the y coordinate of the (x,y) pair
                graph.y_values_per_antenna[antenna].\
                append(datum.antennas[antenna][graph_meta_data['attribute']]\
                [hr_str][min_str])

        min = 0

    return graph
