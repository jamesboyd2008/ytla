# This file contains the definition of the gantt_chart_per_antenna_composer function.

from datetime import datetime
import time

def gantt_chart_per_antenna_composer(datum, double_tuple):
    """
    This function processes data to be graphed as a multi-bar gantt chart.

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

    # if the list is empty, just append 8 dictionaries
    if (not double_tuple[0]['attr_states']):
        for antenna in range(0, 8):
            graph.attr_states.append(
                dict(
                    Task=f"Antenna {antenna}",
                    Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    Finish='placeholder',
                    Resource=f"{datum.antennas[antenna][attribute]}"
                )
            )
        # Add the first label to be assigned a color
        graph.color_labels.append(datum.antennas[-1][attribute])
    # if it's not the last element in the collection
    elif (graph_meta_data['data_count'] < graph_meta_data['data_quantity']):
        for antenna in range(0, 8):
            # if the color needs to change
            if (graph.attr_states[-1 - (7 - antenna)]['Resource'] != datum.antennas[antenna][graph_meta_data['attribute']]):
                # update the value of the 'Finish' key in the dict 8 elements prior
                graph.attr_states[-1 - (7 - antenna)]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                # add a new dict with the new value for the 'Resource' key
                graph.attr_states.append(
                    dict(
                        Task=f"Antenna {antenna}",
                        Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                        Finish='placeholder',
                        Resource=f"{datum.antennas[antenna][graph_meta_data['attribute']]}"
                    )
                )
                if (datum.antennas[antenna][graph_meta_data['attribute']] not in graph.color_labels):
                    graph.color_labels.append(datum.antennas[antenna][graph_meta_data['attribute']])
            else: # it's the same value as before
                graph.attr_states.append(
                    dict(
                        Task=f"Antenna {antenna}",
                        Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                        Finish='placeholder',
                        Resource=f"{datum.antennas[antenna][graph_meta_data['attribute']]}"
                    )
                )
    # TODO: it's the last element and a different value
    # TODO: it's the last element and a different value and no one has seen this value, yet
    else: # it's the last element in the data set
        graph.attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    return graph
