# This file contains the definition of the one_gantt_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_gantt_c(data, graph_meta_data, x_val_quant):
    """
    This function processes data to be graphed as a single-bar gantt chart.

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

        # Check whether this is the front of the bar.
        if (graph.attr_state == 'placeholder'):
            graph.attr_states.append(
                dict(
                    Task = "YTLA",
                    Start = moment,
                    Finish = moment,
                    Resource = f"{datum[graph_meta_data['attribute']][min][sec]}"
                )
            )
            # Track the most recent attribute.
            graph.attr_state = datum[graph_meta_data['attribute']][min][sec]
            # Add a new label to receive a color, later.
            graph.color_labels.append(datum[graph_meta_data['attribute']][min][sec])
        # Check whether the attribute just changed.
        elif (datum[graph_meta_data['attribute']][min][sec] != graph.attr_state):
            graph.attr_state = datum[graph_meta_data['attribute']][min][sec]
            graph.attr_states[-1]['Finish'] = moment
            graph.attr_states.append(
                dict(
                    Task = "YTLA",
                    Start = moment,
                    Finish = moment,
                    Resource = f"{datum[graph_meta_data['attribute']][min][sec]}"
                )
            )
            # Add a new label to receive a color, later.
            if (datum[graph_meta_data['attribute']][min][sec] not in graph.color_labels):
                graph.color_labels.append(datum[graph_meta_data['attribute']][min][sec])
        # There is no change.  The attriubte remains active.
        else:
            # Update the Finish time of the previous attribute.
            graph.attr_states[-1]['Finish'] = moment

    return graph
