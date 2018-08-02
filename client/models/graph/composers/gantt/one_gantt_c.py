# This file contains the definition of the one_gantt_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def one_gantt_c(data, graph_meta_data, count, handicap = None):
    """
    This function processes data to be graphed as a single-bar gantt chart.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        count (int) : The quantity of elements in data.
        handicap (int) : records with indicies divisible by this number will be
                         included in the graph. Others will not be included.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = Graph()

    for index in range(0, count, handicap):
        # Add the x coordinate of the (x,y) pair
        graph.x_values.append(data[index].timestamp.replace('_', ' '))
        # replace underscore for plotly processing
        moment = data[index].timestamp.replace('_', ' ')

        # Check whether this is the front of the bar.
        if (graph.attr_state == 'placeholder'):
            graph.attr_states.append(
                dict(
                    Task = "YTLA",
                    Start = moment,
                    Finish = moment,
                    Resource = f"{data[index][graph_meta_data['attribute']]}"
                )
            )
            # Track the most recent attribute.
            graph.attr_state = data[index][graph_meta_data['attribute']]
            # Add a new label to receive a color, later.
            graph.color_labels.append(data[index][graph_meta_data['attribute']])
        # Check whether the attribute just changed.
        elif (data[index][graph_meta_data['attribute']] != graph.attr_state):
            graph.attr_state = data[index][graph_meta_data['attribute']]
            graph.attr_states[-1]['Finish'] = moment
            graph.attr_states.append(
                dict(
                    Task = "YTLA",
                    Start = moment,
                    Finish = moment,
                    Resource = f"{data[index][graph_meta_data['attribute']]}"
                )
            )
            # Add a new label to receive a color, later.
            if (data[index][graph_meta_data['attribute']] not in graph.color_labels):
                graph.color_labels.append(data[index][graph_meta_data['attribute']])
        # There is no change.  The attriubte remains active.
        else:
            # Update the Finish time of the previous attribute.
            graph.attr_states[-1]['Finish'] = moment

    return graph
