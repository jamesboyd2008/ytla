"""
This file contains the definition of the search() function, which handles user
provided information from the client to yield the desired visualization.
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

def searchy():
    print("triggered 2")
    #Searching a Task with various references
    begin_str = request.values.get("begin")
    end_str = request.values.get("end")

    # parse a string as a datetime.datetime
    begin = datetime.strptime(begin_str, "%Y-%m-%d_%H:%M:%S")
    end = datetime.strptime(end_str, "%Y-%m-%d_%H:%M:%S")

    attribute_name = request.values.get("refer")
    attribute = attributes[attribute_name]

    # a list of empty lists, each empty list representing an antenna.
    # antennas 0-6, plus lucky_no_7 (for a total of 8)
    y_values_per_antenna = [ [], [], [], [], [], [], [], [] ]
    # For antenna-agnostic data that will be represented by a single line chart
    lone_y_values = []
    # For antenna-specific data that will be represented with a gantt chart
    attr_states = []
    # For antenna-agnostic data that will be represneted with a gantt chart
    attr_state = 'placeholder'
    # For timestamps
    x_values = []

    # For determining what kind of plot to plot
    # multi_line = False
    # single_line = False
    # multi_gantt = False
    # single_gantt = False

    # TODO: add lists for datum attributes besides antennas

    data_gettin_visualized = []
    # print("here")
     # assuming mongod is running on 'localhost' at port 27017
    connect('ytla')

    # query the DB, MongoEngine style
    try:
        for datum in Datum.objects:
            # parse a string (datum.timestamp) as a datetime.datetime
            timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")
            # TODO: check the accuracy of these timestamps
            if (timestamp >= begin) and (timestamp <= end):

                if (attribute in gantt_chart_per_antenna):
                    for antenna in range(0, 8):
                        if (not attr_state[antenna]):
                            attr_states[antenna].append(
                                dict(
                                    Task=f"Antenna {antenna}",
                                    Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                    Finish='placeholder',
                                    Resource=f"{datum.antennas[antenna][attribute]}"
                                )
                            )
                        elif (attr_states[antenna][-1]["Resource"] != datum.antennas[antenna][attribute]):
                            attr_states[antenna][-1]["Finish"] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                            attr_states[antenna].append(
                                dict(
                                    Task=f"Antenna {antenna}",
                                    Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                    Finish='placeholder',
                                    Resource=f"{datum.antennas[antenna][attribute]}"
                                )
                            )
                elif (attribute in lone_gantt_chart):
                    # TODO: write this block
                    print("yes")
                x_values.append(datum.timestamp)
                if (attribute in line_chart_per_antenna):
                    for antenna in range(0, 8):
                        y_values_per_antenna[antenna].append(datum.antennas[antenna][attribute])
                elif (attribute in lone_line_chart):
                    lone_y_values.append(datum[attribute])


                #
                # elif (attribute in gantt_chart_per_antenna):
                #
                #
                #
                #
                #
                #     df = [
                #         dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
                #         dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
                #         dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
                #         dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
                #         dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
                #         dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
                #         dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
                #         dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')
                #     ]
                #     colors = {
                #         'Not Started': 'rgb(220, 0, 0)',
                #         'Incomplete': (1, 0.9, 0.16),
                #         'Complete': 'rgb(0, 255, 100)'
                #     }
                #
                #     fig = plotly.figure_factory.create_gantt(
                #         df,
                #         colors=colors,
                #         index_col='Resource',
                #         show_colorbar=True,
                #         group_tasks=True
                #     )
                #     plotly.offline.plot(
                #         fig,
                #         filename='gantt-group-tasks-together',
                #         auto_open=True
                #     )

    except Exception as err:
        print(err)

    # print(f"attribute: {attribute}")
    # print(f"attribute in gantt_chart_per_antenna: {attribute in gantt_chart_per_antenna}")

    beginning = begin.strftime('%Y-%m-%d %H:%M:%S')
    ending = end.strftime('%Y-%m-%d %H:%M:%S')
    title = f"{attribute } from {beginning} to {ending}"
    fig = {
        'data': data_gettin_visualized,
        'layout': Layout(title = title)
    }

    if (attribute in line_chart_per_antenna):
        for antenna in range(0, 8):
            data_gettin_visualized.append(
                Scatter(
                    y=y_values_per_antenna[antenna],
                    x=x_values,
                    name=f"Antenna {antenna} {attribute_name}",
                    mode='lines+markers'
                )
            )
        plotly.offline.plot(
            {
                'data': data_gettin_visualized,
                'layout': Layout(title = title)
            },
            filename=r"visualization.html",
            auto_open=True
        )
        print("triggered 0")

    elif (attribute in lone_line_chart):
        data_gettin_visualized.append(
            Scatter(
                y=lone_y_values,
                x=x_values,
                name=f"YTLA {attribute_name}",
                mode='lines+markers'
            )
        )
        plotly.offline.plot(
            {
                'data': data_gettin_visualized,
                'layout': Layout(title = title)
            },
            filename=r"visualization.html",
            auto_open=True
        )

    elif (attribute in gantt_chart_per_antenna):
        colors = {'SRR selected': 'rgb(220, 0, 0)',
                  'SRR NOT selected': 'rgb(0, 255, 100)'}

        fig = ff.create_gantt(
            attr_states,
            colors=colors,
            index_col='Resource',
            show_colorbar=True,
            group_tasks=True #pickup here. make it work
        )

        plotly.offline.plot(
            fig,
            filename=r"visualization.html",
            auto_open=True
        )


    else: # it's a lone_gantt_chart
        print("it's a lone_gantt_chart")

    # elif (attribute in gantt_chart_per_antenna):
    #     data_gettin_visualized.append(
    #         Scatter( not going to be a scatter
    #             y=lone_y_values,
    #             x=x_values,
    #             name=f"YTLA {attribute_name}",
    #             mode='lines+markers'
    #         )
    #     )
    # elif (attribute in lone_gantt_chart):
    #     data_gettin_visualized.append(
    #         Scatter( not going to be a scatter
    #             y=lone_y_values,
    #             x=x_values,
    #             name=f"YTLA {attribute_name}",
    #             mode='lines+markers'
    #         )
    #     )


    # TODO: zero plotly data corner case

    # return render_template('searchlist.html',todos=todos,t=title,h=headig)
    # a1 = "active"
    # return render_template('index.html',a1=a1,t=title,h=headig,butes=attributes)
