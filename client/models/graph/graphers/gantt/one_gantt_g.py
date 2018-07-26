# This file defines the one_gantt_g function.

from .... search.search_imports import *

def one_gantt_g(graph, title):
    """
    This function generates and opens an HTML document containing a graph.

    Parameters:
        graph (Graph) : The data to be graphed.
        title (str) : The title of the graph.

    Returns:
        NoneType
    """

    # A dict to map labels to their corresponding colors
    colors = {}
    # A counter variable for list element reference by index
    color_count = 0
    # Iterate over all the labels, assigning each a color
    for label in graph.color_labels:
        colors[label] = rgb_colors[color_count]
        color_count += 1

    # Use plotly's figure factory, ff, to almost display a gantt chart
    graph.data_gettin_visualized = ff.create_gantt(
        graph.attr_states,
        colors = colors,
        group_tasks = True,
        index_col = 'Resource',
        show_colorbar = True,
        title = title
    )

    # Display the gantt chart
    plotly.offline.plot(
        graph.data_gettin_visualized,
        filename = r"visualization.html",
        auto_open = True
    )

    # TODO: zero plotly data corner case
