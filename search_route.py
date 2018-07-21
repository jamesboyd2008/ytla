# This file contains the definition of the searchy function, which handles user
# provided information from the client to yield the desired visualization.

from search_imports import *
from datum_helper import *
from plotter import plotter

def searchy(begin, end, refer):
    """
    This function searches the DB.

    This function searches the DB, making a plotly graph out of all items that
    match the contextually derived search criteria, which is attribute and
    a range of timestamps.

    Parameters:
        begin (str) : The beginning of the time range of interest.
        end (str) : The end of the time range of interest.
        refer (str) : The attribute of interest, e.g., sel1x

    Returns:
        NoneType
    """

    # assuming mongod is running on 'localhost' at port 27017
    # Connect to the DB
    connect('ytla')

    graph_meta_data = {
        # The user provided "begin", the beginning of the time range of interest
        # strptime() --> string parsed to a struct_time object
        'begin': datetime.strptime(begin, "%m/%d/%Y %H:%M"), # 01/23/2019 12:27 PM
        # The user provided "end", the ending of the time range of interest
        'end': datetime.strptime(end, "%m/%d/%Y %H:%M"),
        # The user's choice from the dropdown
        'attribute': refer,
        # the number of Datum objects in the DB
        'data_quantity': len(Datum.objects),
        # a counter, representing the number of Datum objects
        'data_count': 1
    }

    # The object that will get graphed
    graph = Graph()

    double_tuple = (graph, graph_meta_data)


    # try to querry the DB, MongoEngine style
    try:
        # TODO: make this loop something more sensible.
        # What if the time range isn't that of the whole DB?
        # Make this loop break before the end of the DB if the timestamps
        # are too late, anyhow. ... or will this pattern break, later?
        for datum in Datum.objects:
            # This function is called for every element in the DB
            double_tuple = datum_helper(datum, double_tuple)
    except Exception as err:
        print(err)
        # you can define more errors, here

    # plot the graph
    plotter(double_tuple)
