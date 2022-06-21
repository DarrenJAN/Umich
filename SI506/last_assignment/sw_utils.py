import copy
import csv
import json
import requests

from urllib.parse import quote, urlencode, urljoin


# Constants are in ALL CAPS, no NOT change, and are GLOBAL

CACHE_FILEPATH = './stu-cache.json'
NONE_VALUES = ('', 'n/a', 'none', 'unknown')
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api'
SWAPI_CATEGORES = f"{SWAPI_ENDPOINT}/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"

# Cache
cache = {}

def convert_gravity_value(value):
    """Convert a planet's "gravity" value to a float. Removes the "standard" unit of measure if
    it exists in the string (case-insensitive check). Delegates to the function
    < convert_to_float > the task of casting the < value > to a float.

    If an exception is encountered the < value > is passed to < convert_to_none > in an attempt
    to convert the < value > to None if the < value > matches a < NONE_VALUES > item. The return
    value of < convert_to_none > is then returned to the caller.

    Parameters:
        value (obj): string to be converted

    Returns:
        float: if value successfully converted; otherwise returns value unchanged
    """

    try:
        return float(value.lower().replace('standard', ''))
    except:
        return convert_to_none(value)


def convert_to_float(value):
    """Attempts to convert the passed in < value > to a float in the try block.

    If an exception is encountered the < value > is passed to < convert_to_none > in an attempt
    to convert the < value > to None if the < value > matches a < NONE_VALUES > item. The return
    value of < convert_to_none > is then returned to the caller.

    Note that a boolean value passed to the function will be converted to a float (e.g., True
    converted to 1.0; False converted to 0.0).

    Parameters:
        value (obj): string or number to be converted

    Returns:
        obj: float if converted to number; None if value in < NONE_VALUES >; otherwise returns
             value unchanged
    """

    try:
        return float(value.replace(',', ''))
    except:
        return convert_to_none(value)



def convert_to_int(value):
    """Attempts to convert the passed in < value > to an int in the try block. Can also convert
    numbers masquerading as strings that include one or more thousand separator commas
    (e.g., "5,000,000").

    If an exception is encountered the < value > is passed to < convert_to_none > in an attempt
    to convert the < value > to None if the < value > matches a < NONE_VALUES > item. The return
    value of < convert_to_none > is then returned to the caller.

    Note that a boolean value passed to the function will be converted to an int (e.g., True
    converted to 1; False converted to 0). If a float is passed the fractional component of the
    number will be removed (e.g. 4.5 -> 4).

    Parameters:
        value (str|int): string or number to be converted

    Returns:
        obj: int if converted to number; None if value in < NONE_VALUES >; otherwise returns value
             unchanged
    """

    try:
        return int(value.replace(',', ''))
    except:
        return convert_to_none(value)


def convert_to_list(value, delimiter=None):
    """Attempts to convert the passed in < value > to a list. In the try block the < value > is
    first compared to the < NONE_VALUES > items. Leading or trailing spaces are removed from the
    passed in < value > before a case-insensitive comparison is performed between the < value >
    and the < NONE_VALUES > items. If a match is obtained None is returned to the caller.

    If the < value > is not in < NONE_VALUES > leading/trailing spaces are removed before
    the < value > is converted to a list. If a < delimiter > is provided it is employed to the
    split the < value >; otherwise the < value > is split without use of a specified delimiter.

    If a runtime exception is encountered the function returns the < value > unchanged.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
        list|None|obj: if < value > is a str returns a list unless < value > in < NONE_VALUES > in
                       which case None is returned; otherwise returns the < value > unchanged
    """

    try:
        value = value.strip()
        if value.lower() in NONE_VALUES:
            return None
        else:
            if delimiter:
                return value.split(delimiter)
            else:
                return  value.split()
    except:
        return value



def convert_to_none(value):
    """Attempts to convert the passed in < value > to < None > in the try block if the < value >
    matches any of the strings in the constant < NONE_VALUES >. Leading or trailing spaces are
    removed from the < value > before a case-insensitive comparison is performed between the
    < value > and the < NONE_VALUES > items. If a match is obtained None is returned; otherwise
    the < value > is returned unchanged.

    If a runtime exception is encountered in the except block the < value > is also returned
    unchanged.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        None: if value successfully converted; otherwise returns value unchanged
    """

    try:
        if value.strip().lower() in NONE_VALUES:
            return None 
        else:
            return value
    except:
        return value


def create_cache_key(url, params=None):
    """Returns a lowercase string key comprising the passed in < url >, and, if < params >
    is not None, the "?" separator, and any URL encoded querystring fields and values.
    Passes to the function < urllib.parse.urljoin > the optional < quote_via=quote >
    argument to override the default behavior and encode spaces with '%20' rather
    than "+".

    Example:
       url = https://swapi.py4e.com/api/people/
       params = {'search': 'Anakin Skywalker'}
       returns 'https://swapi.py4e.com/api/people/?search=anakin%20skywalker'

    Parameters:
        url (str): string representing a Uniform Resource Locator (URL)
        params (dict): one or more key-value pairs representing querystring fields and values

    Returns:
        str: Lowercase "key" comprising the URL and accompanying querystring fields and values
    """

    if params:
        return urljoin(url, f"?{urlencode(params, quote_via=quote)}").lower() # space replaced with '%20'
    else:
        return url.lower()


def get_resource(url, params=None, timeout=10):
    """Retrieves deep copies of SWAPI resources from either the local < cache > dictionary
    or from a remote API if no local copy exists. Deep copies of resources retrieved remotely
    are added to the local < cache > before the resource is returned to the caller. Deep
    copying is required to guard against possible mutatation of the cache objects when
    dictionaries representing SWAPI entities (e.g., films, people, planets, species,
    starships, and vehicles) are modified by other processes.

    Deep copying: Constructs a new compound object from a given mutable object
    (e.g., list, dict), recursively copying into it objects found in the original.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
      """

    # WARN: deep copying required to guard against mutating cache objects
    key = create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key]) # recursive copy of objects
    else:
        resource = get_swapi_resource(url, params, timeout)
        cache[key] = copy.deepcopy(resource) # recursive copy of objects
        return resource


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: This function must be implemented using a list comprehension in order to earn points.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: a list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        # data = []
        # reader = csv.reader(file_obj, delimiter=delimiter)
        # for row in reader:
        #     data.append(row)

        # return data

        #  TODO Refactor
        reader = csv.reader(file_obj, delimiter=delimiter)
        return [row for row in reader]

def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of dictionaries that
    represent the row values using the cvs.DictReader().

    WARN: This function must be implemented using a list comprehension in order to earn points.

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
        #     data.append(line) # OrderedDict() | alternative: data.append(dict(line))
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        return [line for line in reader]


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

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
