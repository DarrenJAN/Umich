# PROBLEM SET 08
import json
import csv


# PROBLEM 1 (10 points)
def read_csv_to_dicts(filepath, encoding='utf-8-sig', newline='', delimiter=','):
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

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = [row for row in csv.DictReader(file_obj, delimiter=delimiter)]
        return data


# PROBLEM 2 (25 points)
def clean_data(data):
    """Cleans each dictionary within the given < data > list.

    Loops over each dictionary in the < data > list, then loops over each
    dictionary's keys. If the key is either one of the specified keys with
    integer values (points or position), converts the current value to an
    integer. If the key is the key for the fastest lap, converts the minute
    and second values to milliseconds, finds the integer value for the fastest
    lap in milliseconds and assigns the value back to the fastest lap key in
    each dictionary.

    This function does not have a return value.

    Parameters:
        data (list): A list of dictionaries, each containing information
        about a driver's GP result or standing.

    Returns:
        None
    """

    for each_data in data:
        for key in each_data.keys():
            value = each_data[key]
            if key in ('points', 'position'):
                each_data[key] = int(value)
            elif key == 'fastest_lap':
                time = value.split(':')
                num = 60000 * int(time[0]) + 1000 * int(time[1]) + int(time[2])
                each_data[key] = num


# PROBLEM 3 (25 points)
def get_drivers_with_points(results):
    """Returns a dictionary with the names and points of drivers who scored
    points in the given < results > list.

    Constructs a dictionary comprehension that creates a dictionary with a
    driver name as the key and their points scored as the values, for each
    driver in the given < results > list who position was in the top 10. Uses
    the provided < points_dict > to retrieve the points associated with each
    top 10 position.

    Parameters:
        results (list): A list of dictionaries, each containing information
        about a driver's GP result.

    Returns:
        results_with_points (dict): A dictionary with the driver's names as
        keys and their respective points as values.
    """

    points_dict = {
        '1': 25,
        '2': 18,
        '3': 15,
        '4': 12,
        '5': 10,
        '6': 8,
        '7': 6,
        '8': 4,
        '9': 2,
        '10': 1,
    }

    return {driver['name']:points_dict[str(driver['position'])] for driver in results if driver['position'] <= 10}


# PROBLEM 4 (25 points)
def add_fastest_lap_point(results, drivers_with_points):
    """This function adds a point to the driver who drove the fastest single lap in a race,
    if they placed above 10th place.

    Uses an accumulator pattern to find the the driver with the shortest lap time from the
    < results > list. After the loop has completed running, uses the name of the driver with
    the shortest lap to update their points value in < drivers_with_points > by one, i.e. adds
    one (1) to their existing points value.

    Parameters:
        results (list): A list of dictionaries, each containing information
        about a driver's GP result.

        drivers_with_points (dict): A dictionary containing the name and points scored
        by each driver who scored points in a race.

    Returns:
        None
    """

    time = float('inf')
    for driver in results:
        if driver['fastest_lap'] < time:
            name = driver['name']
            time = driver['fastest_lap']
            
    drivers_with_points[name] += 1


# PROBLEM 5 (25 points)
def update_standings(standings, drivers_with_points):
    """Updates the < standings > list by adding the points from the given race < results >.

    Using a list comprehension, updates each dictionary in < standings > at
    the key 'points' with the points value retrieved from the < drivers_with_points >
    dictionary.

    Parameters:
        standings (list): A list of dictionaries, each containing information about a
        driver's standing.

        drivers_with_points (dict): A dictionary containing the name and points scored
        by each driver who scored points in a race.

    Returns:
        None
    """

    [driver.update({'points': drivers_with_points[driver['driver']]}) for driver in standings if driver['driver'] in drivers_with_points.keys()]


# PROBLEM 6 (25 points)

# HELPER FUNCTION - DO NOT ALTER
def get_points_by_team(results, team):
    """Gets the total number of points earned by a < team > from a set of
    given < results >.

    Parameters:
        results (list): A list of dictionaries, each containing information
        about a driver's GP result.

        team (string): The name of one of the teams competing in the 2022
        Formula 1 season.

    Returns:
        total_points (int): The total number of points earned by both drivers
        from the given < team >.
    """

    total_points = 0

    for row in results:
        if row['team'] == team:
            total_points += row['points']

    return total_points


def get_team_standings(results, teams):
    """Generates standings for each team based on a Grand Prix's < results >.

    Uses a list comprehension where each element is a dictionary. Each dictionary
    contains two key-value pairs. The first key, 'team', has the name of each team
    from < teams > as the value. The second key, 'points', has the total points
    scored by each team in < teams >. Utilizes the < get_points_by_team > function
    to retrieve the total points scored by each team.

    Parameters:
        results (list): A list of dictionaries, each containing information
        about a driver's GP result.

        teams (list): A list containing the names of the different teams competing
        in the 2022 Formula 1 season.

    Returns:
        team_standings (list): A list of dictonaries containing information about the
        name and total points of each team in < teams >.
    """

    return [{'team': team, 'points': get_points_by_team(results, team)} for team in teams]


# PROBLEM 7 (15 points)
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



# Entry
def main():

    # PROBLEM 1
    print('Problem 1:\n')

    race_results = read_csv_to_dicts('gp_results.csv') # TODO: Replace
    standings = read_csv_to_dicts('driver_standings_pre_GP.csv') # TODO: Replace

    print(f"race_results = {race_results}")
    print(f"standings = {standings}")

    # PROBLEM 2
    print('Problem 2:\n')
    clean_data(race_results)
    clean_data(standings)

    print(f"Problem 2:race_results = {race_results}")
    print(f"Problem 2:standings = {standings}")
    
    # PROBLEM 3
    print('Problem 3:\n')

    drivers_with_points = get_drivers_with_points(race_results) # TODO: Replace
    print(f"drivers_with_points = {drivers_with_points}")
    
    # PROBLEM 4
    print('Problem 4:\n')

    add_fastest_lap_point(race_results, drivers_with_points)
    print(f"drivers_with_points = {drivers_with_points}")

    # PROBLEM 5
    print('Problem 5:\n')

    update_standings(standings, drivers_with_points)
    print(f"standings = {standings}")
    # PROBLEM 6
    print('Problem 6:\n')

    # UNCOMMENT WHEN SOLVING PROBLEM 6
    team_names = [row['team'] for row in standings]
    constructors = list(set(team_names))

    # UNCOMMENT TO VIEW CONSTRUCTORS LIST
    print(constructors)

    team_standings = get_team_standings(standings, constructors) # TODO: Replace
    print(f"team_standings = {team_standings}")

    # PROBLEM 7
    print('Problem 7:\n')

    # UNCOMMENT WHEN SOLVING PROBLEM 7
    sorted_team_standings = sorted(team_standings, key=lambda x: (x['points'], x['team']), reverse=True)
    sorted_driver_standings = sorted(standings, key=lambda x: x['points'], reverse=True)
    write_json('stu_driver_standings_post_GP.json', sorted_driver_standings)
    write_json('stu_teams_standings_post_GP.json', sorted_team_standings)
if __name__ == "__main__":
    main()