# This file contains the definition of the lone_gantt_chart_composer function.

from datetime import datetime
import time

def lone_gantt_chart_composer(datum, double_tuple):
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

    # parse a string (datum.timestamp) as a datetime.datetime
    timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")

    if (graph.attr_state == 'placeholder'):
        graph.attr_states.append(
            dict(
                Task="YTLA",
                Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                Finish='placeholder',
                Resource=f"{datum[graph_meta_data['attribute']]}"
            )
        )
        graph.attr_state = datum[graph_meta_data['attribute']]
        graph.color_labels.append(datum[graph_meta_data['attribute']])
    elif (datum[graph_meta_data['attribute']] != graph.attr_state):
        graph.attr_state = datum[graph_meta_data['attribute']]
        graph.attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        graph.attr_states.append(
            dict(
                Task="YTLA",
                Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                Finish='placeholder',
                Resource=f"{datum[graph_meta_data['attribute']]}"
            )
        )
        if (datum[graph_meta_data['attribute']] not in graph.color_labels):
            graph.color_labels.append(datum[graph_meta_data['attribute']])
    elif (graph_meta_data['data_count'] == graph_meta_data['data_quantity']):
        graph.attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    # TODO: last element, new color
    # TODO: last element, new color, new attribute

    return graph
