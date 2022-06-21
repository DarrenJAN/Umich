# SI 506: Problem Set 09

## This week's Problem Set

This week's problem set focus on the [Star Wars API (SWAPI)](https://swapi.py4e.com/about), the
requests module, and JSON objects.

## Background

In the film
[Episode II Attack of the Clones](https://starwars.fandom.com/wiki/Star_Wars:_Episode_II_Attack_of_the_Clones?so=search),
Obi-Wan overhears a meeting between Count Dooku and the leaders of the commerce guilds, and learns
that they are behind the separatist movement and have built up a new droid army. Obi-Wan transmits
his findings to the Council, relayed by way of Anakin and Padmé's ship, though he is surrounded by
droids and captured before he can finish his report. Anakin and Padmé decided to make their way
there to rescue Obi-Wan.

In this problem set, we will help Anakin and Padme and their droids board their fastest ship to save
Obi-Wan!

:bulb: You have been provided with two helper functions: `read_json` and `write_json`. You will need
to use the functions in the later problems.

## Problem 01 (15 points)

__Task__: Implement a function that can initiate an HTTP GET request to the SWAPI API to return a
representation of a resource.

1. Implement a function called `get_swapi_resource` that accepts two parameters: `url`, a URL that
   provides information about entities in the Star Wars universe; `params`, an optional dictionary
   of querystring arguments (default value is `None`). Review the docstring to better understand the
   function's expected behavior.

    :bulb: You need to utilize the `.get()` method from the `requests` library to access data with
    the `url` and `params` given, if any.

2. After implementing `get_swapi_resource`, return to the main function:
    1. Create a variable called `base_url`. Assign the string `'https://swapi.py4e.com/api'` to this
       variable. We will build on this root URL to get data from SWAPI.
    1. Create a variable called `anakin_params`. Assign the dictionary `{'search': 'anakin'}` to
       this variable.
    1. Call the `get_swapi_resource` function. Using the variables above, get information about
       *Anakin Skywalker*. Access the first element of the `results` key. Assign this dictionary to
       a variable named `anakin`.

   <br />

    Your `anakin` dictionary __must__ include the following key-value pairs:

    ```python
       {'name': 'Anakin Skywalker',
       'height': '188',
       'mass': '84',
       'hair_color': 'blond',
       'skin_color': 'fair',
       'eye_color': 'blue',
       'birth_year': '41.9BBY',
       'gender': 'male',
       'homeworld': 'https://swapi.py4e.com/api/planets/1/',
       'films': ['https://swapi.py4e.com/api/films/4/',
                'https://swapi.py4e.com/api/films/5/',
                'https://swapi.py4e.com/api/films/6/'],
       'species': ['https://swapi.py4e.com/api/species/1/'],
       'vehicles': ['https://swapi.py4e.com/api/vehicles/44/',
                    'https://swapi.py4e.com/api/vehicles/46/'],
       'starships': ['https://swapi.py4e.com/api/starships/39/',
                    'https://swapi.py4e.com/api/starships/59/',
                    'https://swapi.py4e.com/api/starships/65/'],
       'created': '2014-12-10T16:20:44.310000Z',
       'edited': '2014-12-20T21:17:50.327000Z',
       'url': 'https://swapi.py4e.com/api/people/11/'
    }
    ```

## Problem 02 (25 points)

__Task__: Implement a function that can generate a dictionary representing a passenger by extracting
the key-value pairs from the SWAPI representation of the passenger.

1. Implement a function called `get_passenger_info` that accepts two parameters: `passenger`, the
   SWAPI representation of a passenger; `characteristics`, a list of strings representing a
   passenger's characteristics. Review the docstring to better understand the function's expected
   behavior.

2. To implement this function, you need to initialize an empty dictionary. Iterate over the keys in
   the `passenger` dictionary. Add the corresponding key-value pair in `passenger` to the initialized
   dictionary if the key is in the `characteristics` list. If the key is 'homeworld' or 'species',
   utilize the `get_swapi_resource` function to get the corresponding names of the homeworld and
   species as the values for the keys.

3. After implementing `get_passenger_info`, return to the main function:
    1. Create a variable called `characteristics`. Assign the list
       `['name', 'height', 'mass', 'birth_year', 'homeworld', 'species']` to this variable.
    1. Call the `get_passenger_info` function. Using the variables `anakin` and `characteristics`,
       get a dictionary representing *Anakin Skywalker*. Since Anakin is the pilot, you should
       assign this dictionary to a variable named `anakin_pilot_info`.

   <br />

   Your `anakin_pilot_info` dictionary __must__ include the following key-value pairs:

   ```python
   {'name': 'Anakin Skywalker', 'height': '188', 'mass': '84', 'birth_year': '41.9BBY', 'homeworld': 'Tatooine', 'species': 'Human'}
   ```

## Problem 03 (25 points)

__Task__: Implement a function that can update the dictionary representing a passenger by adding the
key-value pairs from the `profiles.json` file.

1. Implement a function called `update_passenger_info` that accepts two parameters: `passenger_info`,
   the return value from the function `get_passenger_info`; `filepath`, a path to the JSON file.
   Review the docstring to better understand the function's expected behavior.

2. To implement this function, you __must__ delegate to the function `read_json` the task of
   returning a dictionary from reading a JSON file. Then iterate over the dictionary's keys. If the
   key is in the value of `passenger_info['name']` (case-insensitive comparison), add the key's
   corresponding value to the `passenger_info` dictionary.

3. After implementing `update_passenger_info`, return to the main function:
    1. Create a variable called `names`. Assign the list `['anakin', 'padmé', 'r2-d2', 'c-3po']` to
       this variable.
    2. Initialize an empty list named `passengers_list`
    3. Implement a for loop to iterate over the `names` list you just created. Inside the loop, do
       the following:

        1. call `get_swapi_resource` function and pass it two arguments: the concatenated string of
           `base_url` and `'/people'`; the querystring `{'search': name}`. Access the first element
           of the `results` key from the return value of the `get_swapi_resource`. Assign this
           dictionary to a variable named `passenger`.

        2. call `get_passenger_info` function passing it `passenger` and `characteristics`. Assign
           the return value to a variable called `passenger_info`.

        3. call `update_passenger_info` function passing it `passenger_info` and `"profiles.json"`.

        4. add `passenger_info` to the `passengers_list` using a built-in list method.

    4. Call the function `write_json` and pass to it as arguments the filepath `passengers_list.json`,
       the `passengers_list`.

    :bulb: Compare your output file to the test fixture file `fxt-passengers_list.json`. Both files
    _must_ match, line for line, and character for character.

## Problem 04 (20 Points)

__Task__: Now we have a list of passengers' information. We want to split passengers into two groups
based on their species (i.e., human, droid). Implement a function that generates a dictionary that
has two key-value pairs. The keys are `'human'` and `'droid'` and the values are the corresponding
lists of the passengers.

1. Implement a function called `group_passengers` that accepts a single parameter: `passengers_list`,
   a list of dictionaries each containing information about a passenger. Review the docstring to
   better understand the function's expected behavior.

2. To implement this function, you need to initialize two empty lists named `human_passengers`,
   `droid_passengers` and one empty dictionary named `passenger_groups`. Then utilize a for loop to
   iterate over the `passengers_list`. If the passenger's species is human, add the passenger's
   information to the `human_passengers` list; otherwise, add the passenger's information to the
   `droid_passengers` list. Add the keys `'human'`, `'droid'` and the corresponding values
   `human_passengers`, `droid_passengers` to the dictionary `passenger_groups`.

3. After implementing `group_passengers`, return to the main function. Call the function passing it
   `passengers_list`. Assign the return value to a variable named `human_droid`.

   Your `human_droid` __must__ look like the dictionary below:

   ```python
   {
       'human': [
           {'name': 'Anakin Skywalker', 'height': '188', 'mass': '84', 'birth_year': '41.9BBY', 'homeworld': 'Tatooine', 'species': 'Human', 'mother': 'Shmi Skywalker', 'father': None, 'identity': 'Jedi Knight', 'nickname': 'Ani'},
           {'name': 'Padmé Amidala', 'height': '185', 'mass': '45', 'birth_year': '46BBY', 'homeworld': 'Naboo', 'species': 'Human', 'mother': 'Jobal Naberrie', 'father': 'Ruwee Naberrie', 'identity': 'Senator', 'nickname': 'Queen Amidala'}],
       'droid': [
           {'name': 'R2-D2', 'height': '96', 'mass': '32', 'birth_year': '33BBY', 'homeworld': 'Naboo', 'species': 'Droid', 'model': 'R2 series', 'class': 'Astromech Droid', 'sensor_color': ['Black']},
           {'name': 'C-3PO', 'height': '167', 'mass': '75', 'birth_year': '112BBY', 'homeworld': 'Tatooine', 'species': 'Droid', 'model': '3PO-series', 'class': 'Protocol Droid', 'sensor_color': ['Yellow', 'Red']}]
   }
   ```

## Problem 05 (20 Points)

__Task__: Implement a function that creates a list of dictionaries, each containing only the very
basic information about a starship (i.e., name and max_atmosphering_speed)

1. Implement the function named `get_starships` that accepts a single parameter: `person`, a SWAPI
   representation of a person that has piloted the starships. Given the SWAPI representation of a
   person, access the starships' URLs. Iterate over the URLs. Delegate to the function
   `get_swapi_resource` the task of finding the starships' information. Use the starship's name, max atmosphering speed, and maximum passenger capacity as the values to a dictionary with the keys `'name'`, `'max_atmosphering_speed'`, and `'passengers'`, respectively. Add the dictionary to a list. Return the list to the caller.

2. To implement this function, you need to do the following:

    1. Initialize an empty list named `starships_list`.

    2. Access the URLs of a person's starships and assign it to a variable named `starships_urls`.

    3. Iterate over the `starships_urls`. Inside the loop, initialize an empty dictionary
       `starship_dict` and delegate to the function `get_swapi_resource` the task of finding the
       SWAPI representation of a starship. Then you add the keys `'name'`, `'max_atmosphering_speed'`, `'passengers'`
       and the corresponding values (i.e., starship's name, max atmosphering speed and maximum passenger capacity) to
       the `starship_dict`. Add the `starship_dict` to the `starships_list` using a built-in list
       method.

    4. After exiting the loop, return the `starships_list` to the caller.

3. After implementing `get_starships`, return to the main function. Call the function passing it
   the variable `anakin`. Assign the return value to a variable named `starships_list`.

   Your starships_list __must__ resemble the list below:

   ```python
   [
       {
           'name': 'Naboo fighter',
           'max_atmosphering_speed': '1100',
           'passengers': '0'
           },
       {
           'name': 'Trade Federation cruiser',
           'max_atmosphering_speed': '1050',
           'passengers': '48247'
           },
       {
           'name': 'Jedi Interceptor',
           'max_atmosphering_speed': '1500',
           'passengers': '0'
           }
   ]
   ```

## Problem 06 (20 points)

__Task__: To save Obi-Wan, we need to take the fastest starship to get to Geonosis. So we are going
to implement a function that can help us find the fastest starship among the starships we got from
the function `get_starships`

1. Implement the function named `get_fastest_starship` that accepts a single parameter: `person`, a
   SWAPI representation of a person. Then we __must__ delegate to the function `get_starships` the
   task of finding all the starships that a given person has piloted previously. Iterate over the
   starships to find the one with the highest max atmospheric speed and the capacity to carry at
   least three passengers. Review the docstring to better understand the function's expected
   behavior.

2. After implementing `get_fastest_starship`, return to the main function. Call the function passing
   it the variable `anakin`. Assign the return value to a variable named `anakin_fastest_starship`.

## Problem 07 (25 points)

__Task__: The last step is to board all passengers to the fastest starship that we found from
Problem 06. Implement a function that can add passengers from the `passengers_list` to the fastest
starship.

1. Implement the function named `board_ship` that accepts two parameters: `fastest_starship`, a
   dictionary containing the starship's name and its speed; `passengers_list`, a list of
   dictionaries, each containing information about a passenger. This function iterates the
   `passengers_list`, organizing each passenger's name and iteration count (starting from 1) as a
   tuple, adding the tuple to a list, then mapping the list to the dictionary
   `fastest_starship['boarding_order']`.

2. To implement this function, you need to do the following:

    1. Initialize an empty list named `order`.

    2. Iterate over the `passengers_list` to extract the passenger name and the current iteration
       count starting from 1. Put the passenger name and the count in a tuple and append it to the
       `order` list.

        :bulb: You need to utilize the built-in `enumerate` function to solve this problem.

    3. Assign the `order` list to `fastest_starship['boarding_order']`.

3. After implementing `board_ship`, return to the main function. Call the function passing it the
   variable `anakin_fastest_starship` and `passengers_list`.

   :bulb: Now your `anakin_fastest_starship` __must__ look like the dictionary below:

   ```python
   {'name': 'Jedi Interceptor', 'max_atmosphering_speed': '1500', 'boarding_order': [('Anakin Skywalker', 1), ('Padmé Amidala', 2), ('R2-D2', 3), ('C-3PO', 4)]}
   ```
