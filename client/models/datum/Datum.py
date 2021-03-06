# This file defines the Datum class, which is a container for all the available
# telescope data associated with the same timestamp.

from datetime import datetime
import time
from .. antennas.Antenna_Snapshot import Antenna_Snapshot
from ... helpers.make_a_day import make_a_day
from mongoengine import *

class Datum(Document):
    """
    Returns an object with the specified default values for properties.
    """
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    # datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    timestamp = StringField(default = "0000-00-00_00:00")
    nt_state = DictField(default = make_a_day("dummy data")) # also in logSys
    nt_select = DictField(default = make_a_day("dummy data")) # also in logSys
    lo_freq = DictField(default = make_a_day(0.0)) # also in logSys
    lo_power = DictField(default = make_a_day(0.0)) # also in logSys
    # 0-6 Antenna_Snapshot objects plus lucky number 7
    antennas = ListField(EmbeddedDocumentField(Antenna_Snapshot))
