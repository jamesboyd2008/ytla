"""
This file contains loops that sort YTLA data into their appropriate
visualization collections, such as lists of values for line charts and
gantt charts.
"""

from attributes import *

# A list of they keys in the attriubtes dictionary
attribute_names = list(attributes.keys())

# A container for antenna-specific data that may visualize well as line charts
line_chart_per_antenna = []
# These indices match data in attributes that may look good as a line chart
for i in [ 0, 1, 4, 5, 6, 9, 15, 16, 17, 18, 19, 20 ]:
    line_chart_per_antenna.append(attributes[attribute_names[i]])

# A container for antenna-agnostic data that may visualize well as line charts
lone_line_chart = []
# These indices match data in attributes that may look good as a line chart
for i in [ 13, 14 ]:
    lone_line_chart.append(attributes[attribute_names[i]])

# A container for antenna-specific data that may visualize well as gantt charts
gantt_chart_per_antenna = []
# These indices match data in attributes that may look good as a gantt chart
for i in [ 2, 3, 7, 8 ]:
    gantt_chart_per_antenna.append(attributes[attribute_names[i]])

# A container for antenna-agnostic data that may visualize well as gantt charts
lone_gantt_chart = []
# These indices match data in attributes that may look good as a gantt chart
for i in [ 11, 12 ]:
    lone_gantt_chart.append(attributes[attribute_names[i]])
