"""
This file contains the definition of the Graph class, which holds data to be
graphed.
"""

class Graph:
    # objection initialization method
    def __init__(self):
        # a list of empty lists, each empty list representing an antenna.
        # antennas 0-6, plus lucky_no_7 (for a total of 8)
        self.y_values_per_antenna = [ [], [], [], [], [], [], [], [] ]
        # For antenna-agnostic data that will be represented by a single line chart
        self.lone_y_values = []
        # For antenna-specific data that will be represented by a multi-bar
        # gantt chart, such as hybrid_selY
        self.gantt_values_per_antenna = [ [], [], [], [], [], [], [], [] ]
        # For antenna-agnostic data that will be represented with a gantt chart
        self.attr_states = []
        # For antenna-agnostic data that will be represneted with a gantt chart
        self.attr_state = 'placeholder'
        # For timestamps
        self.x_values = []
        # Objects that will be given to plotly for plotting
        self.data_gettin_visualized = []
        # A collection of attributes that will be identified by a color
        # color_labels = ['DATA']
        self.color_labels = []
