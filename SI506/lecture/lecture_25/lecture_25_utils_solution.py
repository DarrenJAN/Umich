# SI 506 Lecture 25

import csv
import json
import requests
from urllib.parse import urlencode, urljoin


# Constants
CACHE_FILEPATH = './stu-cache.json'
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api'
SWAPI_CATEGORES = f"{SWAPI_ENDPOINT}/"
SWAPI_FILMS = f"{SWAPI_ENDPOINT}/films/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"

# Cache
cache = {}


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


def convert_to_int(value):
    """Attempts to convert a string or a number to an int. Can also convert
    numeric strings that include a thousands separator comma (e.g., "5,000",
    "5,000,000"). If unsuccessful returns the value unchanged. Note that this
    function will return True for boolean values, faux string boolean values
    (e.g., "true"), "NaN", exponential notation, etc.

    Parameters:
        value (str|int): string or number to be converted

    Returns:
        int: if value successfully converted else returns value unchanged
    """

    try:
        return int(value.replace(',', ''))
    except:
        return value


def convert_to_list(value, delimiter=None):
    """Attempts to convert a string < value > to a list using the provided < delimiter >. Removes
    leading/trailing spaces before converting < value > to a list. If unsuccessful or an exception
    is encountered returns the < value > unchanged.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
         list: string converted to a list.
    """

    try:
        if delimiter:
            return value.strip().split(delimiter)
        else:
            return value.strip().split()
    except:
        return value


def create_cache_key(url, params=None):
    """Returns a lowercase string key comprising the passed in < url >, and, if < params >
    is not None, the "?" separator, and any URL encoded querystring fields and values.

    Example:
       url = https://swapi.py4e.com/api/people/
       params = {'search': 'Anakin Skywalker'}
       returns 'https://swapi.py4e.com/api/people/?search=anakin+skywalker'

    Parameters:
        url (str): string representing a Uniform Resource Locator (URL)
        params (dict): one or more key-value pairs representing querystring fields and values

    Returns:
        str: Lowercase "key" comprising the URL and accompanying querystring fields and values
    """

    if params:
        querystring = f"?{urlencode(params)}" # prefix '?' separator
        return urljoin(url, querystring).lower() # space replaced with '+'
    else:
        return url.lower()


def get_resource(url, params=None, timeout=10):
    """Retrieves a SWAPI resource from either the local cache or a remote endpoint.
    Delegates to the function < create_cache_key > the task of generating a key
    comprising the passed in < url > and any querystring key-pairs in < params >.
    If the resource is not stored locally < get_swapi_resource > is called to
    retrieve the resource. The (new) resource is then added to the cache before
    being returned to the caller.
    """

    key = create_cache_key(url, params)
    if key in cache.keys():
        return cache[key] # retrieve from cache
    else:
        resource = get_swapi_resource(url, params, timeout)
        cache[key] = resource # add to cache
        return resource


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
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


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
