# LAB EXERCISE 06
print('Lab Exercise 06 \n')

# SETUP
elite_eight = [
    {'Game': 'Game 1', 'Team': 'Oregon State Beavers','Score': 61, 'Fouls': 20, 'Conference': 'Pac-12', 'Date': 'March 29, 2021'},
    {'Game': 'Game 1', 'Team': 'Houston Cougars', 'Score': 67, 'Fouls': 12, 'Conference': 'American Athletic', 'Date': 'March 29, 2021'},
    {'Game': 'Game 2', 'Team': 'Arkansas Razorbacks','Score': 72, 'Fouls': 18, 'Conference': 'Southeastern', 'Date': 'March 29, 2021'},
    {'Game': 'Game 2', 'Team': 'Baylor Bears', 'Score': 81, 'Fouls': 21, 'Conference': 'Big 12', 'Date': 'March 29, 2021'},
    {'Game': 'Game 3', 'Team': 'USC Trojans', 'Score': 66, 'Fouls': 13, 'Conference': 'Pac-12', 'Date': 'March 30, 2021'},
    {'Game': 'Game 3', 'Team': 'Gonzaga Bulldogs', 'Score': 85, 'Fouls': 16, 'Conference': 'West Coast', 'Date': 'March 30, 2021'},
    {'Game': 'Game 4', 'Team': 'UCLA Bruins', 'Score': 51, 'Fouls': 14, 'Conference': 'Pac-12', 'Date': 'March 30, 2021'},
    {'Game': 'Game 4', 'Team': 'Michigan Wolverines', 'Score': 49, 'Fouls': 11, 'Conference': 'Big 10', 'Date': 'March 30, 2021'}
]

# END SETUP

# Problem 01 (3 points)
def get_teams_by_conference(teams, conference):
    """
    This function returns a list of team names filtered on the passed in < conference >.

    Parameters:
        teams (list): A list of dictionaries each representing a tournament team that made it to the quarterfinals in the March Madness basketball tournament.
        conference (list): A list of strings containing one or more conference names.

    Returns:
        team_names (list): A list containing the teams' names
    """
    result = []
    for team in teams:
        if team['Conference'] in conference:
            result.append(team['Team'])
    return result

# Problem 02 (4 points)
def get_team_most_points(teams):
    """
    This function returns a dictionary representing the team that scored the most points among the teams in the list. The dictionary comprises the following key-value pairs: 'Name': < team_name >, 'Points' < points_scored >.

    Parameters:
        teams (list): A list of dictionaries each representing a tournament team that made it to the quarterfinals in the March Madness basketball tournament.

    Returns:
        team_with_most_points (dict): A dictionary containing the team's name and the number of points
    """
    result = {}
    max_points = 0
    for team in teams:
        if team['Score'] > max_points:
            max_points = team['Score']
            result['Name'] = team['Team']
            result['Points'] = team['Score']
    return result

# Problem 03 (5 points)
def get_final_four(teams):
    result = {}
    for i in range(len(teams)):
        if i % 2 == 0:
            cur = teams[i]['Score']
            next = teams[i]['Score']
            if cur > next :
                result[teams[i]['Team']] = teams[i]['Score']
            else:
                result[teams[i+1]['Team']] = teams[i+1]['Score']
    return result

# Problem 04 (8 points)
def get_avg_fouls(teams):
    sum = 0
    for team in teams:
        sum += team['Fouls']
    avg = sum/len(teams)
    return int(avg)

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")
    west_coast_schools = get_teams_by_conference(elite_eight, ['Pac-12', 'West Coast'])
    print(west_coast_schools)

    # Problem 02
    print("Problem 02:\n")
    team_with_most_points = get_team_most_points(elite_eight)
    print(team_with_most_points)

    # Problem 03
    print("Problem 03:\n")
    final_four = get_final_four(elite_eight)
    print(final_four)

    # Problem 04
    print("Problem 04:\n")
    avg_fouls = get_avg_fouls(elite_eight)
    print(avg_fouls)


if __name__ == "__main__":
    main()