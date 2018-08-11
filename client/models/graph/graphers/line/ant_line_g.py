# This file defines the line_chart_per_antenna function.

import random
from .... search.search_imports import *
import string

def ant_line_g(graph, title, attr):
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
                y = graph.y_values_per_antenna[antenna],
                x = graph.x_values,
                name = f"Antenna {antenna} {attr}",
                mode = 'lines+markers'
            )
        )

    # Generate a pseudorandom filename.
    fn = ''.join(random.choices(string.ascii_letters,k=7)) + '.html'

    plotly.offline.plot(
        {
            'data': graph.data_gettin_visualized,
            'layout': Layout(title = title)
        },
        filename = fn,
        auto_open = True
    )
