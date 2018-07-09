#!/usr/bin/python3.6
"""
This program seeds a database (DB) with data from the cosmos,
written to text files,
having been collected by the Yuan-Tseh Lee Array (ytla) radio telescope.
"""
from Datum import Datum
from Antenna_Snapshot import Antenna_Snapshot
from mongoengine import *

connect('ytla')

def main():
    logSys_line_count = 0
    logCorr_X_line_count = 0
    logCorr_Y_line_count = 0
    logIFLO_X_line_count = 0
    logIFLO_Y_line_count = 0

    for iteration in range(200):

        # the record to be inserted into the DB
        datum = Datum()

        filepath = 'logSys'
        with open(filepath) as fp:
            i = 0
            while i < logSys_line_count:
                fp.readline()
                i += 1
            line = fp.readline().split("    ")
            logSys_line_count += 1
            while not line:
                line = fp.readline().split("    ")
                logSys_line_count += 1
            datum.timestamp = line[0]
            datum.NTState = line[1]
            datum.NTSelect = line[2]
            datum.LOfreq = line[3]
            datum.LOpower = line[4]

        antennas = []
        # 7 antennas exist
        # no. 8 is initialized with the default value of 0 for every attribute
        for antenna in range(0, 8):
            # initialize an Antenna_Snapshot object to contain all data specific to
            # a single antenna at a single moment.
            antennas.append(Antenna_Snapshot())

# TODO: DRY this up
        filepath = 'logCorr_X'
        with open(filepath) as fp:
            i = 0
            while i < logCorr_X_line_count:
                fp.readline()
                i += 1
            line = fp.readline().split("    ")
            logCorr_X_line_count += 1
            while not line:
                line = fp.readline().split("    ")
                logCorr_X_line_count += 1
            for antenna in range(0,7):
                antennas[antenna].sel1X = line[2]
                antennas[antenna].sel2X = line[3]
                antennas[antenna].intswX = line[4]
                antennas[antenna].hybrid_selX = line[5]
                antennas[antenna].intLenX = float((line[6]).strip())
                line = fp.readline().split("    ")
                logCorr_X_line_count += 1

        filepath = 'logCorr_Y'
        with open(filepath) as fp:
            i = 0
            while i < logCorr_Y_line_count:
                fp.readline()
                i += 1
            line = fp.readline().split("    ")
            logCorr_Y_line_count += 1
            while not line:
                line = fp.readline().split("    ")
                logCorr_Y_line_count += 1
            # print(line)
            for antenna in range(0,7):
                antennas[antenna].sel1Y = line[2]
                antennas[antenna].sel2Y = line[3]
                antennas[antenna].intswY = line[4]
                antennas[antenna].hybrid_selY = line[5]
                antennas[antenna].intLenY = float((line[6]).strip())
                line = fp.readline().split("    ")
                logCorr_Y_line_count += 1

        filepath = 'logIFLO_X'
        with open(filepath) as fp:
            i = 0
            while i < logIFLO_X_line_count:
                fp.readline()
                i += 1
            line = fp.readline().split("    ")
            logIFLO_X_line_count += 1
            while not line:
                line = fp.readline().split("    ")
                logIFLO_X_line_count += 1
            for antenna in range(1, 8):
                antennas[antenna - 1].iflo_x = float((line[antenna]).strip())
            antennas[7].iflo_x = 6.0 # lucky no. 7 for July, 2018
            logIFLO_X_line_count += 1

        filepath = 'logIFLO_Y'
        with open(filepath) as fp:
            i = 0
            while i < logIFLO_Y_line_count:
                fp.readline()
                i += 1
            line = fp.readline().split("    ")
            logIFLO_Y_line_count += 1
            while not line:
                line = fp.readline().split("    ")
                logIFLO_Y_line_count += 1
            for antenna in range(1, 8):
                antennas[antenna - 1].iflo_y = float((line[antenna]).strip())
            antennas[7].iflo_y = 6.0 # lucky no. 7 for July, 2018
            logIFLO_Y_line_count += 1

        datum.antennas = antennas # include the antenna data in the record

        datum.save() # insert the record into the DB

# time.sleep(2)
if __name__ == '__main__':
    main()
    print("it may have worked")
