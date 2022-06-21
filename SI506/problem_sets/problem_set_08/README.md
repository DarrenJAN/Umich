# SI 506: Problem Set 08

## This week's Problem Set

This week's problem set focuses on list and dictionary comprehensions, nested data structures, and functions.

## Background

:racing_car: &nbsp; :dash::dash::dash:

<!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:racing_car: :dash:\
&nbsp;&nbsp;&nbsp;:racing_car: :dash: -->

Last Sunday (03/20) was the start of the 2022 Formula One season. The Formula One (aka F1) competition has been around since 1950 and a season involves teams competing in a series of races known as *Grands Prix*. F1 cars are the fastest regulated racing cars in the world, with top speeds reaching around 215 mph (350 km/h)!

Throughout this assignment we will ask you to use list and dictionary comprehensions. For each implementation, we will ask you to assign a specific name to the loop variable in each comprehension. **Please** ensure that you name your loop variables appropriately for accurate grading.

Kindly refer to the code snippets below to notice the placement of loop variables in list and dictionary comprehensions:

```python
   # LIST COMPREHENSION
   [< expression > for < loop_variable > in < list/dict >]

   # DICTIONARY COMPREHENSION
   {< key >: < value > for < loop_variable > in < list/dict >}
```

## Problem 01 (10 points)

1. Write a function called `read_csv_to_dicts` that defines four parameters:

    `filepath` (str): A filepath of a csv file to be read from.

    `encoding` (str): Name of encoding used to decode file. Has a *default value* of `'utf-8-sig'`.

    `newline` (str): Replacement value for newline; *default value* is `''`.

    `delimiter` (str): Delimiter that separates row values; *default value* is `','`.

    This function should load a csv file and return its contents in a list of dictionaries,
    where each dictionary is one row from the csv file.

2. Inside of `main()`, use the `read_csv_to_dicts` function to read in the two .csv files provided:

    1. Retrieve data from `gp_results.csv` and store it in a variable named `race_results`.

    2. Retrieve data from `driver_standings_pre_GP.csv` and store it in a variable named `standings`.

:bulb: `race_results` *must* resemble the following data structure:

```python
    [{'name': 'Alexander Albon', 'team': 'Williams', 'position': '13', 'fastest_lap': '1:37:355'},
    {'name': 'Carlos Sainz', 'team': 'Ferrari', 'position': '2', 'fastest_lap': '1:35:740'},
    {'name': 'Charles Leclerc', 'team': 'Ferrari', 'position': '1', 'fastest_lap': '1:34:570'}, ...]
```

:bulb: `standings` *must* resemble the following data structure:
```python
    [{'driver': 'Max Verstappen', 'team': 'Red Bull', 'home_country': 'Netherlands', 'points': '0'},
    {'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'home_country': 'United Kingdom', 'points': '0'},
    {'driver': 'George Russell', 'team': 'Mercedes', 'home_country': 'United Kingdom', 'points': '0'}, ...]
```

## Problem 02 (25 points)

1. Implement the function named `clean_data`. The function defines one parameter:

   * `data`: A list of dictionaries, each containing information about a driver's GP result or standing.

   Review the docstring to better understand the function's expected behavior.

2. To implement this function, you need to employ a nested `for` loop and an `if-elif` statement. Iterate over the `data` list. Then iterate over each key in the nested dictionary's keys.

   * If the key is either `'points'` or `'position'`, convert the value assigned to the key to an integer.
   * If the key is `'fastest_lap'`, **split** the underlying string value into its three components (minutes, seconds, milliseconds) and convert the minute and second values to milliseconds and sum up the total lap time in **milliseconds**. The string format is `mm:ss:msms`.

   The related time conversions are:

    ```
    1 minute = 60000 milliseconds
    1 second = 1000 milliseconds
    ```

3. After implementing `clean_data`, return to the `main` function.

   1. Call the function passing it the `race_results` list.

   :bulb: Your `race_results` list __must__ resemble the list below:

   ```python
   [{'name': 'Alexander Albon', 'team': 'Williams', 'position': 13, 'fastest_lap': 97355},
   {'name': 'Carlos Sainz', 'team': 'Ferrari', 'position': 2, 'fastest_lap': 95740},
   {'name': 'Charles Leclerc', 'team': 'Ferrari', 'position': 1, 'fastest_lap': 94570}, ...]
   ```

   2. Call the function passing it the `standings` list.

   :bulb: Your `standings` list __must__ resemble the list below:

   ```python
   [{'driver': 'Max Verstappen', 'team': 'Red Bull', 'home_country': 'Netherlands', 'points': 0},
   {'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'home_country': 'United Kingdom', 'points': 0},
   {'driver': 'George Russell', 'team': 'Mercedes', 'home_country': 'United Kingdom', 'points': 0}, ...]
   ```

