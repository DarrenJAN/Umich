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

    # dict comprehension is inappropriate here; not creating a new dict
    # using it for the side effects (i.e., delete key-value pair)
    # del is also a statement and can't be used inside a comprehension
    # return {del entity[key] for key in keys if key in entity.keys()}

    for key in keys:
        if key in entity.keys():
            del(entity[key])

    return entity


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

        reader = csv.DictReader(file_obj, delimiter=delimiter)
        return [line for line in reader] # list of OrderDicts


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

    response = get_swapi_resource(f"{endpoint}/people/", {'search': 'chewbacca'})

    print(f"\nChallenge 01: Response\n{response}")

    chewie = response['results'][0] # first element

    print(f"\nChallenge 01: Chewbacca\n{chewie}")

    # Write to file
    write_json('stu-chewie.json', chewie)

    # Add homeworld
    chewie['homeworld'] = get_swapi_resource(chewie['homeworld'])

    # Add species
    if chewie['species']:
        chewie['species'] = get_swapi_resource(chewie['species'][0]) # list element

    print(f"\nChallenge 01: Chewbacca enriched\n{chewie}")

    # Write to file
    write_json('stu-chewie_enriched.json', chewie)


    # CHALLENGE 02

    drop_keys = ('films', 'created', 'edited', 'people', 'residents', 'starships', 'vehicles')

    x_wing = get_swapi_resource(f"{endpoint}/starships/", {'search': 't-65 x-wing'})['results'][0]
    x_wing = drop_data(x_wing, drop_keys) # delete key-value pairs

    print(f"\nChallenge 02: T-65 X-wing\n{x_wing}")

    # Write to file
    write_json('stu-x_wing.json', x_wing)


    # CHALLENGE 03

    wookiee_starships = read_csv_to_dicts('wookieepedia_starships.csv')
    wookiee_x_wing = wookiee_starships[-2] # T-65 X-wing

    # Combine data (dict.update())
    x_wing.update(wookiee_x_wing) # update existing matching keys/add new key-value pairs

    print(f"\nChallenge 03: T-65 X-wing enhanced\n{x_wing}")

    # Write to file
    write_json('stu-x_wing_enriched.json', x_wing)


    # CHALLENGE 04

    for i in range(len(x_wing['pilots'])):
        # Get URL
        pilot = get_swapi_resource(x_wing['pilots'][i])
        pilot = drop_data(pilot, drop_keys)

        # Get pilot's home planet
        homeworld = get_swapi_resource(pilot['homeworld'])
        pilot['homeworld'] = drop_data(homeworld, drop_keys)

        # Get pilot's species
        # WARN: Pilot Jek Tono Porkins has no species URL
        if pilot['species']:
            species = get_swapi_resource(pilot['species'][0])
            pilot['species'] = drop_data(species, drop_keys)

        # Replace URLs
        x_wing['pilots'][i] = pilot

    # WARN: elements are not updated using a simple for loop
    # for element in x_wing['pilots']:
    #     pilot = get_swapi_resource(element)
    #     element = drop_data(pilot, drop_keys) # does not update value

    # Write to file
    write_json('stu-x_wing_pilots.json', x_wing)


    # CHALLENGE 05

    x_wing = drop_data(x_wing, ('pilots',)) # one-item tuple

    # Get Luke Skywalker
    luke = get_swapi_resource(f"{endpoint}/people", {'search': 'luke skywalker'})['results'][0]
    luke = drop_data(luke, drop_keys)

    homeworld = get_swapi_resource(luke['homeworld'])
    luke['homeworld'] = drop_data(homeworld, drop_keys)

    if luke['species']:
        species = get_swapi_resource(luke['species'][0])
        luke['species'] = drop_data(species, drop_keys)

    # Get R2-D2 (Astromech droid)
    r2 = get_swapi_resource(f"{endpoint}/people", {'search': 'r2-d2'})['results'][0]
    r2 = drop_data(r2, drop_keys)

    homeworld = get_swapi_resource(r2['homeworld'])
    r2['homeworld'] = drop_data(homeworld, drop_keys)

    if r2['species']:
        species = get_swapi_resource(r2['species'][0])
        r2['species'] = drop_data(species, drop_keys)

    x_wing['crew_members'] = {'pilot': luke, 'astromech_droid': r2}

    # Write to file
    write_json('stu-x_wing_crew.json', x_wing)


if __name__ == '__main__':
    main()
