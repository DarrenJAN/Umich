# SI 506: Lab Exercise 06

## This week's Lab Exercise

This week's lab exercise includes four (4) problems that focus on the dictionary, functions, and conditional statements.

## Background

For this lab, you are provided with a list of dictionaries that includes information about the elite eight teams that played in 2021 NCAA "March Madness" basketball tournament.
The dictionaries within the list contain the game the team played in, the team name, the points scored, the number of fouls, the conference that each team belongs to, and when the game was played.
You will use `for` loops, `conditional statements`, and functions to complete the problems.

```python
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
```

## 1.0 Problem 01 (3 points)

1. Implement a function called `get_teams_by_conference()` that accepts two parameters: `teams`, a list of dictionaries containing the eight teams that advanced to the quarterfinals of the tournament. `conference`, a parameter to specify a list of strings containing different conferences. This function must loop over the `elite_eight` list and return a list of strings containing the teams' names if the teams are in the specified conference(s).

2. Inside of the `main()` function, call `get_teams_by_conference()` passing to it the list argument `elite_eight` and specify the conference as `['Pac-12', 'West Coast']`. Then assign the return value to a variable called `west_coast_schools`.

:bulb: After calling this function on `elite_eight` and `['Pac-12', 'West Coast']`, the return value must match the following list:

```python
['Oregon State Beavers', 'USC Trojans', 'Gonzaga Bulldogs', 'UCLA Bruins']
```

## 2.0 Problem 02 (4 points)

1. Implement a function called `get_team_most_points()` that accepts one parameter: `teams`, a list of dictionaries containing the eight teams that advanced to the quarterfinals of the tournament. This function must loop over `elite_eight` and check the value that belongs to the key `"Score"` to find the team that scored the most points. Create an empty dictionary inside the function. Assign the team's name as a value to the key `"Name"` and assign the number of points as a value to the key `"Points"`. Return the dictionary.

2. Inside of the `main()` function, call `get_team_most_points()` passing to it the list argument `elite_eight` and assign the return value to a variable called `team_with_most_points`.

:bulb: After calling this function on `elite_eight`, the return value must match the following list:

```python
{'Name': "Gonzaga Bulldogs", 'Points': 85}
```

## 3.0 Problem 03 (5 points)

1. Implement a function called `get_final_four()` that accepts one parameter: `teams`, a list of dictionaries containing the eight teams that advanced to the quarterfinals of the tournament. Loop over `elite_eight` and check the values that belong to the key `"Game"` and `"Score"` to find the winners of each game. Create an empty dictionary inside of the function. Assign each game winner's name as the key and its score as the value to the dictionary. Return the dictionary.

2. Inside of the `main()` function, call `get_final_four()` passing to it the list `elite_eight` as the argument. Assign the return value to a variable called `final_four`.

:bulb: You can assume that the teams you need to compare are exactly adjacent to each other in the list. Consider using a range-based `for` loop to compare two teams at once. Remember that you must ensure your iterator goes to every other element.

:bulb: Remember the modulo operator can allow you to differentiate between odd and even indexes.

:bulb: After calling this function on `elite_eight`, the return value must match the following list:

```python
{'Houston Cougars': 67, 'Baylor Bears': 81, 'Gonzaga Bulldogs': 85, 'UCLA Bruins': 51}
```

## 4.0 Problem 04 (8 points)

1. Implement a function called `get_avg_fouls()` that accepts one parameter: `teams`, a list of dictionaries containing the eight teams that advanced to the quarterfinals of the tournament. Utilize the accumulator pattern to get the total number of fouls and the built-in `len()` function to count the number of teams and then calculate the average number of fouls among the elite eight. Return the average rating as a whole number.

2. Inside of the `main()` function, call `get_avg_fouls()` passing to it the dictionary argument `elite_eight`. Assign the return value to a variable called `avg_fouls`.

:bulb: After calling this function on `elite_eight`, the return value _must_ be 15.
