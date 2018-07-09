
from Antenna_Snapshot import Antenna_Snapshot
from Datum import Datum
from bson.objectid import ObjectId # For ObjectId to work
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
from plotly.graph_objs import Layout, Scatter

attributes = [
    'sel1X',
    'sel2X',
    'intswX',
    'hybrid_selX',
    'intLenX',
    'sel1Y',
    'sel2Y',
    'intswY',
    'hybrid_selY',
    'intLenY',
    'Timestamp',
    'NTState',
    'NTSelect',
    'LOfreq',
    'LOpower',
    # 'lfI_X',
    # 'lfQ_X',
    # 'lfI_Y',
    # 'lfQ_Y',
    'IFLO_X',
    'IFLO_Y'
]

app = Flask(__name__)
# Bootstrap(app)
title = "MongoDB Demo"
heading = "MongoDB Demo"
#modify=ObjectId()


def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
@app.route("/uncompleted")
def tasks ():
    a2="active"
    return render_template('index.html',a2=a2,attributes=attributes,t=title,h=heading)

@app.route("/search", methods=['GET'])
def search():
    #Searching a Task with various references
    begin_str = request.values.get("begin")
    end_str = request.values.get("end")

    # parse a string as a datetime.datetime
    begin = datetime.strptime(begin_str, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

    attribute = request.values.get("refer")

    # a list of empty lists, each empty list representing an antenna.
    # antennas 0-6, plus lucky_no_7 (for a total of 8)
    y_values = [[], [], [], [], [], [], [], []]
    x_values = []

    # TODO: add lists for datum attributes besides antennas

    data_gettin_visualized = []

     # assuming mongod is running on 'localhost' at port 27017
    connect('ytla')

    if (attribute == "IFLO_X"):
        # try:
        #     # for rec in collection.find({"instrument":"ETH"}):
        #     for rec in db.find({"antennas":"ETH"}):
        #         eth_ts = datetime.datetime.fromtimestamp(rec['timestamp'])
        #         if (eth_ts >= begin) and (eth_ts <= end):
        #             eth_last_price.append(rec['lastPrice'])
        #             eth_best_bid.append(rec['bestBid'])
        #             eth_best_ask.append(rec['bestAsk'])
        #             eth_timestamp.append(eth_ts)
        # except Exception as err:
        #     print(err)

        # query the DB, MongoEngine style
        try:
            for datum in Datum.objects:
                # parse a string (datum.timestamp) as a datetime.datetime
                timestamp = datetime.strptime(datum.timestamp, "%Y-%m-%d %H:%M:%S")
                # TODO: check the accuracy of these timestamps
                if (timestamp >= begin) and (timestamp <= end):
                    x_values.append(datum.timestamp)
                    # add the iflo_x value for each antenna
                    # for antenna in range(1, 8):
                    for antenna in range(0, 8):
                        y_values[antenna].append(datum.antennas[antenna].iflo_x)
        except Exception as err:
            print(err)

        # for antenna in range(1, 8):
        for antenna in range(0, 8):
            data_gettin_visualized.append(
                Scatter(
                    y=y_values[antenna],
                    x=x_values,
                    name=f"Antenna {antenna} IFLO_X",
                    mode='lines+markers'
                )
            )
            # TODO: pick a color for the lines
    # elif (attribute == "btc"):





    # print(f"attribute: {attribute}")
    # each attribute should be present for each array
    # if (attribute == "eth"):
    #     try:
    #         # for rec in collection.find({"instrument":"ETH"}):
    #         for rec in db.find({"instrument":"ETH"}):
    #             eth_ts = datetime.datetime.fromtimestamp(rec['timestamp'])
    #             if (eth_ts >= begin) and (eth_ts <= end):
    #                 eth_last_price.append(rec['lastPrice'])
    #                 eth_best_bid.append(rec['bestBid'])
    #                 eth_best_ask.append(rec['bestAsk'])
    #                 eth_timestamp.append(eth_ts)
    #     except Exception as err:
    #         print(err)
    #
    #     attribute_lp = Scatter(
    #         y=eth_last_price,
    #         x=eth_timestamp,
    #         name='ETH Last Price',
    #         mode='lines+markers')
    #
    #     attribute_bb = Scatter(
    #         y=eth_best_bid,
    #         x=eth_timestamp,
    #         name='ETH Best Bid',
    #         mode='lines+markers')
    #
    #     attribute_ba = Scatter(
    #         y=eth_best_ask,
    #         x=eth_timestamp,
    #         name='ETH Best Ask',
    #         mode='lines+markers')
    #
    #
    #
    # elif (attribute == "btc"):
    #     # Because of the price difference between Etherum and Bitcoin
    #     # Divide Bitcon prices by 10 to make the graph nicer
    #     try:
    #         # for rec in collection.find({"instrument":"BTC"}):
    #         for rec in db.find({"instrument":"BTC"}):
    #             btc_ts = datetime.datetime.fromtimestamp(rec['timestamp'])
    #             if (btc_ts >= begin) and (btc_ts <= end):
    #                 btc_last_price.append(rec['lastPrice'] / 10)
    #                 btc_best_bid.append(rec['bestBid'] / 10)
    #                 btc_best_ask.append(rec['bestAsk'] / 10)
    #                 btc_timestamp.append(btc_ts)
    #     except Exception as err:
    #         print(err)
    #
    #     attribute_lp = Scatter(
    #         y=btc_last_price,
    #         x=btc_timestamp,
    #         name='BTC Last Price minus 10^1',
    #         mode='lines+markers')
    #
    #     attribute_bb = Scatter(
    #         y=btc_best_bid,
    #         x=btc_timestamp,
    #         name='BTC Best Bid minus 10^1',
    #         mode='lines+markers')
    #
    #     attribute_ba = Scatter(
    #         y=btc_best_ask,
    #         x=btc_timestamp,
    #         name='BTC Best Ask minus 10^1',
    #         mode='lines+markers')

    # title = attribute + " Markets Graph"
    # beginning = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    beginning = begin.strftime('%Y-%m-%d %H:%M:%S')
    ending = end.strftime('%Y-%m-%d %H:%M:%S')
    title = f"{attribute } from {beginning} to {ending}"

    plotly.offline.plot(
        {
            'data': data_gettin_visualized,
            'layout': Layout(title = title)
        },
        filename=r"visualization.html",
        auto_open=True
    )

    # return render_template('searchlist.html',todos=todos,t=title,h=heading)
    a1 = "active"
    return render_template('index.html',a1=a1,t=title,h=heading,attributes=attributes)

if __name__ == "__main__":
    # app.run(debug=True) # Careful with the debug mode..
    app.run(host='0.0.0.0', debug=True, port=5000)
