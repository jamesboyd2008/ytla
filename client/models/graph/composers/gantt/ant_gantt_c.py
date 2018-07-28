# This file contains the definition of the ant_gantt_c function.

from ... Graph import Graph
from .... datum.Datum import Datum

def ant_gantt_c(data, graph_meta_data):
    """
    This function processes data to be graphed as a multi-bar gantt chart.

    Parameters:
        data (List) : List of Datum objs associated with the same timestamp.
        graph_meta_data (dict) : The querry attribute, begin and end times.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = Graph()

    for datum in data:
        # Add the x coordinate of the (x,y) pair
        graph.x_values.append(datum.timestamp.replace('_', ' '))
        # replace underscore for plotly processing
        moment = datum.timestamp.replace('_', ' ')

        # Check whether the lists with the list are empty.
        #     i.e. ---> [ [], [], [], [], [], [], [], [] ]
        # This is grounds for assuming that datum is the first element in the DB
        # found to be within the time range, for this query.
        if (not graph.gantt_values_per_antenna[0]):
            # Append a dict to every list in gantt_values_per_antenna
            for antenna in range(0, 8):
                graph.gantt_values_per_antenna[antenna].append(
                    dict(
                        Task = f"Antenna {antenna}",
                        Start = moment,
                        Finish = moment,
                        Resource = f"{datum.antennas[antenna][graph_meta_data['attribute']]}"
                    )
                )
                # Add the color to the list of colors if it's not there, yet
                if (datum.antennas[antenna][graph_meta_data['attribute']] not in graph.color_labels):
                    graph.color_labels.append(datum.antennas[antenna][graph_meta_data['attribute']])
        # This isn't the first datum found within the time range.
        else:
            # for each of the 8 antennas
            for antenna in range(0, 8):
                # Update the Finish time of the Tasks
                graph.gantt_values_per_antenna[antenna][-1]['Finish'] = moment
                # if the color needs to change
                if (graph.gantt_values_per_antenna[antenna][-1]['Resource'] != datum.antennas[antenna][graph_meta_data['attribute']]):
                    # add a new dict with the new value for the 'Resource' key
                    graph.gantt_values_per_antenna[antenna].append(
                        dict(
                            Task = f"Antenna {antenna}",
                            Start = moment,
                            Finish = moment,
                            Resource = f"{datum.antennas[antenna][graph_meta_data['attribute']]}"
                        )
                    )
                    # Add the color to the list of colors if it's not there, yet
                    if (datum.antennas[antenna][graph_meta_data['attribute']] not in graph.color_labels):
                        graph.color_labels.append(datum.antennas[antenna][graph_meta_data['attribute']])

    return graph
