"""
This file contains the definition of the search() function, which handles user
provided information from the client to yield the desired visualization.
"""

from Antenna_Snapshot import Antenna_Snapshot
from Datum import Datum
from attributes import attributes
from bson.objectid import ObjectId # For ObjectId to work
from chart_picker import *
from datetime import datetime
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
import json
from mongoengine import *
import plotly
from rgb_colors import *# 12 different rgb colors
import time
# import pymongo
import plotly.figure_factory as ff
from plotly.graph_objs import Layout, Scatter

def searchy():
    #Searching a Task with various references
    begin_str = request.values.get("begin")
    end_str = request.values.get("end")

    # parse a string as a datetime.datetime
    # The user provided "begin", the beginning of the time range of interest
    begin = datetime.strptime(begin_str, "%Y-%m-%d_%H:%M:%S")
    # The user provided "end", the ending of the time range of interest
    end = datetime.strptime(end_str, "%Y-%m-%d_%H:%M:%S")
    # The user's choice from the dropdown
    attribute_name = request.values.get("refer")
    # The datum value corresponding to the user's choice from the dropdown
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
    # Objects that will be given to plotly for plotting
    data_gettin_visualized = []
    # A collection of attributes that will be identified by a color
    # color_labels = ['DATA']
    color_labels = []

     # assuming mongod is running on 'localhost' at port 27017
    connect('ytla')

    # query the DB, MongoEngine style
    try:
        data_quantity = len(Datum.objects)
        data_count = 1
        for datum in Datum.objects:
            # parse a string (datum.timestamp) as a datetime.datetime
            timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d_%H:%M:%S")
            # TODO: check the accuracy of these timestamps
            if (timestamp >= begin) and (timestamp <= end):

                if (attribute in gantt_chart_per_antenna):
                    # if the list is empty, just append 8 dictionaries
                    if (not attr_states):
                        for antenna in range(0, 8):
                            attr_states.append(
                                dict(
                                    Task=f"Antenna {antenna}",
                                    Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                    Finish='placeholder',
                                    Resource=f"{datum.antennas[antenna][attribute]}"
                                )
                            )
                        # Add the first label to be assigned a color
                        color_labels.append(datum.antennas[-1][attribute])
                    # if it's not the last element in the collection
                    elif (data_count < data_quantity):
                        # print(f"list of dictionaries: {json.dumps(attr_states, indent = 4)}")
                        # print(f"len(attr_states): {len(attr_states)}")
                        for antenna in range(0, 8):
                            # if the color needs to change
                            if (attr_states[-1 - (7 - antenna)]['Resource'] != datum.antennas[antenna][attribute]):
                                # print("srr switch:")
                                # print(json.dumps(attr_states[-1 - (7 - antenna)], indent = 4))
                                # print(json.dumps(datum.antennas[antenna][attribute]))
                                # update the value of the 'Finish' key in the dict 8 elements prior
                                attr_states[-1 - (7 - antenna)]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                                # add a new dict with the new value for the 'Resource' key
                                attr_states.append(
                                    dict(
                                        Task=f"Antenna {antenna}",
                                        Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                        Finish='placeholder',
                                        Resource=f"{datum.antennas[antenna][attribute]}"
                                    )
                                )
                                if (datum.antennas[antenna][attribute] not in color_labels):
                                    color_labels.append(datum.antennas[antenna][attribute])
                            else: # it's the same value as before
                                attr_states.append(
                                    dict(
                                        Task=f"Antenna {antenna}",
                                        Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                        Finish='placeholder',
                                        Resource=f"{datum.antennas[antenna][attribute]}"
                                    )
                                )
                    # TODO: it's the last element and a different value
                    # TODO: it's the last element and a different value and no one has seen this value, yet
                    else: # it's the last element in the data set
                        attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')

                elif (attribute in lone_gantt_chart):
                    if (attr_state == 'placeholder'):
                        attr_states.append(
                            dict(
                                Task="YTLA",
                                Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                Finish='placeholder',
                                Resource=f"{datum[attribute]}"
                            )
                        )
                        attr_state = datum[attribute]
                        color_labels.append(datum[attribute])
                    elif (datum[attribute] != attr_state):
                        attr_state = datum[attribute]
                        attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                        attr_states.append(
                            dict(
                                Task="YTLA",
                                Start=timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                                Finish='placeholder',
                                Resource=f"{datum[attribute]}"
                            )
                        )
                        if (datum[attribute] not in color_labels):
                            color_labels.append(datum[attribute])
                    elif (data_count == data_quantity):
                        attr_states[-1]['Finish'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    # TODO: last element, new color
                    # TODO: last element, new color, new attribute
                elif (attribute in line_chart_per_antenna):
                    for antenna in range(0, 8):
                        y_values_per_antenna[antenna].append(datum.antennas[antenna][attribute])
                else: # (attribute in lone_line_chart):
                    lone_y_values.append(datum[attribute])

                x_values.append(datum.timestamp)

            data_count += 1

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

        # TODO: update this dict to create itself.
        # Currently, it only works with hybrid_selX and hybrid_selY
        # colors = {
        #     'SRR selected': 'rgb(220, 0, 0)',
        #     'SRR NOT selected': 'rgb(0, 255, 100)',
        #     'DATA': (1, 0.9, 0.16)
        # }
        print(f"color_labels: {color_labels}")
        colors = {}
        color_count = 0
        for color in color_labels:
            colors[color] = rgb_colors[color_count]
            color_count += 1

        # TODO: determine whether the strange alternating of antenna to antenna is significant in the displaying of the gantt chart.  Perhaps you must not skip around. You could test this with the data in test_driver.py
        data_gettin_visualized = ff.create_gantt(
            attr_states,
            colors=colors,
            index_col='Resource',
            show_colorbar=True,
            group_tasks=True
        )

        plotly.offline.plot(
            data_gettin_visualized,
            filename=r"visualization.html",
            auto_open=True
        )

    else: # it's a lone_gantt_chart

        colors = {}
        color_count = 0
        for color in color_labels:
            colors[color] = rgb_colors[color_count]
            color_count += 1

        data_gettin_visualized = ff.create_gantt(
            attr_states,
            colors=colors,
            index_col='Resource',
            show_colorbar=True,
            group_tasks=True
        )

        plotly.offline.plot(
            data_gettin_visualized,
            filename=r"visualization.html",
            auto_open=True
        )

    # TODO: zero plotly data corner case
