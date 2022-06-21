# SI 506 Lecture 24

import copy
from urllib.parse import urljoin, urlencode

# import lecture_24_utils_solution
import lecture_24_utils_solution as utl

# from lecture_24_utils_solution import (
#     convert_data, convert_to_float, convert_to_int,
#     SWAPI_ENDPOINT, SWAPI_CATEGORES, SWAPI_FILMS, SWAPI_PEOPLE, SWAPI_PLANETS,
#     SWAPI_SPECIES, SWAPI_STARSHIPS, SWAPI_VEHICLES, read_json, write_json
#     ) # (...) permits statement to be expressed accross multiple lines

# from lecture_24_utils_solution import *


def create_person(data):
    """Returns a new dictionary representation of a person from the passed in
    < data >. Calls < utl.get_swapi_resource() > to retrieve species data if
    cached data is not available.

    Type conversions:
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        species

    Parameters:
        data (dict): source data

    Returns:
        dict: new person dictionary
    """

    if data.get('species'):
        species_data = utl.get_resource(data['species'][0]) # checks cache
        species = create_species(species_data) # trim
    else:
        species = None

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'birth_year': data.get('birth_year'),
        'species': species
        }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'classification': data.get('classification'),
        'designation': data.get('designation'),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'language': data.get('language')
    }


def main():
    """Entry point for the script.

    Paramters:
        None

    Returns:
        None
    """

    # 1.0 MODULES

    # 1.3 GET MODULE NAME

    module_name = utl.__name__

    print(f"\n1.3: utl module name = {module_name}")


    # 1.4 IMPORTING MODULES ACCESS MODULE DEFINITIONS AND STATEMENTS

    # Get the SWAPI representation of the ice planet Hoth

    # Unaliased module
    # import lecture_24_utils_solution
    # response = lecture_24_utils_solution.get_swapi_resource(lecture_24_utils_solution.SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.1.1: SWAPI Planet Hoth={swapi_hoth}")

    # Aliased module
    # import lecture_24_utils_solution as utl
    # response = utl.get_swapi_resource(utl.SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.1.2: SWAPI Planet Hoth={swapi_hoth}")


    # Import module names directly using the < from > keyword
    # from lecture_24_utils_solution import get_swapi_resource, SWAPI_PLANETS
    # response = get_swapi_resource(SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.1.3: SWAPI Planet Hoth={swapi_hoth}")

    # Assign aliases to imported names
    # from lecture_24_utils_solution import get_swapi_resource as get, SWAPI_PLANETS as url
    # response = get(url, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.1.4: SWAPI Planet Hoth={swapi_hoth}")

    # 1.5 BUILT-IN DIR() FUNCTION

    utl_names = dir(utl)

    print(f"\n1.2 utl module's names = {utl_names}")


    # 2.0 TRY-EXCEPT STATEMENTS
    int_keys = ('diameter', 'orbital_period', 'rotation_period', 'surface_water')

    # Membership test
    hoth_v1 = utl.read_json('./fxt-hoth_v1.json')
    for key, val in hoth_v1.items():
        if key in int_keys:
            hoth_v1[key] = int(val)

    print(f"\n2.0.1 Hoth convert vals = {hoth_v1}")

    hoth_v2 = utl.read_json('./fxt-hoth_v2.json')

    # Membership test
    # WARN: Triggers TypeError
    # int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

    # TODO Uncomment
    # for key, val in hoth_v2.items():
    #     if key in int_keys:
    #         hoth_v2[key] = int(val)

    # print(f"\n2.0.2 Hoth int vals = {hoth_v2}")

    # Generic try-except (str -> int)
    for key, val in hoth_v2.items():
        hoth_v2[key] = utl.convert_to_int(val)

    # Alternative structure (handling multiple conversions)
    # for key, val in hoth_v2.items():
    #     if key in int_keys:
    #         hoth_v2[key] = utl.convert_to_int(val)
    #     elif key in some_type_keys:
    #         ...
    #     elif key == some_key:
    #         ...
    #     else:
    #         ...

    print(f"\n2.0.3 Hoth convert vals = {hoth_v2}")

    # Write to file
    utl.write_json('stu-hoth.json', hoth_v2)


    # 3.0 CACHING

    people = (
        'Obi-Wan Kenobi',
        'Luke Skywalker',
        'Leia Organa',
        'Han Solo',
        'Chewbacca',
        'Lando Calrissian',
        'Poe Dameron',
        'Finn',
        'Rey'
    )

    # Note use of the helper function < create_person >
    swapi_people = []
    for person in people:
        response = utl.get_resource(utl.SWAPI_PEOPLE, {'search': person})
        swapi_person = response['results'][0]
        swapi_person = create_person(swapi_person) # trim
        swapi_people.append(swapi_person)


    # UGLY: How to utilize the cache without implementing < get_resource > or
    # using the helper functions < create_person > or < create_specied >

    # cache_hits = 0
    # cache_misses = 0
    # for person in people:
    #     # Generate key
    #     person_search_key = utl.create_cache_key(utl.SWAPI_PEOPLE, {'search': person})

    #     # Check cache
    #     if person_search_key in utl.cache.keys():
    #         cache_hits += 1
    #         # Get person from cached response
    #         swapi_person = utl.cache[person_search_key]['results'][0] # access list
    #     else:
    #         cache_misses += 1
    #         # Issue HTTP GET and cache response
    #         response = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': person})
    #         utl.cache[person_search_key] = copy.deepcopy(response) # contains nested dicts/lists

    #         # Access Person and species URL
    #         swapi_person = response['results'][0]
    #         species_url = swapi_person['species'][0]

    #         # Check cache
    #         if species_url in utl.cache.keys():
    #             cache_hits += 1
    #             swapi_person['species'] = utl.cache[species_url]
    #         else:
    #             cache_misses += 1
    #             response = utl.get_swapi_resource(species_url) # no params
    #             utl.cache[species_url] = copy.deepcopy(response) # contains nested dicts/lists

    #             # Update person with species dict
    #             swapi_person['species'] = response

    #     swapi_people.append(swapi_person)

    # # Cache hits/misses
    # max_calls = cache_hits + cache_misses
    # print(f"\nCache hits = {cache_hits} ({cache_hits/max_calls * 100:.2f}%); "
    #       f"Cache misses = {cache_misses} ({cache_misses/max_calls * 100:.2f}%)")

    # Write to file
    utl.write_json('stu-cache.json', utl.cache)
    utl.write_json('stu-swapi_people.json', swapi_people)


if __name__ == '__main__':
    main()
