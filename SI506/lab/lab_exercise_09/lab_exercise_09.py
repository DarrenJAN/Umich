# LAB EXERCISE 09
import json
import requests

print('Lab Exercise 09 \n')

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api'

passengers = ['luke skywalker',
            'leia organa',
            'r2-d2',
            'c-3po']

# END SETUP


# PROBLEM 01 (5 Points)

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
    if params == None:
        response = requests.get(url,timeout=timeout)
        resources = response.json() # convert message payload to dict
    else:
        response = requests.get(url,params, timeout=timeout) 
        resources = response.json() # convert message payload to dict
    return resources


# Problem 05 (4 points)
def write_json(filepath, data, encoding='utf-8', indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)


# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01 (5 points)
    print("Problem 01:\n")
    url = f"{ENDPOINT}/starships"
    swapi_millennium_falcon = get_swapi_resource(f"{ENDPOINT}/starships", {'search': 'falcon'})['results'][0]
    print(swapi_millennium_falcon)

    # Problem 02 (3 points)
    print("Problem 02:\n")
    millennium_falcon = {}
    millennium_falcon['ship'] = swapi_millennium_falcon
    print(f"millennium_falcon={millennium_falcon}")


    # Problem 03 (4 points)
    print("Problem 03:\n")
    url = f"{ENDPOINT}/people"
    swapi_chewie = get_swapi_resource(f"{ENDPOINT}/people", {'search': 'chewbacca'})['results'][0]
    swapi_han_solo = get_swapi_resource(f"{ENDPOINT}/people", {'search': 'han solo'})['results'][0]
    crew_members = {'pilot': swapi_han_solo, 'co-pilot': swapi_chewie}
    millennium_falcon['crew_members'] = crew_members
    print(f"millennium_falcon={millennium_falcon}")


    # Problem 04 (4 points)
    print("Problem 04:\n")
    millennium_falcon['passengers'] = []
    for passenger in passengers:
        swapi_passenger = get_swapi_resource(f"{ENDPOINT}/people", {'search': passenger})['results'][0]
        millennium_falcon['passengers'].append(swapi_passenger)
    
    #Problem 05 (4 points)
    print("Problem 05:\n")
    write_json('stu_blast_off.json', millennium_falcon)

if __name__ == "__main__":
    main()
