# This file contains the definition of the datum_helper function.

import datetime
from .. graph.composers.gantt.ant_gantt_c import ant_gantt_c
from .. graph.composers.gantt.one_gantt_c import one_gantt_c
from .. graph.composers.line.ant_line_c import ant_line_c
from .. graph.composers.line.one_line_c import one_line_c
from .. search.search_imports import *

def datum_helper(data, graph_meta_data):
    """
    Searches through all data attached to a specific timestamp, and returns a
    graph.

    Parameters:
        data (mongoengine.QuerySet) : DB records returned from a query

        graph_meta_data (dict) : user-provided information about the graph

    Returns:
        graph (Graph) : data that whill be graphed
    """

    # The object that will get graphed
    graph = Graph()

    end = datetime.strptime( graph_meta_data['end'], "%Y-%m-%d_%H:%M")
    begin = datetime.strptime( graph_meta_data['begin'], "%Y-%m-%d_%H:%M")
    x_val_quant = int(( end - begin ).total_seconds() / 60)

    # print(f"quantity of days --> {len(data)}")
    # Choose appropriate visualization
    if (graph_meta_data['attribute'] in gantt_chart_per_antenna):
        graph = ant_gantt_c(data, graph_meta_data, x_val_quant)
    elif (graph_meta_data['attribute'] in lone_gantt_chart):
        graph = one_gantt_c(data, graph_meta_data, x_val_quant)
    elif (graph_meta_data['attribute'] in line_chart_per_antenna):
        graph = ant_line_c(data, graph_meta_data, x_val_quant)
    else: # (graph_meta_data['attribute'] in lone_line_chart):
        graph = one_line_c(data, graph_meta_data, x_val_quant)
    return graph
