# This file defines the lone_line_chart_grapher function.

from search_imports import *

def lone_line_chart_grapher(graph, title, attr):
    """
    This function plots a line chart.

    Parameters:
        graph (Graph) : The data to be graphed.
        title (str) : The title of the graph.
        attr (str) : The attribute that will be graphed.

    Returns:
        NoneType
    """
    
    graph.data_gettin_visualized.append(
        Scatter(
            y=graph.lone_y_values,
            x=graph.x_values,
            name=f"YTLA {attr}",
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
