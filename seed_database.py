#!/usr/bin/python3.6

# This program seeds a database (DB) with data from text files.
# Some data are random.
# Some data are from the Yuan-Tseh Lee Array (ytla) radio telescope.

from client.models.datum.Datum import Datum
from client.models.antennas.Antenna_Snapshot import Antenna_Snapshot
from mongoengine import *
import random

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

        filepath = 'db_ops/logSys'
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
            datum.nt_state = line[1]
            datum.nt_select = line[2]
            datum.lo_freq = float((line[3]).strip())
            datum.lo_power = float((line[4]).strip())


        antennas = []
        # 7 antennas exist
        # no. 8 is initialized with the default value of 0 for every attribute
        for antenna in range(0, 8):
            # initialize an Antenna_Snapshot object to contain all data specific to
            # a single antenna at a single moment.
            datum.antennas.append(Antenna_Snapshot())

# TODO: DRY this up
        filepath = 'db_ops/logCorr_X'
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
                datum.antennas[antenna].sel1X = line[2]
                datum.antennas[antenna].sel2X = line[3]
                datum.antennas[antenna].intswX = line[4]
                datum.antennas[antenna].hybrid_selValX = line[5]
                datum.antennas[antenna].intLenX = float((line[6]).strip())
                line = fp.readline().split("    ")
                logCorr_X_line_count += 1

        filepath = 'db_ops/logCorr_Y'
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
                datum.antennas[antenna].sel1Y = line[2]
                datum.antennas[antenna].sel2Y = line[3]
                datum.antennas[antenna].intswY = line[4]
                datum.antennas[antenna].hybrid_selValY = line[5]
                datum.antennas[antenna].intLenY = float((line[6]).strip())
                line = fp.readline().split("    ")
                logCorr_Y_line_count += 1

        filepath = 'db_ops/logIFLO_X'
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
                datum.antennas[antenna - 1].iflo_x = float((line[antenna]).strip())
            logIFLO_X_line_count += 1

        filepath = 'db_ops/logIFLO_Y'
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
                datum.antennas[antenna - 1].iflo_y = float((line[antenna]).strip())
            logIFLO_Y_line_count += 1

        lf_Xfloat = []
        lf_Yfloat = []
        for x in range(14):
            lf_Xfloat.append(random.randint(1 + 5 * x, 10 + 5 * x))
            lf_Yfloat.append(random.randint(1 + 5 * x, 10 + 5 * x))

        # Assign values for lfI, X and Y
        antCount=0
        for i in range(0, 14, 2):
            datum.antennas[antCount].lfI_X = lf_Xfloat[i]
            datum.antennas[antCount].lfI_Y = lf_Yfloat[i]
            antCount+=1

        # Assign values for lfQ, X and Y
        antCount=0
        for i in range(1, 14, 2):
            datum.antennas[antCount].lfQ_X = lf_Xfloat[i]
            datum.antennas[antCount].lfQ_Y = lf_Yfloat[i]
            antCount+=1

        datum.save() # insert the record into the DB

if __name__ == '__main__':
    main()
    print("it may have worked")
