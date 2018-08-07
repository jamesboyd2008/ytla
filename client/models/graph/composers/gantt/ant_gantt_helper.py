# This file contains the definition of the ant_gantt_helper function.

from ... Graph import Graph
from .... datum.Datum import Datum

def ant_gantt_helper(datum, graph, graph_meta_data, hr, min):
    """
    This function processes one day of one attribute's data.

    60 data_points/hr * 24 hr/day= 1440 data_points/day

    Parameters:
        datum (Datum) : One hour of YTLA diagnostic information ~ 1 - 3 MB
        graph (Graph) : The object to be visualized.
        graph_meta_data (dict) : The querry attribute, begin and end times.
        hr (int) : The hour in which the datum was recorded.
        min (int) : The minute in which the datum was recorded.

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    moment = datum.timestamp.replace('_', ' ')

    for h in range(hr, 24):
        for m in range(min, 60):
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
                    graph.gantt_values_per_antenna[antenna].append(
                        dict(
                            Task = f"Antenna {antenna}",
                            Start = moment,
                            Finish = moment,
                            Resource = f"{datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str]}"
                        )
                    )
                    # Add the color to the list of colors if it's not there, yet
                    if (datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str] not in graph.color_labels):
                        graph.color_labels.append(datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str])
            # This isn't the first datum found within the time range.
            else:
                # for each of the 8 antennas
                for antenna in range(0, 8):
                    # Update the Finish time of the Tasks
                    graph.gantt_values_per_antenna[antenna][-1]['Finish'] = moment
                    # if the color needs to change
                    if (graph.gantt_values_per_antenna[antenna][-1]['Resource'] != datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str]):
                        # add a new dict with the new value for the 'Resource' key
                        graph.gantt_values_per_antenna[antenna].append(
                            dict(
                                Task = f"Antenna {antenna}",
                                Start = moment,
                                Finish = moment,
                                Resource = f"{datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str]}"
                            )
                        )
                        # Add the color to the list of colors if it's not there, yet
                        if (datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str] not in graph.color_labels):
                            graph.color_labels.append(datum.antennas[antenna][graph_meta_data['attribute']][hr_str][min_str])

        min = 0

    return graph
