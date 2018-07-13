"""
This file is the C in MVC. This is the middleman between the front and
back ends.  Information comes here to decide where to go, next.
"""

from Antenna_Snapshot import Antenna_Snapshot
from Datum import Datum
from attributes import attributes
from bson.objectid import ObjectId # For ObjectId to work
from chart_picker import *
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField
# from pymongo import MongoClient # Database connector
# from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    # BooleanField, SubmitField, IntegerField, FormField, validators
# from wtforms.validators import Required

import time
from datetime import datetime
from mongoengine import *
import plotly
# import pymongo
import plotly.figure_factory as ff
from plotly.graph_objs import Layout, Scatter
# import search_route
from search_route import *



app = Flask(__name__)
# Bootstrap(app)
title = "YTLA Data"
headig = "YTLA Data"

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
@app.route("/uncompleted")
def tasks ():
    a2="active"
    return render_template('index.html',a2=a2,butes=attributes,t=title,h=headig)

@app.route("/search", methods=['GET'])
def search():
    searchy()
    return redirect('/')

if __name__ == "__main__":
    # app.run(debug=True) # Careful with the debug mode..
    app.run(host='0.0.0.0', debug=True, port=5000)
