# This file contains the class definition of Aggregation.

# from datetime import datetime
# import time
# from .. antennas.Antenna_Snapshot import Antenna_Snapshot
# from ... helpers.make_a_day import make_a_day
from .. graph.Graph import Graph
from mongoengine import *

class Aggregation(Document):
    """
    Represents a day's worth of 1 out of ~ 122 telescope metadata.
    """
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    timestamp = StringField() # "%Y-%m-%d_%H:%M"
    attr = StringField()
    graph = EmbeddedDocumentField(Graph)
