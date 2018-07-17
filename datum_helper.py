# This file contains the datum_helper(arg, arg, arg, ... ) function, which takes arg arg arg and opens an HTML document that displays a graph.

from search_imports import *

def datum_helper(datum, double_tuple):
    """
    Searches through all data attached to a specific timestamp, and returns a
    graph.

    Parameters:
        datum (Datum): all YTLA data from Datum and Antenna_Snapshot attached
                       to a specific timestamp

        double_tuple (tuple): the graph and associated metadata

    Returns:
        double_tuple - and instance of Graph and a tuple of metadata
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]

    # parse a string (datum.timestamp) as a datetime.datetime
    timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")
    # TODO: check the accuracy of these timestamps
    if (timestamp >= graph_meta_data['begin']) and (timestamp <= graph_meta_data['end']):
        if (graph_meta_data['attribute'] in gantt_chart_per_antenna):
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

        elif (graph_meta_data['attribute'] in lone_gantt_chart):
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
        elif (graph_meta_data['attribute'] in line_chart_per_antenna):
            for antenna in range(0, 8):
                graph.y_values_per_antenna[antenna].append(datum.antennas[antenna][graph_meta_data['attribute']])
        else: # (graph_meta_data['attribute'] in lone_line_chart):
            graph.lone_y_values.append(datum[graph_meta_data['attribute']])

        graph.x_values.append(datum.timestamp)

    graph_meta_data['data_count'] += 1 # TODO: this must be in the time range, not the DB

    double_tuple = (graph, graph_meta_data)

    return double_tuple
