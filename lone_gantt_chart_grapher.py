# This file defines the

from search_imports import *

def lone_gantt_chart_grapher(graph, title):
    print(f"graph: {graph}")
    print(f"title: {title}")
    colors = {}
    color_count = 0
    for color in graph.color_labels:
        colors[color] = rgb_colors[color_count]
        color_count += 1

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
# finally:
    # TODO: zero plotly data corner case
    # try to delete the old graph, somehow
# finally:
    # del graph
# print(f"len(graph.y_values_per_antenna[0]): { len( graph.y_values_per_antenna[0] ) }")
