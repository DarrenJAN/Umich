# SI 506: Problem Set 10

## This week's problem set

This week, we focus on modules, `try/except` blocks, and caching.
You will work on two Python files: `problem_set_10.py` and `swapi_entities.py`, where the `problem_set_10.py` file is the main workspace that imports classes and functions from `swapi_entities.py`.
The `swapi_planets.json` is the source data for this problem set.

:exclamation: **You _must_ submit both `problem_set_10.py` and `swapi_entities.py` to Gradescope in order to earn points (do not change the filenames).**

## Problem 1.0 (45 points)

### Problem 1.1 (20 points)

Implement the function `read_json()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

Import the file `swapi_entities.py` as `ent` in the beginning of the file `problem_set_10.py`.

Read the `swapi_planets.json` file into a variable called `planet_data` in `main()` in `problem_set_10.py`.

### Problem 1.2 (5 points)

Implement the function `write_json()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

### Problem 1.3 (20 points)

#### Problem 1.3.1
Implement the function `create_cache_key()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

:bulb: If params is `{'search': anakin skywalker}`, the return value should be:
    `https://swapi.py4e.com/api/people/?search=anakin+skywalker`

#### Problem 1.3.2
Implement the function `get_cache()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

#### Problem 1.3.3
Implement the function `get_resource()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

#### Problem 1.3.4
Implement the function `get_swapi_resource()` in the file `swapi_entities.py`. Review the function's docstring to better understand its expected behavior.

## Problem 2.0 (55 points)

### Problem 2.1 (10 points)
In the file `swapi_entities.py`, write a `convert_to_float()` function that uses a `try` and `except` block that attempts to convert a given value to a float. If the given value cannot be properly converted to a float, it should return the value in its original form. Review the function's docstring to better understand its expected behavior.

### Problem 2.2 (15 points)
In the file `swapi_entities.py`, write a `create_species()` function. Note that some values need to be converted to floats. See docstring for more information. Review the function's docstring to better understand its expected behavior.

### Problem 2.3 (15 points)
In the file `swapi_entities.py`, write a `create_homeworld()` function. Note that some values need to be converted to floats. See docstring for more information. Review the function's docstring to better understand its expected behavior.

### Problem 2.4 (15 points)
In the file `swapi_entities.py`, write a `convert_data()` function that converts the values associated with the `homeworld` and `species` keys to dictionaries. Review the function's docstring to better understand its expected behavior.

:exclamation: When the value is "unknown", you _must_ set it to `None` instead of converting it.

## Problem 3.0 (20 points)

Write a `create_person()` function. This function should return a filtered dictionary representation of a person with nested homeworld and species dictionaries. Review the function's docstring to better understand its expected behavior.

:exclamation: Note that in returning the dictionary literal, some values should also be converted to floats. See the Docstring for more details.

## Problem 4.0 (20 points)

In `main()`, create an empty list called `people`. Loop over the `planet_data` list. Within each dictionary in the `planet_data` list, access the list of urls mapped to the `residents` key. In a nested `for` loop, call `get_resource()` using each url in the `resident` key. Call `convert_data()` on this return value and call `create_person()` on the return value of `convert_data()`. Append the final return value to the `people` variable. 

:bulb: You will notice a difference in runtime between the first time you run this and the times after due to the cache file.

## Problem 5.0 (10 points)

In `main()`, call `write_json()` including the `people` list of dictionaries you just created and write it to a file called `full_residents.json`. 