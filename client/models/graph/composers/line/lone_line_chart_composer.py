# This file contains the definition of the lone_line_chart_composer function.

def lone_line_chart_composer(datum, double_tuple):
    """
    This function processes data to be graphed as a single-line line chart.

    Parameters:
        datum (Datum) : Data associated with the same timestamp.
        double_tuple (tuple) : The graph (Graph) and its associated
                               metadata (dict).

    Returns:
        graph (Graph) : Data that will be graphed.
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]
    graph.lone_y_values.append(datum[graph_meta_data['attribute']])

    return graph
