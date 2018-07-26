# This file contains the definition of the ant_line_c function.

def ant_line_c(datum, double_tuple):
    """
    This function processes data to be graphed as a multi-line plot.

    Parameters:
        datum (Datum) : Data associated with the same timestamp.
        double_tuple (tuple) : The graph (Graph) and its associated
                               metadata (dict).

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]

    for antenna in range(0, 8):
        graph.y_values_per_antenna[antenna].\
        append(datum.antennas[antenna][graph_meta_data['attribute']])

    return graph
