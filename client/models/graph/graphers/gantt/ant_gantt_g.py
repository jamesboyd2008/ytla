# This file defines ant_gantt_g function.

from .... search.search_imports import *

def ant_gantt_g(graph, title):
    """
    This function graphs a multi-bar gantt chart.

    Parameters:
        graph (Graph) : Data that will be graphed.
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

    # Make dummy data bars grey.
    colors['dummy data'] = 'rgb(128, 128, 128)' # gray

    # Process the 2D array of gantt_values_per_antenna for graphing
    for antenna in graph.gantt_values_per_antenna:
        for entry in antenna:
            graph.data_gettin_visualized.append(entry)

    # Use plotly's figure factory, ff, to almost display a gantt chart
    figure = ff.create_gantt(
        graph.data_gettin_visualized,
        colors = colors,
        group_tasks = True,
        index_col = 'Resource',
        show_colorbar = True,
        title = title
    )
    # Display the gantt chart
    plotly.offline.plot(
        figure,
        filename = r"visualization.html",
        auto_open = True
    )

    # TODO: zero plotly data corner case
