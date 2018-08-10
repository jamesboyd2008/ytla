# This file contains the definition of the ant_gantt_helper function.

from datetime import datetime
from .... datum.Datum import Datum
from ... Graph import Graph

def ant_gantt_helper(datum, graph, graph_meta_data, hr, min, end_hr, end_min):
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
            # Check whether the lists with the list are empty.
            #     i.e. ---> [ [], [], [], [], [], [], [], [] ]
            # This is grounds for assuming that datum is the first element in the DB
            # found to be within the time range, for this query.
            if (not graph.gantt_values_per_antenna[0]):
                # Append a dict to every list in gantt_values_per_antenna
                for antenna in range(0, 8):
                    # Define a variable pointing to the label of the gantt value
                    label = datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str]
                    graph.gantt_values_per_antenna[antenna].append(
                        dict(
                            Task = f"Antenna {antenna}",
                            Start = moment,
                            Finish = moment,
                            Resource = label
                        )
                    )
                    # Add the color to the list of colors if it's not there, yet
                    if (label not in graph.color_labels):
                        graph.color_labels.append(label)
            # This isn't the first datum found within the time range.
            else:
                # for each of the 8 antennas
                for antenna in range(0, 8):
                    # Update the Finish time of the Tasks
                    graph.gantt_values_per_antenna[antenna][-1]['Finish'] = moment
                    # Define a variable pointing to the label of the gantt value
                    label = datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str]
                    # if the color needs to change
                    if (graph.gantt_values_per_antenna[antenna][-1]['Resource'] != label):
                        # add a new dict with the new value for the 'Resource' key
                        graph.gantt_values_per_antenna[antenna].append(
                            dict(
                                Task = f"Antenna {antenna}",
                                Start = moment,
                                Finish = moment,
                                Resource = label
                            )
                        )
                        # Add the color to the list of colors if it's not there, yet
                        if (label not in graph.color_labels):
                            graph.color_labels.append(label)

        min = 0

    return graph
