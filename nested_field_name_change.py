# This program renames a field within an array in every item in the
# database (DB) after soliciting the user for the old name and the new name.

import pymongo
from sys import version_info # To get your version of python

def update_db(old_var, new_var):
    """
    This function updates the name of a list-nested-object-field in MongoDB

    Parameters:
        old_var (str) : the old name of the variable to be updated.
        new_var (str) : the new name of the variable to be updated.

    Returns:
        result (str) : success/failure message
    """

    # Success/failure message
    result = "The update failed."
    # Connect with the MongoDB server which is assumed to already be running on
    # the local machine at port 27017.
    client = pymongo.MongoClient('localhost', 27017)
    # Connect with the DB.
    db = client.ytla
    # Use the datum collection
    collection = db['datum']

    try:
        for datum in collection.find({}):
            item = datum
            id = datum['_id']
            # Iterate over 8 antennas
            for i in range(0, 8):
                # Add the new field
                item["antennas"][i][new_var] = item["antennas"][i][old_var]
                # Delete the old field
                del item["antennas"][i][old_var]
            # Persist the update(s)
            result = collection.update_one(
                {"_id": id},
                { "$set": item }
            )
    except pymongo.errors.ConnectionFailure as err:
        print('Connection Error: ', err)

    return result

def main():
    """
    Solicits the user for variable names and updates the name of the variable.
    """
    # creates boolean value, representing your version of python (3+ or other)
    py3 = version_info[0] > 2

    # Questions for the user
    old_name_message = "Please enter the current name of the variable: "
    new_name_message = "Please enter the new name of the variable: "

    # If the user is using Python3+
    if py3:
        old_var = input(old_name_message)
        new_var = input(new_name_message)
    # The user is using something before Python3
    else:
        old_var = raw_input(old_name_message)
        new_var = raw_input(new_name_message)

    # print a success/failure message
    print(update_db(old_var, new_var))

if __name__ == "__main__":
    main()
