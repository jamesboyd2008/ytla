#!/usr/bin/python

# This file contains the function definition for timestamp_converter.

from datetime import datetime
import pymongo
import sys

def timestamp_converter(db, collection):
    """
    Converts timestamps in MongoDB from str to datetime.datetime.

    Parameters:
        db (str) : the name of the database.
        collection (str) : the name of the collection.

    Returns:
        result (str) : success/failure message
    """

    result = "The update failed."
    # Connect with the MongoDB server which is assumed to already be running on
    # the local machine at port 27017.
    client = pymongo.MongoClient('localhost', 27017)
    # Connect with the appropriate DB.
    db = client[db]
    # Use the appropriate collection.
    collection = db[collection]

    try:
        for datum in collection.find({}):
            rec = datum
            id = datum['_id']

            timestamp = datetime.strptime(rec["timestamp"], "%Y-%m-%d_%H:%M:%S")
            rec["timestamp"] = timestamp

            # Persist the update(s)
            result = collection.update_one(
                {"_id": id},
                { "$set": rec }
            )
    except pymongo.errors.ConnectionFailure as err:
        print('Connection Error: ', err)

    print(result)
    return result

if __name__ == "__main__":
    timestamp_converter(sys.argv[1], sys.argv[2])
