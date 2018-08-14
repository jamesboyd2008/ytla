
from Antenna_Snapshot import Antenna_Snapshot
from Datum import Datum
from bson.objectid import ObjectId # For ObjectId to work
import time
from datetime import datetime
from mongoengine import *
import plotly
from plotly.graph_objs import Layout, Scatter

def main():

    connect('ytla')

    nums = [[]] * 8

    for datum in Datum.objects:
        for num in range(0, 8):
            nums[num].append(datum.antennas[num].iflo_x)

    for num in range(0, 8):
        print(f"nums[{num}]: {nums[num]}")

if __name__ == "__main__":
    main()
