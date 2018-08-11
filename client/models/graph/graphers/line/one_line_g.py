# This file defines the one_line_g function.

import random
from .... search.search_imports import *
import string

def one_line_g(graph, title, attr):
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
            y = graph.lone_y_values,
            x = graph.x_values,
            name = f"YTLA {attr}",
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
        # filename=r"visualization.html",
        filename = fn,
        auto_open = True
    )
