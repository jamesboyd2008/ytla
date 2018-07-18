# This file defines the Antenna_Snapshot class, which is a container for all the
# available telescope data associated with a single antenna at a single time.

from mongoengine import *

class Antenna_Snapshot(EmbeddedDocument):
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    sel1X = IntField(default=0) # also in the logCorr_X file
    sel2X = IntField(default=0) # also in the logCorr_X file
    intswX = StringField(default="dummy data") # also in the logCorr_X file
    hybrid_selX = StringField(default="dummy data") # also in the logCorr_X file
    intLenX = FloatField(default=0.0) # also in the logCorr_X file
    sel1Y = IntField(default=0) # also in the logCorr_Y file
    sel2Y = IntField(default=0) # also in the logCorr_Y file
    intswY = StringField(default="dummy data") # also in the logCorr_Y file
    hybrid_selY = StringField(default="dummy data") # also in logCorr_Y
    intLenY = FloatField(default=0.0) # also in the logCorr_Y file
    iflo_x = FloatField(default=0.0) # also in the logIFLO_X file
    iflo_y = FloatField(default=0.0) # also in the logIFLO_Y file
    lfI_X = FloatField(default=0.0) # also in the logLF_X file
    lfQ_X = FloatField(default=0.0) # also in the logLF_X file
    lfI_Y = FloatField(default=0.0) # also in the logLF_Y file
    lfQ_Y = FloatField(default=0.0) # also in the logLF_Y file
