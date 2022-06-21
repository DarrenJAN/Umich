# SI 506: Problem Set 6

## This week's Problem Set

This week's problem set will focus on dictionaries (associative arrays).

## Background

March Madness is a basketball tournament among 68 National Collegiate Athletic Association (NCAA)
Division I basketball teams. Fans create forms or brackets to keep track of teams they predict
will win and compare their predictions to others. The odds of getting all winning teams correct is
1 in about 9 quintillion. You have been provided with three files that contain information about
previous tournaments:

- `march_madness_2021.csv`: Each row contains information about a game from the 2021 championship,
    including the round the game was played in and the seeds (rankings), names, and final scores of the
    competing teams. [Source](https://www.kaggle.com/woodygilbertson/ncaam-march-madness-scores-19852021)
- `dk_predictions_2021.csv`: Each row contains the round of the game and names of the winning and
    losing teams predicted by Draft Kings in 2021.
    [Source](https://dknation.draftkings.com/2021/3/14/22330457/march-madness-predictions-2021-ncaa-tournament-picks-national-title-game)
- `championships_1985_2021.csv`: Each row contains information about a championship game between
    1985 and 2021, including the year and the seeds (rankings), names, and final scores of the
    competing teams. [Source](https://www.kaggle.com/woodygilbertson/ncaam-march-madness-scores-19852021)

## Problem 01 (15 Points)

1. Write a function called `read_csv_to_dicts` that defines four parameters:

    `filepath` (str): A filepath of a csv file to be read from.

    `encoding` (str): Name of encoding used to decode file. Has a *default value* of `utf-8`.

    `newline` (str): Replacement value for newline; *default value* is `''`.

    `delimiter` (str): Delimiter that separates row values; *default value* is `','`.

    This function should load a csv file and return its contents in a list of dictionaries,
    where each dictionary is one row from the csv file.

2. Inside `main()`, call `read_csv_to_dicts` to load `march_madness_2021.csv` and
`dk_predictions_2021.csv` and assign the return values to the variables called `games_2021` and
`dk_pred_2021`, respectively.

The `games_2021` list must contain the following elements:

```python
    [
        {'ROUND': '6', 'WSEED': '1', 'WTEAM': 'Baylor', 'WSCORE': '86', 'LSEED': '1', 'LTEAM': 'Gonzaga', 'LSCORE': '70'},
        {'ROUND': '5', 'WSEED': '1', 'WTEAM': 'Gonzaga', 'WSCORE': '93', 'LSEED': '11', 'LTEAM': 'UCLA', 'LSCORE': '90'},
        {'ROUND': '5', 'WSEED': '1', 'WTEAM': 'Baylor', 'WSCORE': '78', 'LSEED': '2', 'LTEAM': 'Houston', 'LSCORE': '59'},
        {'ROUND': '4', 'WSEED': '2', 'WTEAM': 'Houston', 'WSCORE': '67', 'LSEED': '12', 'LTEAM': 'Oregon State', 'LSCORE': '61'},
        {'ROUND': '4', 'WSEED': '1', 'WTEAM': 'Baylor', 'WSCORE': '81', 'LSEED': '3', 'LTEAM': 'Arkansas', 'LSCORE': '72'},
        ...
    ]
```

The `dk_pred_2021` list must contain the following elements:

```python
    [
        {'ROUND': '1', 'WTEAM': 'Gonzaga', 'LTEAM': 'Nofolk'},
        {'ROUND': '1', 'WTEAM': 'Missouri', 'LTEAM': 'Oklahoma'},
        {'ROUND': '1', 'WTEAM': 'Creighton', 'LTEAM': 'UCSB'},
        {'ROUND': '1', 'WTEAM': 'Virginia', 'LTEAM': 'Ohio'},
        {'ROUND': '1', 'WTEAM': 'USC', 'LTEAM': 'Drake'},
        ...
    ]
```

:bulb: Given the length of `games_2021` and `dk_pred_2021`, printing a slice with about 5 dictionaries should be sufficient for checking your work.


## Problem 02 (20 Points)

1. Create a function called `clean_row` that defines one parameter:

    `game` (dict): A dictionary containing information about *one* basketball game.

    The function contains the following helper dictionaries:

    `rounds`: Maps a numeric string to a common name for a March Madness tournament round.

    `names`: Maps the name of a team used in some datasets to a standardized name to be used across
        all datasets.

    This function must loop over the items in `game` and do the following:

    1. Use the `rounds` dictionary to convert the value of the tournament round in `game`.

    2. Use the `names` dictionary to convert the team names in `game`.

    3. Convert any numeric values in `game` to an integer.

:exclamation: This function does not include a return statement (it implicitly returns `None`).

2. Inside `main()`, iterate through `games_2021` and call the `clean_row` function
on each nested dictionary.

3. Inside `main()`, iterate through `dk_pred_2021` and call the `clean_row` function on each nested dictionary. .

The `games_2021` list must contain the following elements:

```python
    [
        {'ROUND': 'national championship', 'WSEED': 1, 'WTEAM': 'Baylor', 'WSCORE': 86, 'LSEED': 1, 'LTEAM': 'Gonzaga', 'LSCORE': 70},
        {'ROUND': 'final 4', 'WSEED': 1, 'WTEAM': 'Gonzaga', 'WSCORE': 93, 'LSEED': 11, 'LTEAM': 'UCLA', 'LSCORE': 90},
        {'ROUND': 'final 4', 'WSEED': 1, 'WTEAM': 'Baylor', 'WSCORE': 78, 'LSEED': 2, 'LTEAM': 'Houston', 'LSCORE': 59},
        {'ROUND': 'elite 8', 'WSEED': 2, 'WTEAM': 'Houston', 'WSCORE': 67, 'LSEED': 12, 'LTEAM': 'Oregon State', 'LSCORE': 61},
        {'ROUND': 'elite 8', 'WSEED': 1, 'WTEAM': 'Baylor', 'WSCORE': 81, 'LSEED': 3, 'LTEAM': 'Arkansas', 'LSCORE': 72},
        ...
    ]
```

The `dk_pred_2021` list must contain the following elements:

```python
    [
        {'ROUND': 'round of 64', 'WTEAM': 'Gonzaga', 'LTEAM': 'Norfolk State'},
        {'ROUND': 'round of 64', 'WTEAM': 'Missouri', 'LTEAM': 'Oklahoma'},
        {'ROUND': 'round of 64', 'WTEAM': 'Creighton', 'LTEAM': 'UC Santa Barbara'},
        {'ROUND': 'round of 64', 'WTEAM': 'Virginia', 'LTEAM': 'Ohio'},
        {'ROUND': 'round of 64', 'WTEAM': 'Southern California', 'LTEAM': 'Drake'}
        ...
    ]
```


## Problem 03 (15 Points)

1. Inside `main()`, initialize an accumulator list named `underdogs`. For each row from `games_2021` where
the team with the worse (higher number) ranking won a game, add a dictionary to the accumulator.
The dictionary must have the following format:

{
    < winning team name >: < winning team ranking >,
    < losing team name >: < losing team ranking >
}

The `underdogs` list must contain the following elements:

```python
    [
        {'UCLA': 11, 'Michigan': 1},
        {'Oregon State': 12, 'Loyola (Ill.)': 8},
        {'UCLA': 11, 'Alabama': 2},
        {'Syracuse': 11, 'West Virginia': 3},
        {'Oregon State': 12, 'Oklahoma State': 4},
    ...
    ]
```


## Problem 04 (20 Points)

1. Create a function called `score_game_prediction` that defines two parameters:

    `pred` (dict): Prediction of the outcome for *one* basketball game.

    `games` (list): A list of dictionaries with the outcomes of completed basketball games.

    This function contains the following helper dictionary:

    `points`: Maps the name of a round to the points earned for correctly picking a winner from that
        round

    This function *must* iterate over `games`. If the predicted game matches the round and winner
    from any of the actual games, the function returns the corresponding number of points. Otherwise,
    it returns 0.

2. Inside `main()`, use an accumulator pattern with the accumulator `total_points` and the function
`score_game_prediction` to determine the number of points that the 2021 Draft Kings bracket
scored overall. To *each row* of `dk_pred_2021`, add a column value for the points given to the
individual game prediction. The name of this new column is `BRACKETSCORE`.

The `dk_pred_2021` list must contain the following elements:

```python
    [
        {'ROUND': 'round of 64', 'WTEAM': 'Gonzaga', 'LTEAM': 'Norfolk State', 'BRACKETSCORE': 1},
        {'ROUND': 'round of 64', 'WTEAM': 'Missouri', 'LTEAM': 'Oklahoma', 'BRACKETSCORE': 0},
        {'ROUND': 'round of 64', 'WTEAM': 'Creighton', 'LTEAM': 'UC Santa Barbara', 'BRACKETSCORE': 1},
        {'ROUND': 'round of 64', 'WTEAM': 'Virginia', 'LTEAM': 'Ohio', 'BRACKETSCORE': 0},
        {'ROUND': 'round of 64', 'WTEAM': 'Southern California', 'LTEAM': 'Drake', 'BRACKETSCORE': 1},
    ...
    ]
```


## Problem 05 (20 Points)

1. Inside `main()`, read the file `championships_1985_2021.csv` and assign the return value to
the variable `championships_1985_2021`.

2. Use the `clean_row` function to edit each row of `championships_1985_2021`.

The `championships_1985_2021` list must contain the following elements:

```python
    [
        {'YEAR': 2021, 'WSEED': 1, 'WTEAM': 'Baylor', 'WSCORE': 86, 'LSEED': 1, 'LTEAM': 'Gonzaga', 'LSCORE': 70},
        {'YEAR': 2019, 'WSEED': 1, 'WTEAM': 'Virginia', 'WSCORE': 85, 'LSEED': 3, 'LTEAM': 'Texas Tech', 'LSCORE': 77},
        {'YEAR': 2018, 'WSEED': 1, 'WTEAM': 'Villanova', 'WSCORE': 79, 'LSEED': 3, 'LTEAM': 'Michigan', 'LSCORE': 62},
        {'YEAR': 2017, 'WSEED': 1, 'WTEAM': 'North Carolina', 'WSCORE': 71, 'LSEED': 1, 'LTEAM': 'Gonzaga', 'LSCORE': 65},
        {'YEAR': 2016, 'WSEED': 2, 'WTEAM': 'Villanova', 'WSCORE': 77, 'LSEED': 1, 'LTEAM': 'North Carolina', 'LSCORE': 74},
    ...
    ]
```

3. Iterate over `championships_1985_2021`. Use an accumulator dictionary `champ_count` to collect
the name of each winning team and the number of championships they won over the 16-year period.

The `champ_count` dictionary must contain the following items:

```python
    {
        'Baylor': 1,
        'Virginia': 1,
        'Villanova': 3,
        'North Carolina': 4,
        'Duke': 5,
        ...
    }
```


## Problem 06 (20 Points)

1. Create a function called `subtract_scores` that defines one parameter:

    `game` (dict): A dictionary containing information about *one* basketball game.

    This function subtracts the losing score from the winning score in the game and returns
    the (nonnegative) value.

2. Inside `main()`, loop through `championships_1985_2021` and call the `subtract_scores`
function to find the game with the largest difference between the winning and losing scores.
Assign the difference to the variable `max_diff`. Assign the dictionary of the game with this
difference to the variable `max_diff_game`.


## Problem 07 (15 Points)

1. Write a function called `write_dicts_to_csv` that defines five parameters:

    `filepath` (str): Path to target file

    `data` (list): List of dictionaries to be written to the target file

    `fieldnames` (seq): Sequence that indicates the order of the columns.

    `encoding` (str): Name of encoding used to encode the file. Has a *default value* of `utf-8`.

    `newline` (str): Specifies replacement value for newline. Has an empty string (`''`)
    as its *default value*.

    This function writes data to a csv file in filepath, where each dictionary
    is a row in the csv file.

2. In `main()`, create a variable `write_fieldnames` that has as its value a list representing the
column names in `dk_pred_2021`.

3. Call `write_dicts_to_csv` to write `dk_pred_2021` to the filepath
`stu_updated_predictions.csv` using positional arguments. Include the `write_fieldnames` variable in your function call.

:bulb: In VS Code you can compare or "diff" the file you generate (`stu_updated_predictions.csv`) against `fxt_updated_predictions.csv`.