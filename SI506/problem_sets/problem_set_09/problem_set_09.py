import requests
import json

# HELPER FUNCTION. DO NOT ALTER
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

# HELPER FUNCTION. DO NOT ALTER
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is;
                            otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to
                      encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

# PROBLEM 1
def get_swapi_resource(url, params=None):
    """
    Initiates an HTTP GET request to the SWAPI service in order
    to return a representation of a resource. < params > is not included in the
    request if no params is passed to this function during the function call.
    Once a response is received, it is converted to a python dictionary.

    Parameters:
        url (str): a URL that specifies the resource.
        params (dict): an optional dictionary of querystring arguments.
        The default value is None.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params == None:
        response = requests.get(url)
        resources = response.json() # convert message payload to dict
    else:
        response = requests.get(url, params) 
        resources = response.json() # convert message payload to dict
    return resources

# PROBLEM 2
def get_passenger_info(passenger, characteristics):
    """
    Creates a dictionary representing a passenger by extracting
    the key-value pairs from the SWAPI representation of the passenger
    (i.e., the JSON object retrieved from the SWAPI API)

    Since there are multiple key-value pairs in the < passenger > dictionary
    retrieved from the SWAPI API, the function simplifies the < passenger >
    dictionary by only keeping the key-value pairs that have the key in
    < characteristics >. In addition, if the key in < passenger > is 'homeworld'
    or 'species', utilizes the function < get_swapi_resource > to get the
    corresponding names of the homeworld and species. Then use the names of the
    homeworld and species as the values for the corresponding keys 'homeworld',
    'species'.

    Parameters:
        passenger (dict): a dictionary containing information about a passenger
        characteristics (list): a list of strings representing a passenger's
        characteristics

    Returns:
        dict: a dictionary containing information about a passenger
    """

    result = {}
    for c in characteristics:
        result[c] = passenger[c]
        if c == 'homeworld':
            result[c] = get_swapi_resource(passenger[c])['name']
        elif c == 'species':
            result[c] = get_swapi_resource(passenger[c][0])['name']
    return result

# PROBLEM 3
def update_passenger_info(passenger_info, filepath):
    """
    To further enrich the dictionary returned from the function
    get_passenger_info(), updates the dictionary by adding the key-value pairs
    from the JSON file.

    Delegates to the function < read_json() > the task of returning a
    dictionary from the given file path. Then iterates over the dictionary's keys to
    get each passenger's name. If the name is in the value of passenger_info['name'],
    updates the < passenger_info > dictionary by adding the corresponding value
    from the dictionary returned from the read_json() function.

    Parameters:
        passenger_info (dict): a dictionary containing information about a passenger
        filepath (str): a path to a file

    Returns:
        None
    """
    read_result = read_json(filepath)
    for key, value in read_result.items():
        if key.lower() in passenger_info['name'].lower():
            passenger_info.update(value)


# PROBLEM 4
def group_passengers(passengers_list):
    """
    Generates a dictionary that has two key-value pairs. The keys
    are 'human' and 'droid', and the values are lists of dictionaries, each
    containing information of a passenger.

    Parameters:
        passengers_list (list): a list of dictionaries, each containing
        information about a passenger.

    Returns:
        dict: a dictionary that classifies the passengers into two types:
        human or droid
    """

    human_passengers = []
    droid_passengers = []
    passenger_groups = {}
    for passenger in passengers_list:
        if passenger['species'] == 'Human':
            human_passengers.append(passenger)
        else:
            droid_passengers.append(passenger)

    passenger_groups['human'] = human_passengers
    passenger_groups['droid'] = droid_passengers
    return passenger_groups

# PROBLEM 5
def get_starships(person):
    """
    Creates a list of dictionaries, each containing a starship's
    name and max atmosphering speed.

    Given the SWAPI representation of a person, accesses the starships' URLs.
    Iterates over the URLs. Delegates to the function < get_swapi_resource > to
    return a SWAPI representation of a starship. Uses the starship's name,
    max atmosphering speed, and max passenger capacity as the values in a dictionary
    that has the keys 'name', 'max_atmosphering_speed', 'passengers', respectively.
    Adds the dictionary to a list.

    Parameters:
        person (dict): a SWAPI representation of a person

    Returns:
        list: a list of dictionaries, each containing a starship's name and max
        atmosphering speed.
    """

    starships_list = []
    starships_urls = person['starships']
    for cur_url in starships_urls:
        starship_dict = {}
        starship_dict['name'] = get_swapi_resource(cur_url)['name']
        starship_dict['max_atmosphering_speed'] = get_swapi_resource(cur_url)['max_atmosphering_speed']
        starship_dict['passengers'] = get_swapi_resource(cur_url)['passengers']
        starships_list.append(starship_dict)
    return starships_list

# PROBLEM 6
def get_fastest_starship(person):
    """
    Finds the fastest starship among the person's starships.

    Delegates to the function < get_starships > the task of returning a list of starships. Then
    iterates over the starships to find the starship with the highest max
    atmosphering speed. Returns this starship to the caller.

    Parameters:
        person (dict): a SWAPI representaition of a person

    Returns:
        dict: a dictionary containing the fastest starship's name and
        max_atmosphering_speed.
    """

    starships = get_starships(person)
    min_speed = 0
    result = {}
    for starship in starships:
        if(int(starship['passengers']) >= 3):
            if int(starship['max_atmosphering_speed']) > min_speed:
                min_speed = int(starship['max_atmosphering_speed'])
                result['name'] = starship['name']
                result['max_atmosphering_speed'] = starship['max_atmosphering_speed']
                result['passengers'] = starship['passengers']
    return result

# PROBLEM 7
def board_ship(fastest_starship, passengers_list):
    """
    Updates the < fastest_starship > dictionary by adding
    passengers and their boarding orders from the passengers_list.

    Parameters:
        fastest_starship (dict): a dictionary containing the starship's name
        and max_atmosphering_speed.
        passengers_list (list): a list of dictionaries, each containing
        information about a passenger.

    Returns:
        None
    """

    list = []
    order  = 0
    for passenger in passengers_list:
        order += 1
        cur_tupe = (passenger['name'], order);
        list.append(cur_tupe)

    fastest_starship['boarding_order'] = list


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # problem 1.2: Create a SWAPI representation of Anakin Skywalker
    base_url = 'https://swapi.py4e.com/api'
    anakin_params = {'search': 'anakin'}
    anakin = get_swapi_resource(base_url + '/people', anakin_params)['results'][0]
    print(f"\nProblem 1: Anakin Skywalker = {anakin}")

    # problem 2.3: Call get_passenger_info
    characteristics = ['name', 'height', 'mass', 'birth_year', 'homeworld', 'species']
    anakin_pilot_info = get_passenger_info(anakin, characteristics)
    print(f"\nProblem 2: anakin_pilot_info = {anakin_pilot_info}")

    # problem 3: Create passengers_list
    names = ['anakin', 'padmé', 'r2-d2', 'c-3po']
    passengers_list = []
    for name in names:
        current_passenger = get_swapi_resource(base_url + '/people', {'search':name})['results'][0]
        passenger_info = get_passenger_info(current_passenger, characteristics)
        update_passenger_info(passenger_info, 'profiles.json')
        passengers_list.append(passenger_info)
    write_json('passengers_list.json',  passengers_list)
    # problem 4: call group_passengers()
    human_droid = group_passengers(passengers_list)
    print(f"\nProblem 4: human_droid = {human_droid}")

    # problem 5: call get_starships()
    starships_list = get_starships(anakin)
    print(f"\nProblem 5: starships_list = {starships_list}")

    # problem 6: call get_fastest_starship()
    anakin_fastest_starship = get_fastest_starship(anakin)
    print(f"\nProblem 6: anakin_fastest_starship = {anakin_fastest_starship}")

    # problem 7: call board_ship()
    board_ship(anakin_fastest_starship, passengers_list)
    print(f"\nProblem 7: anakin_fastest_starship = {anakin_fastest_starship}")



if __name__ == "__main__":
    main()