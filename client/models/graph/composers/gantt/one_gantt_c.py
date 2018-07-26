# This file contains the definition of the one_gantt_c function.

from datetime import datetime
import time

def one_gantt_c(datum, double_tuple):
    """
    This function processes data to be graphed as a single-bar gantt chart.

    Parameters:
        datum (Datum) : Data associated with the same timestamp.
        double_tuple (tuple) : The graph (Graph) and its associated
                               metadata (dict).

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]

    # replace underscore for plotly processing
    moment = datum.timestamp.replace('_', ' ')

    # Check whether this is the front of the bar.
    if (graph.attr_state == 'placeholder'):
        graph.attr_states.append(
            dict(
                Task = "YTLA",
                Start = moment,
                Finish = moment,
                Resource = f"{datum[graph_meta_data['attribute']]}"
            )
        )
        # Track the most recent attribute.
        graph.attr_state = datum[graph_meta_data['attribute']]
        # Add a new label to receive a color, later.
        graph.color_labels.append(datum[graph_meta_data['attribute']])
    # Check whether the attribute just changed.
    elif (datum[graph_meta_data['attribute']] != graph.attr_state):
        graph.attr_state = datum[graph_meta_data['attribute']]
        graph.attr_states[-1]['Finish'] = moment
        graph.attr_states.append(
            dict(
                Task = "YTLA",
                Start = moment,
                Finish = moment,
                Resource = f"{datum[graph_meta_data['attribute']]}"
            )
        )
        # Add a new label to receive a color, later.
        if (datum[graph_meta_data['attribute']] not in graph.color_labels):
            graph.color_labels.append(datum[graph_meta_data['attribute']])
    # There is no change.  The attriubte remains active.
    else:
        # Update the Finish time of the previous attribute.
        graph.attr_states[-1]['Finish'] = moment

    return graph
