"""
This file contains the definition of the Graph class, which holds data to be
graphed.
"""

from mongoengine import *

# class Graph(Document):
class Graph(EmbeddedDocument):
    # a list of empty lists, each empty list representing an antenna.
    # antennas 0-6, plus lucky_no_7 (for a total of 8)
    # y_values_per_antenna = [ [], [], [], [], [], [], [], [] ]
    y_values_per_antenna = ListField(default = [ [], [], [], [], [], [], [], [] ])
    # For antenna-agnostic data that will be represented by a single line chart
    lone_y_values = ListField(default = [])
    # For antenna-specific data that will be represented by a multi-bar
    # gantt chart, such as hybrid_selValY
    gantt_values_per_antenna = ListField(default = [ [], [], [], [], [], [], [], [] ])
    # For antenna-agnostic data that will be represented with a gantt chart
    attr_states = ListField(default = [])
    # For antenna-agnostic data that will be represneted with a gantt chart
    attr_state = StringField(default = 'placeholder')
    # For timestamps
    x_values = ListField(default = [])
    # Objects that will be given to plotly for plotting
    data_gettin_visualized = ListField(default = [])
    # A collection of attributes that will be identified by a color
    # color_labels = ['DATA']
    color_labels = ListField(default = [])
