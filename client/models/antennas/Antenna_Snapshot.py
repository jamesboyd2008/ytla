# This file defines the Antenna_Snapshot class, which is a container for all the
# available telescope data associated with a single antenna at a single time.

from ... helpers.make_an_hour import make_an_hour
from mongoengine import *

class Antenna_Snapshot(EmbeddedDocument):
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    sel1X = DictField(default=make_an_hour(0.0)) # also in the logCorr_X file
    sel2X = DictField(default=make_an_hour(0.0)) # also in the logCorr_X file
    intswX = DictField(default=make_an_hour(0.0)) # also in the logCorr_X file
    hybrid_selValX = DictField(default=make_an_hour(0.0)) # also in the logCorr_X file
    intLenX = DictField(default=make_an_hour(0.0)) # also in the logCorr_X file
    sel1Y = DictField(default=make_an_hour(0.0)) # also in the logCorr_Y file
    sel2Y = DictField(default=make_an_hour(0.0)) # also in the logCorr_Y file
    intswY = DictField(default=make_an_hour(0.0)) # also in the logCorr_Y file
    hybrid_selValY = DictField(default=make_an_hour(0.0)) # also in logCorr_Y
    intLenY = DictField(default=make_an_hour(0.0)) # also in the logCorr_Y file
    iflo_x = DictField(default=make_an_hour(0.0)) # also in the logIFLO_X file
    iflo_y = DictField(default=make_an_hour(0.0)) # also in the logIFLO_Y file
    lfI_X = DictField(default=make_an_hour(0.0)) # also in the logLF_X file
    lfQ_X = DictField(default=make_an_hour(0.0)) # also in the logLF_X file
    lfI_Y = DictField(default=make_an_hour(0.0)) # also in the logLF_Y file
    lfQ_Y = DictField(default=make_an_hour(0.0)) # also in the logLF_Y file
