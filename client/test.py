from bson.objectid import ObjectId # For ObjectId to work
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField
from pymongo import MongoClient # Database connector
# from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    # BooleanField, SubmitField, IntegerField, FormField, validators
# from wtforms.validators import Required
import time
import datetime
import plotly
import pymongo
from plotly.graph_objs import Layout, Scatter

# client = MongoClient('localhost', 27017)    #Configure the connection to the database
# db = client.camp2016    #Select the database
# todos = db.todo #Select the collection
todos = []
# db = client.ytla
# collection = db['stats']
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
    #Display the Uncompleted Tasks
    # todos_l = todos.find({"done":"no"})
    a2="active"
    # return render_template('index.html',a2=a2,todos=todos_l,t=title,h=heading)
    return render_template('index.html',a2=a2,attributes=attributes,t=title,h=heading)

@app.route("/search", methods=['GET'])
def search():
    #Searching a Task with various references
    begin = request.values.get("begin")
    end = request.values.get("end")
    attribute = request.values.get("refer")
    # if(key=="_id"):
    # 	todos_l = todos.find({refer:ObjectId(key)})
    # else:
    # 	todos_l = todos.find({refer:key})

    # eth_last_price = []
    # eth_best_bid = []
    # eth_best_ask = []
    # eth_timestamp = []
    #
    # btc_last_price = []
    # btc_best_bid = []
    # btc_best_ask = []
    # btc_timestamp = []

    client = pymongo.MongoClient('localhost', 27017)
    db = client.ytla
    # collection = db['stats']

    if (attribute == "IFLO_X"):
        try:
            # for rec in collection.find({"instrument":"ETH"}):
            for rec in db.find({"antennas":"ETH"}):
                eth_ts = datetime.datetime.fromtimestamp(rec['timestamp'])
                if (eth_ts >= begin) and (eth_ts <= end):
                    eth_last_price.append(rec['lastPrice'])
                    eth_best_bid.append(rec['bestBid'])
                    eth_best_ask.append(rec['bestAsk'])
                    eth_timestamp.append(eth_ts)
        except Exception as err:
            print(err)

        attribute_lp = Scatter(
            y=eth_last_price,
            x=eth_timestamp,
            name='ETH Last Price',
            mode='lines+markers')

        attribute_bb = Scatter(
            y=eth_best_bid,
            x=eth_timestamp,
            name='ETH Best Bid',
            mode='lines+markers')

        attribute_ba = Scatter(
            y=eth_best_ask,
            x=eth_timestamp,
            name='ETH Best Ask',
            mode='lines+markers')



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

    title = attribute + " Markets Graph"
    plotly.offline.plot(
        {
            # 'data': [eth_lp, eth_bb, eth_ba, btc_lp, btc_bb, btc_ba],
            # 'data': [btc_lp, btc_bb, btc_ba],
            'data': [attribute_lp, attribute_bb, attribute_ba],
            'layout': Layout(title = title)},
        filename=r"btc.html", auto_open=True)

    # return render_template('searchlist.html',todos=todos,t=title,h=heading)
    a1 = "active"
    return render_template('index.html',a1=a1,t=title,h=heading,attributes=attributes)

if __name__ == "__main__":
    # app.run(debug=True) # Careful with the debug mode..
    app.run(host='0.0.0.0', debug=True, port=5000)
