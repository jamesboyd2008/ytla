"""
This file defines the Datum class, which is a container for all the available
telescope data associated with the same timestamp.
"""

from datetime import datetime
import time
from Antenna_Snapshot import Antenna_Snapshot
from mongoengine import *

class Datum(Document):
    # Fields are picked from here:
    # http://docs.mongoengine.org/apireference.html#fields
    # datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    timestamp = StringField() # from local machine
    nt_state = StringField() # also in logSys
    nt_select = StringField() # also in logSys
    lo_freq = FloatField(default=0.0) # also in logSys
    lo_power = FloatField(default=0.0) # also in logSys
    # 0-6 Antenna_Snapshot objects plus lucky number 7
    antennas = ListField(EmbeddedDocumentField(Antenna_Snapshot))
    
