# This file defines the plotter function, which, given chart data, plots a
# chart on an HTML document and opens that document in the default web browser.

from ... search.search_imports import *
from . line.ant_line_g import ant_line_g
from . line.one_line_g import one_line_g
from . gantt.ant_gantt_g import ant_gantt_g
from . gantt.one_gantt_g import one_gantt_g

def plotter(double_tuple):
    """
    This function plots charts.

    Parameters:
        double_tuple (tuple) : The graph and its associated metadata.

    Returns:
        plottable (bool) : Whether there are any x coordinates to plot.
    """

    graph = double_tuple[0]
    graph_meta_data = double_tuple[1]

    if len(graph.x_values) == 0:
        plottable = False
    else:
        beginning = graph_meta_data['begin'].replace('_', ' ')
        ending = graph_meta_data['end'].replace('_', ' ')
        title = f"{graph_meta_data['attribute']} from {beginning} to {ending}"

        if (graph_meta_data['attribute'] in line_chart_per_antenna): # does this need to be inside the loop?
            ant_line_g(graph, title, graph_meta_data['attribute'])
        elif (graph_meta_data['attribute'] in lone_line_chart):
            one_line_g(graph, title, graph_meta_data['attribute'])
        elif (graph_meta_data['attribute'] in gantt_chart_per_antenna):
            ant_gantt_g(graph, title)
        else: # it's a lone_gantt_chart
            one_gantt_g(graph, title)

        plottable = True

    return plottable