## Problem 03 (25 points)

1. Implement the function named `get_drivers_with_points`. The function defines one parameter:

   * `results`: A list of dictionaries, each containing information about a driver's GP result.

   Review the function's docstring for more information about the function's expected behavior.

   :exclamation: The loop variable in your dictionary comprehension **MUST** be named `driver`.

2. After implementing `get_drivers_with_points`, return to the `main` function. Call the function passing it the list `race_results` as an argument. Assign the return value to a variable named `drivers_with_points`.

## Problem 04 (25 points)

1. Implement the function named `add_fastest_lap_point`. The function defines two parameters:

   * `results`: A list of dictionaries, each containing information about a driver's GP result.
   * `drivers_with_points`: A dictionary containing the name and points scored by each driver who scored points in a race.

   Review the docstring to better understand the function's expected behavior.

2. To implement the function, use an accumulator pattern to find the the driver with the shortest lap time from the `results` list. After the fastest driver has been identified, update their points value in `drivers_with_points` by adding one (1) point to their existing points total.

   :bulb: Your accumulator pattern needs to update both the lap time and the name of the driver every time it finds a "new" shortest lap time.

3. After implementing `add_fastest_lap_point`, return to the `main` function. Call the function passing it the `race_results` list and the `drivers_with_points` dictionary.

   :bulb: After calling the function, `drivers_with_points` __must__ resemble the dictionary below:

   ```python

   {
      'Carlos Sainz': 18,
      'Charles Leclerc': 26,
      'Esteban Ocon': 6,
      'Fernando Alonso': 2,
      'George Russell': 12,
      'Kevin Magnussen': 10,
      'Lewis Hamilton': 15,
      'Valtteri Bottas': 8,
      'Yuki Tsunoda': 4,
      'Zhou Guanyu': 1
   }
   ```

## Problem 05 (25 points)

1. Implement the function named `update_standings`. The function defines two parameters:

   * `standings`: A list of dictionaries, each containing information about a driver's standing.

   * `drivers_with_points`: A dictionary containing the name and points scored by each driver who scored points in a race.

   Review the docstring to better understand the function's expected behavior.

   :bulb: This function has no return value, i.e. it returns `None`.

2. To implement this function, you need to use a list comprehension that *updates* each driver's dictionary in `standings` with their new points value from `drivers_with_points` if the name of the driver is one of the keys of the `drivers_with_points` dictionary.

   :exclamation: The loop variable in your list comprehension **MUST** be named `driver`.

3. After implementing `update_standings`, return to the `main` function. Call the function using the arguments `standings` and `drivers_with_points`.

## Problem 06 (25 points)

1. Implement the function named `get_team_standings`. The function defines two parameters:

   * `results`: A list of dictionaries, each containing information about a driver's GP result.

   * `teams`: A list containing the names of the different teams competing in the 2022 Formula 1 season.

   Review the docstring to better understand the function's expected behavior.

2. To implement this function, you need to use a list comprehension that generates a list of dictionaries. Each dictionary contains two key-value pairs:

    |Key|Value|
    |-|-|
    |'team'|Name of team|
    |'points'|Points scored by drivers of given team|

   :bulb: You must utilize the given `get_points_by_team()` function *inside* your list comprehension in order to retrieve the total points value for each team.
   
   :exclamation: The loop variable in your list comprehension **MUST** be named `team`.

3. After implementing `get_team_standings`, return to the `main` function.

   1. Uncomment the two lines containing variable assignments for `team_names` and `constructors`.
   2. Call the function using the arguments `standings` and `constructors`. Assign the return value to a variable called `team_standings`.

## Problem 07 (15 points)

1. Implement the function named `write_json`. The function defines four parameters:

   * `filepath`: A path to target file.
   * `data`: A list of dictionaries that needs to be written
   into a JSON file;
   * `encoding`: Name of encoding used to encode the file (default value = `utf-8`).
   * `indent`: An integer number of "pretty printed" indention spaces applied to encoded JSON (default value = `2`).

   Review the function's docstring for more information about the function's expected behavior.

2. After implementing `write_json`, return to the main function.
   1. Uncomment the two lines of code underneath the `print` statement that call the `sorted()` method.
   2. Call the `write_json` method with `'stu_driver_standings_post_GP.json'` as the filepath, and `sorted_driver_standings` as the data.
   3. Call the `write_json` method with `'stu_teams_standings_post_GP.json'` as the filepath and `sorted_team_standings` as the data.
