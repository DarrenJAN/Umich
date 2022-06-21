# SI 506: Lab Exercise 09

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on using the `requests` module to load data from the swapi API.

## Background

For this lab, you are going to assist the main characters of "Star Wars: A New Hope" escape from the Death Star. You will need to acquire data from the swapi API for the following items and write them to a json file to simulate the ship taking off:

- The ship (the Millennium Falcon)

- The crew (Han Solo and Chewbacca)

- And the passengers (Luke, Leia, C-3PO, and R2-D2)


## 1.0 Problem 01 (5 points)

1. Write a function called `get_swapi_resource` that defines three parameters:

    * `url` (str): a url that specifies the resource.

    * `params` (dict): optional dictionary of querystring arguments; *default value* is `None`.

    * `timeout` (int): timeout value in seconds; *default value* is `10`

    This function should use the `requests` module to get the data from the swapi API and return the JSON interpretation of the response. Read the doc string for more information.

    :bulb: Check your lecture notes if you have additional questions about how this should function.

2. Inside of the `main()` function, create a variable called `swapi_millennium_falcon` and assign it the value of `get_swapi_resource` using the `ENDPOINT` variable provided and `/starships` as the url and `falcon` as the search param. API's will return more data than just the result, so make sure to extract the first value of `results` in the json you get back from the API. **This must be done in one line.**

:bulb: Remember, `params` should take a dictionary with a key (the action you are taking) and a value (the value you're searching for).


## 2.0 Problem 02 (3 points)

1. Inside of the `main()`, create a new empty dictionary called `millennium_falcon` to represent the collection of the ship, crew members, and passengers.

2. Assign `swapi_millennium_falcon` with a key of `ship` to `millennium_falcon`.


## 3.0 Problem 03 (4 points)

1. Inside of the `main()` function, call `get_swapi_resource` with a search param of `chewbacca` and assign it to a variable called `swapi_chewie`. API's will return more data than just the result, so make sure to extract the first value of `results` in the json you get back from the API. **This must be done in one line.**

:bulb: The url for this should include `/people` instead of `starships` like in Problem 01.

2. Next, call `get_swapi_resource` again, but with a search param of `han solo` and assign it to a variable called `swapi_han_solo`. API's will return more data than just the result, so make sure to extract the first value of `results` in the json you get back from the API. **This must be done in one line.**

3. Finally, create a new dictionary called `crew_members` with the following key/value pairs:

    * `pilot`: `swapi_han_solo`

    * `co-pilot`: `swapi_chewie`

Then assign that dictionary to the `millennium_falcon` dictionary with a key of `crew_members`.


## 4.0 Problem 04 (4 points)

1. Add a new key called `passengers` to `millennium_falcon` and assign it a value of an empty list.

2. Use a for loop to iterate over the `passengers` list provided at the top of the file. For each passenger, call `get_swapi_resource` for that passenger and assign it to a variable named `swapi_passenger`. API's will return more data than just the result, so make sure to extract the first value of `results` in the json you get back from the API. **This must be done in one line.** Then append `swapi_passenger` to the `passengers` list in `millennium_falcon`.


## 5.0 Problem 05 (4 points)

Now that we've loaded up the `millennium_falcon`, it's time to blast off!

1. Implement a function named `write_json` that takes the following parameters:

    * filepath (str): the path to the file

    * data (dict)/(list): the data to be encoded as JSON and written to
    the file

    * encoding (str): name of encoding used to encode the file

    * indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    :bulb: This should utilze json.dump to write the json to a file.

2. Inside of the `main()` function, call `write_json()` with a filepath of `stu_blast_off.json` using the `millennium_falcon` dictionary. The dictionary should match the `fxt_blast_off.json` file provided.

:bulb: If you are struggling with this one, check to make sure you are assigning the values to the correct keys in `millennium_falcon` without modifying the data.