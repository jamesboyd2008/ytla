# This file defines the line_chart_per_antenna function.

from search_imports import *

def line_chart_per_antenna_grapher(graph, title, attr):
    """
    This function graphs multiple line plots.

    Parameters:
        graph (Graph) : Data that will be graphed.
        title (str) : The title of the graph.
        attr (str) : The attribute being graphed.

    Returns:
        NoneType
    """

    for antenna in range(0, 8):
        graph.data_gettin_visualized.append(
            Scatter(
                y=graph.y_values_per_antenna[antenna],
                x=graph.x_values,
                name=f"Antenna {antenna} {attr}",
                mode='lines+markers'
            )
        )
    plotly.offline.plot(
        {
            'data': graph.data_gettin_visualized,
            'layout': Layout(title = title)
        },
        filename=r"visualization.html",
        auto_open=True
    )
