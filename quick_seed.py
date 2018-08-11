#!/usr/bin/python3.6

# This program seeds a database (DB) with dummy data.

from client.models.datum.Datum import Datum
from client.models.antennas.Antenna_Snapshot import Antenna_Snapshot
import datetime
from mongoengine import *
import random
import time

def main():

    connect('ytla')

    # Ensure that the seconds of all timestamps are divisible by 5,
    # because the maximum granularity of the time series in the DB is 5 seconds.
    # not_yet = True
    # while not_yet:
    #     timey = datetime.datetime.now()
    #     if timey.second % 5 == 0:
    #         not_yet = False
    #     else:
    #         time.sleep(1)
    # timenow = timey.strftime('%Y-%m-%d_%H:%M:%S')
    # incrementor = datetime.timedelta(seconds = 5)
    start = time.perf_counter()

    timenow = '2018-08-02_12:00:00'
    incrementor = datetime.timedelta(seconds = 60)
    datum = Datum()
    # this_hour = Datum.objects(timestamp = timenow[0:16]) # make this not happen during seed

    # for i in range(17281):
    # for i in range(120960): # one week
    # for i in range(): # one hour
    # for i in range(24): # two minutes
    # for i in range(17280): #  12 writes/min * 60 min/hour * 24 hour/day = 1 day
    for i in range(2880): # 60 writes/hr * 24 hr/day * 2 days = 2880 writes
        # Confirm whether a document has already been started for this_hour.
        # this_hour = Datum.objects(timestamp = timenow[0:16]) # make this not happen during seed
        # if i % 720 == 0: # it's a new hour
        if i % 1440 == 0: # it's a new hour
            # create a new document
            datum = Datum()
            # Give the new Datum object some antennas.
            antennas = []
            # 7 antennas exist
            # no. 8 is initialized with the default value of 0 for every attribute
            for antenna in range(0, 8):
                # initialize an Antenna_Snapshot object to contain all data specific to
                # a single antenna at a single moment.
                datum.antennas.append(Antenna_Snapshot())
            hour, minute = '0', '0'
            datum.timestamp = timenow[0:16]
        else: # same hour as before
            # print("|"),
            # update the document
            # datum = this_hour[0]
            # now = datetime.datetime.now()
            now = datetime.datetime.strptime(timenow, '%Y-%m-%d_%H:%M:%S')
            hour = str(now.hour)
            minute = str(now.minute)
        # print(f"hour: {hour}")
        # print(f"minute: {minute}")
        # print(f"second: {second}")
        # if (i > 40000) and (i < 80000):
        # print(f"type(datum): {type(datum)}")
        # print(f"type(datum.nt_state): {type(datum.nt_state)}")
        if (i > 1000) and (i < 2000):
            datum.nt_state[hour][minute] = "wreck 'em"
        else:
            datum.nt_state[hour][minute] = "rack 'em"

        lf_Xfloat = []
        lf_Yfloat = []
        for x in range(14):
            lf_Xfloat.append(random.randint(1 + 5 * x, 10 + 5 * x))
            lf_Yfloat.append(random.randint(1 + 5 * x, 10 + 5 * x))

        # Assign values for lfI, X and Y
        antCount=0
        for index_1 in range(0, 14, 2):
            datum.antennas[antCount].lfI_X[hour][minute] = lf_Xfloat[index_1]
            datum.antennas[antCount].lfI_Y[hour][minute] = lf_Yfloat[index_1]
            antCount += 1

        # Assign values for lfQ, X and Y
        antCount=0
        for index_2 in range(1, 14, 2):
            datum.antennas[antCount].lfQ_X[hour][minute] = lf_Xfloat[index_2]
            datum.antennas[antCount].lfQ_Y[hour][minute] = lf_Yfloat[index_2]
            antCount += 1

        # insert the record into the DB
        # Ensure this is persisting the correct datum
        datum.save()
        print(f"DB seed is {i / 2880 * 100}% complete.")
        timenow = datetime.datetime.strptime(timenow, '%Y-%m-%d_%H:%M:%S')
        timenow += incrementor
        timenow = timenow.strftime('%Y-%m-%d_%H:%M:%S')

    print(f"time elapsed (seconds) to seed DB: {time.perf_counter() - start}")

if __name__ == '__main__':
    main()
    print("it may have worked")
