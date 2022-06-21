# SI 506 Lecture 23

import csv
import json
import requests


def drop_data(entity, keys):
    """Deletes < entity > dictionary key-values pairs if a key matches a key
    in the passed in < keys > tuple.

    Parameters:
        entity (dict): dictionary with key-value pairs to drop (i.e., delete)
        keys (tuple): key-value pairs to remove from < entity >

    Returns:
        dict: dictionary with matching key-value pairs removed
    """

    pass # TODO Implement


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        # data = []
        # reader = csv.DictReader(file_obj, delimiter=delimiter)
        # for line in reader:
        #     data.append(line) # OrderedDict
        #     # data.append(dict(line)) # convert OrderedDict to dict

        # return data

        # Implement using a list comprehension
        pass # TODO Reimplement (2 lines of code max)


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point."""

    endpoint = 'https://swapi.py4e.com/api'


    # CHALLENGE 01

    response = None # Call function

    # print(f"\nChallenge 01: Response\n{response}")

    chewie = None # Get Chewie from response

    # print(f"\nChallenge 01: Chewbacca\n{chewie}")

    # TODO Write to file

    # Add homeworld
    # TODO Uncomment
    # chewie[???] = None # TODO Call function

    # Add species
    # TODO Uncomment
    # chewie[???] = None # TODO Call function

    # print(f"\nChallenge 01: Chewbacca enriched\n{chewie}")

    # TODO Write to file


    # CHALLENGE 02

    drop_keys = ('films', 'created', 'edited', 'people', 'residents', 'starships', 'vehicles')

    x_wing = None # Call function
    x_wing = None # Call function and delete key-value pairs

    # print(f"\nChallenge 02: T-65 X-wing\n{x_wing}")

    # TODO Write to file


    # CHALLENGE 03

    wookiee_starships = None # TODO call function and read file
    wookiee_x_wing = None # Get T-65 X-wing

    # TODO Combine dictionaries (xwing and wookiee_x_wing)

    # print(f"\nChallenge 03: T-65 X-wing enhanced\n{x_wing}")

    # TODO Write to file


    # CHALLENGE 04

    # TODO Implement loop

    # WARN: elements are not updated using a simple for loop

    # TODO Write to file


    # CHALLENGE 05

    x_wing = None # TODO Call function and drop data

    # Get Luke Skywalker
    luke = None # Call function
    luke = None # Call function

    homeworld = None # Call function
    # TODO Uncomment
    # luke[???] = None # Call function

    # TODO Get Luke's species (if URL exists) and assign to luke[???]

    # Get R2-D2 (Astromech droid)
    r2 = None # Call function
    r2 = None # Call function

    homeworld = None # Call function
    # TODO Uncomment
    # r2[???] = None # Call function

    # TODO Get R2-D2 species (if URL exists) and assign to r2[???]

    # TODO Assign crew_members to x_wing

    # TODO Write to file


if __name__ == '__main__':
    main()
