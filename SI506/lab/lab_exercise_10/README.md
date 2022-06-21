# SI 506: Lab Exercise 10

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on using modules and the `requests` module to load data from the SWAPI API.

## Background

The Star Wars universe is comprised of a variety of different planets, each unique in its own way. In this lab exercise, we are going to look at the planets that serve as the homeworld to some popular Star Wars characters.

You have been provided with a dictionary named `hero_homeworlds` that contains the name of some popular heroes as the **keys** and the names of their homeworlds as the **values**.

```python

hero_homeworlds = {
    'luke': 'tatooine',
    'leia': 'alderaan',
    'chewbacca': 'kashyyyk',
    'han solo': 'corellia',
    'lando calrissian': 'socorro'
}

```

## 1.0 Problem 01 (4 points)

1. In `swapi_utils.py`:

    1. Assign the URL 'https://swapi.py4e.com/api' to the variable `ENDPOINT`.

    2. Write a function called `get_swapi_resource` that defines three parameters:

        * `url` (str): a url that specifies the resource.

        * `params` (dict): optional dictionary of querystring arguments; *default value* is `None`.

        * `timeout` (int): timeout value in seconds; *default value* is `10`

        This function should use the `requests` module to get the data from the SWAPI API and return the JSON interpretation of the response. Read the doc string for more information.

2. In `lab_exercise_10.py`, import `swapi_utils` as `utl` on the **second** line of the file.

## 2.0 Problem 02 (4 points)

1. Inside of the `main()`, create a new empty list called `homeworlds`.

2. Using a standard `for` loop, iterate over the **keys** of `hero_homeworlds`. Then, call `get_swapi_resource` with `ENDPOINT` and '/planets' as the URL and the correct search params to fetch the SWAPI data for each hero's home planet. Assign the data inside the results to a variable called `swapi_homeworld`. Append `swapi_homeworld` to the `homeworlds` list.

:exclamation: Remember to use the `utl` module when calling `get_swapi_resource` and when using `ENDPOINT`.

:bulb: SWAPI will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from SWAPI.

## 3.0 Problem 03 (5 points)

1. In `lab_exercise_10.py`, create a function called `create_planet` that accepts two parameters:

    * `planet` (dict): A SWAPI representation of a planet.

    * `filters` (tuple): A tuple containing the names of the planet features.

    `create_planet` creates and empty dictionary called `new_planet`. Then it loops over `planet` and `filters`. For each `planet` key that is in `filters`, the function converts the value based on the following:

    * If the *value* is numeric, convert the value to `int`. Assign the converted value to the same key in `new_planet`.

    * If the *key* is either 'climate' or 'terrain', split the string into a list of strings using the correct delimiter. Assign the converted value to the same key in `new_planet`.

    * For all other values, assign the value to the same key in `new_planet`.

2. Inside of the `main()`,

    1. Using a list comprehension, loop over for each element of `homeworlds`, using the loop variable `homeworld`. Call the `create_planet` function using `homeworld` and `planet_filters` and append the result in the list comprehension. Assign the resulting list to a variable named `clean_homeworlds`.


## 4.0 Problem 04 (4 points)

1. Using a dictionary comprehension, iterate over the `clean_homeworlds`, using the loop variable `homeworld`. For each `homeworld`, check if the value for the key 'diameter' is *at least* **11000**. If the diameter is at least 11000, then assign the name of the homeworld as a key and the homeworld as the value inside the dictionary comprehension. Assign the resulting ditionary to a variable named `large_homeworlds`.

Your `large_homeworlds` must resemble the following:

```python

{
    'Alderaan': {
        'name': 'Alderaan',
        'diameter': 12500,
        'climate': ['temperate'],
        'terrain': ['grasslands', 'mountains'],
        'population': 2000000000
        },

    'Kashyyyk': {
        'name': 'Kashyyyk',
        'diameter': 12765,
        'climate': ['tropical'],
        'terrain': ['jungle', 'forests', 'lakes', 'rivers'],
        'population': 45000000
        },

    'Corellia': {
        'name': 'Corellia',
        'diameter': 11000,
        'climate': ['temperate'],
        'terrain': ['plains', 'urban', 'hills', 'forests'],
        'population': 3000000000
        }
}

```

## 5.0 Problem 05 (3 points)

1. In `swapi_utils.py`, implement a function named `write_json` that takes the following parameters:

    * `filepath` (str): the path to the file.

    * `data` (dict)/(list): the data to be encoded as JSON and written to the file.

    * `encoding` (str): name of encoding used to encode the file. Has a default value of `'utf-8'`.

    * `ensure_ascii` (str): if `False` non-ASCII characters are printed as is; otherwise non-ASCII characters are escaped. Has a default value of `False`.

    * `indent` (int): number of "pretty printed" indention spaces applied to encoded JSON. Has a default value of `2`.

    :bulb: This should utilze json.dump to write the json to a file.

2. Inside of the `main()` function, call `write_json` with a filepath of `stu_large_homeworlds.json` using the `large_homeworlds` dictionary. The dictionary should match the `fxt_large_homeworlds.json` file provided.

:exclamation: Remember to use the `utl` module when calling `write_json`.