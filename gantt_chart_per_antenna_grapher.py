# This file defines gantt_chart_per_antenna_grapher function.

from search_imports import *

def gantt_chart_per_antenna_grapher(graph, title):
    """
    This function graphs a multi-bar gantt chart.

    Parameters:
        graph (Graph) : Data that will be graphed.
        title (str) : The title of the graph.

    Returns:
        NoneType
    """
    
    colors = {}
    color_count = 0
    for color in graph.color_labels:
        colors[color] = rgb_colors[color_count]
        color_count += 1

    # TODO: where is the iteration?

    # TODO: determine whether the strange alternating of antenna to antenna is significant in the displaying of the gantt chart.  Perhaps you must not skip around. You could test this with the data in test_driver.py
    graph.data_gettin_visualized = ff.create_gantt(
        graph.attr_states,
        colors=colors,
        index_col='Resource',
        show_colorbar=True,
        group_tasks=True
    )

    plotly.offline.plot(
        graph.data_gettin_visualized,
        filename=r"visualization.html",
        auto_open=True
    )
