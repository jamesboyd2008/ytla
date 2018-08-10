# This file contains the definition of the one_gantt_helper function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_gantt_helper(datum, graph, graph_meta_data, hr, min, end_hr, end_min):
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
        # Iterate over all minutes within the hour, starting at first recorded.
        for m in range(min, end_min + 1):
            hr_str = str(h)
            min_str = str(m)
            padded_hr_str = hr_str.zfill(2)
            padded_min_str = min_str.zfill(2)
            # replace hours and minutes in moment.
            moment = moment[0:11]
            moment += padded_hr_str + ':' + padded_min_str
            # Add the x coordinate of the (x,y) pair
            graph.x_values.append(moment)

            # Check whether this is the front of the bar.
            if (graph.attr_state == 'placeholder'):
                graph.attr_states.append(
                    dict(
                        Task = "YTLA",
                        Start = moment,
                        Finish = moment,
                        Resource = f"{datum[graph_meta_data['attribute']][hr_str][min_str]}"
                    )
                )
                # Track the most recent attribute.
                graph.attr_state = datum[graph_meta_data['attribute']][hr_str][min_str]
                # Add a new label to receive a color, later.
                graph.color_labels.append(datum[graph_meta_data['attribute']][hr_str][min_str])
            # Check whether the attribute just changed.
            elif (datum[graph_meta_data['attribute']][hr_str][min_str] != graph.attr_state):
                graph.attr_state = datum[graph_meta_data['attribute']][hr_str][min_str]
                graph.attr_states[-1]['Finish'] = moment
                graph.attr_states.append(
                    dict(
                        Task = "YTLA",
                        Start = moment,
                        Finish = moment,
                        Resource = f"{datum[graph_meta_data['attribute']][hr_str][min_str]}"
                    )
                )
                # Add a new label to receive a color, later.
                if (datum[graph_meta_data['attribute']][hr_str][min_str] not in graph.color_labels):
                    graph.color_labels.append(datum[graph_meta_data['attribute']][hr_str][min_str])
            # There is no change.  The attriubte remains active.
            else:
                # Update the Finish time of the previous attribute.
                graph.attr_states[-1]['Finish'] = moment

        min = 0

    return graph
