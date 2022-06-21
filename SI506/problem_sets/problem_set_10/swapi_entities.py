import json
import requests
from urllib.parse import urljoin, urlencode

CACHE_NAME = 'cache.json'

# Problem 1.1
def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# Problem 1.2
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """
    This function dumps the JSON object in the dictionary `data` into a file on
    `filepath`.
    Parameters:
        filepath (string): The location and filename of the file to store the JSON
        data (dict): The dictionary that contains the JSON representation of the objects.
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

# Problem 1.3.1
def create_cache_key(url, params=None):
    """ Returns a unique cache key value based on the url and params. If the params value is left as None, just returns the url in lowercase.
    If the params parameter contains values, this function starts off with a querystring variable containing just a '?' and uses urlencode to
    replace any spaces in the params value with a '+'. Then, the function returns the return value of urljoin between the url and updated querystring.

    Parameters:
        url (str): url that specifies resource.
        params (dict): an optional dictionary of querystring arguments. Default value is None.

    Returns:
        str: unique and referencable querystring
    """
    if params:
        querystring = f"?{urlencode(params)}" # prefix '?' separator
        return urljoin(url, querystring).lower() # space replaced with '+'
    else:
        return url.lower()

# Problem 1.3.2
def get_cache(filepath):
    """ Tries to read the cache file, if it contains anything. If it doesn't contain any information, it returns an empty dictionary.

    Parameters:
        filepath (str): file path to cache file.

    Returns:
        dict/list: dict or list representation of the decoded cache file object.
    """
    cache = {}
    try:
        cache =  read_json(filepath)
        return cache
    except:
        return cache

# Problem 1.3.3
def get_resource(filepath, url, params=None, timeout=10):
    """
    Gets the cache and uses create_cache_key function to generate the unique referencable value for the desired value.
    If the key already exists in the cache, retrieves the value from the cache and returns it. If not, makes a call to 
    SWAPI and stores the value from the API with the unique key in the cache file and writes to the cache file.

    Parameters:
        filepath (str): filepath to cache file
        url (str): url that specifies the resource
        params (dict): an optional dictionary of querystring arguments. Default value is none.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    cache = get_cache(filepath)
    key = create_cache_key(url, params)
    if key in cache.keys():
        return cache[key] # retrieve from cache
    else:
        resource = get_swapi_resource(url, params, timeout)
        cache[key] = resource # add to cache
        return resource

# Problem 1.3.4
def get_swapi_resource(url, params=None, timeout=10):
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
        response = requests.get(url,timeout=timeout)
        resources = response.json() # convert message payload to dict
    else:
        response = requests.get(url,params, timeout=timeout) 
        resources = response.json() # convert message payload to dict
    return resources

# Problem 3.1.2
def convert_to_float(value):
    """Attempts to convert a string or a number < value > to a float. If unsuccessful or an
    exception is encountered returns the < value > unchanged. Note that this function will
    return True for boolean values, faux string boolean values (e.g., "true"), "NaN", exponential
    notation, etc.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        float: if value successfully converted; otherwise returns value unchanged
    """
    try:
        return float(value)
    except:
        return value


def create_species(species):
    """Creates a cleaned species dictionary from SWAPI.

    Parameters:
        species (dict): representation of a species from SWAPI.

    Type Conversions:
        average_height(str->float)
        average_lifespan(str->float)

    Key Order:
        name
        classification
        average_height
        designation
        average_lifespan
        language
        url

    Returns:
        dictionary literal: filtered readable version of species dictionary.
    """

    return {
        'name': species.get('name'),
        'classification': species.get('classification'),
        'average_height': convert_to_float(species.get('average_height')),
        'designation': species.get('designation'),
        'average_lifespan': convert_to_float(species.get('average_lifespan')),
        'language': species.get('language'),
        'url': species.get('url')
    }


def create_homeworld(homeworld):
    """ Returns a filtered homeworld dictionary from the SWAPI representation of a planet.

    Parameters:
        homeworld (dict): SWAPI representation of a planet.

    Type Conversions:
        rotation_period(str->float)
        diameter(str->float)
        population(str->float)

    Key Order:
        name
        rotation_period
        diameter
        climate
        population
        url

    Returns:
        dictionary literal: filtered readable version of planet dictionary.
    """
    return {
        'name': homeworld.get('name'),
        'rotation_period': convert_to_float(homeworld.get('rotation_period')),
        'diameter': convert_to_float(homeworld.get('diameter')),
        'climate': homeworld.get('climate'),
        'population': convert_to_float(homeworld.get('population')),
        'url': homeworld.get('url')
    }

# Problem 3.2
def convert_data(person, planet_data):
    """Helper function that converts specific string values of the person dictionary.
    Remember to set the value to None when the string is "unknown"
    (when the keys are n/a, none, or unknown) in any string values within the person dictionary.
    Retrieves homeworld information from planet_data
    and species information from the cache or SWAPI in order to convert urls to dictionaries
    by using create_homeworld() and create_species().

    Type conversions:
        homeworld (str->dict)
        species (list->dict)

    Parameters:
        dict: dictionary of a person
        planet_data: dictionary of planets read in from swapi_planets.json

    Returns:
        dict: dictionary of a person with necessary values converted
    """
    for key, value in person.items():
        if value == 'n/a' or value == 'none' or value == 'unknown':
            person[key] = None

    species_urls = person['species']
    if len(species_urls) != 0:
        species_url = species_urls[0]
        get_resource_return = get_resource(CACHE_NAME, species_url)
        person['species'] = create_species(get_resource_return)

    if person['homeworld'] != None:
        for planet in planet_data:
            if person['homeworld'] == planet['url']:
                person['homeworld'] = create_homeworld(planet)
                break

    return person


# Problem 4.0
def create_person(person):
    """Returns a filtered person dictionary from the SWAPI representation of a person.

    Parameters:
        person (dict): representation of a converted person dictionary from SWAPI.

    Type Conversions:
        height_cm (str->float)
        mass_kg(str->float)

    Key Order:
        name
        height_cm
        mass_kg
        birth_year
        homeworld
        species

    Returns:
        dict: filtered readable version of person dictionary
    """
    return {
        'name': person.get('name'),
        'height_cm': convert_to_float(person.get('height')),
        'mass_kg': convert_to_float(person.get('mass')),
        'birth_year': person.get('birth_year'),
        'homeworld': person.get('homeworld'),
        'species': person.get('species'),
    }