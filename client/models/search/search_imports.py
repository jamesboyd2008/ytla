"""
This file contains import statements and variables for the search_route.py file
"""

from .. antennas.Antenna_Snapshot import Antenna_Snapshot
from .. datum.Datum import Datum
from .. graph.Graph import Graph
from . attributes import attributes
from bson.objectid import ObjectId # For ObjectId to work
from .. graph.chart_picker import * # TODO: get rid of all *
from datetime import datetime
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
import json
from mongoengine import *
import plotly
from .. graph.graphers.rgb_colors import *# 12 different rgb colors
import time
# import pymongo
import plotly.figure_factory as ff
from plotly.graph_objs import Layout, Scatter
