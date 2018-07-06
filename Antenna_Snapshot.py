"""
This file defines the Antenna_Snapshot class, which is a container for all the
available telescope data associated with a single antenna at a single time.
"""

from mongoengine import *

class Antenna_Snapshot(EmbeddedDocument):
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    sel1X = IntField() # also in the logCorr_X file
    sel2X = IntField() # also in the logCorr_X file
    intswX = StringField() # also in the logCorr_X file
    hybrid_selX = StringField() # also in the logCorr_X file
    intLenX = FloatField() # also in the logCorr_X file
    sel1Y = IntField() # also in the logCorr_Y file
    sel2Y = IntField() # also in the logCorr_Y file
    intswY = StringField() # also in the logCorr_Y file
    hybrid_selY = StringField() # also in logCorr_Y
    intLenY = FloatField() # also in the logCorr_Y file
    iflo_x = FloatField()) # also in the logIFLO_X file
    iflo_y = FloatField()) # also in the logIFLO_Y file
