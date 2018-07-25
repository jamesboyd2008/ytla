# This file defines the plotter function, which, given chart data, plots a
# chart on an HTML document and opens that document in the default web browser.

from search_imports import *
from line_chart_per_antenna_grapher import line_chart_per_antenna_grapher
from lone_line_chart_grapher import lone_line_chart_grapher
from gantt_chart_per_antenna_grapher import gantt_chart_per_antenna_grapher
from lone_gantt_chart_grapher import lone_gantt_chart_grapher

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
        beginning = graph_meta_data['begin'].strftime('%Y-%m-%d %H:%M:%S')
        ending = graph_meta_data['end'].strftime('%Y-%m-%d %H:%M:%S')
        title = f"{graph_meta_data['attribute']} from {beginning} to {ending}"

        if (graph_meta_data['attribute'] in line_chart_per_antenna): # does this need to be inside the loop?
            line_chart_per_antenna_grapher(graph, title, graph_meta_data['attribute'])
        elif (graph_meta_data['attribute'] in lone_line_chart):
            lone_line_chart_grapher(graph, title, graph_meta_data['attribute'])
        elif (graph_meta_data['attribute'] in gantt_chart_per_antenna):
            gantt_chart_per_antenna_grapher(graph, title)
        else: # it's a lone_gantt_chart
            lone_gantt_chart_grapher(graph, title)

        plottable = True

    return plottable
