#!/usr/bin/python2.7

from datetime import datetime

# Python/MongoDB interface that supports python objects as DB records
from mongoengine import *
# class for all same-timestamp data
from client.models.datum.Datum import Datum
# class for all same-antenna data
from client.models.antennas.Antenna_Snapshot import Antenna_Snapshot

import time

# Connect to the MongoDB database (DB)
# It is assumed that mongod is running on 'localhost' at port 27017
# https://docs.mongodb.com/manual/tutorial/manage-mongodb-processes/#start-mongod-processes
connect('ytla')

while (1):
# intantiate a Datum object to hold all data associated with the same timestamp
# such as antenna data
        datum = Datum()

        # a collection for Antenna_Snapshot objects
        antennas = []
        # 7 antennas exist
        # an 8th antenna is added for consistency
        for antenna in range(0, 8):
            # initialize an Antenna_Snapshot object to contain all data specific to
            # a single antenna at a single moment.
            antennas.append(Antenna_Snapshot())

        # Add the antennas to the record
        datum.antennas = antennas

        timenow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

        # note when the data was collected
        datum.timestamp = timenow

        datum.nt_state = "NTState"
        datum.nt_select = "NTSelect"
        datum.lo_freq = 7
        datum.lo_power = 10

        print(datum.timestamp)
        time.sleep(0.1)
