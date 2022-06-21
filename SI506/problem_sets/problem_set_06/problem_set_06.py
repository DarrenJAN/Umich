import csv

# PROBLEM 1
def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Accepts a file path for a .csv file to be read, creates a file object,
    and uses csv.DictReader() to return a list of dictionaries
    that represent the row values from the file.

    Parameters:
        filepath (str): path to csv file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


# PROBLEM 2
def clean_row(game):
    """
    Changes ROUND column values to descriptive strings,
    standardizes team
    names, and converts numeric strings to integers.

    Parameters:
        game (dict): information about one basketball game

    Returns:
        None
     """

    rounds = {'0': 'play-in round',
        '1': 'round of 64',
        '2': 'round of 32',
        '3': 'sweet 16',
        '4': 'elite 8',
        '5': 'final 4',
        '6': 'national championship'}

    names = {'BYU': 'Brigham Young',
        'E Washington': 'Eastern Washington',
        'FSU': 'Florida State',
        'Georgia State': 'Georgia Tech',
        'Loyola-Chicago': 'Loyola (Ill.)',
        'Nofolk': 'Norfolk State',
        'UCSB': 'UC Santa Barbara',
        'UConn': 'Connecticut',
        'UNCG': 'UNC Greensboro',
        'USC': 'Southern California',
        'WVU': 'West Virginia',
        }
    for key in game.keys():
        if key == 'ROUND':
            game[key] = rounds[game[key]]
        elif game[key] in names:
            game[key] = names[game[key]]
        elif game[key].isnumeric():
            game[key] = int(game[key])


# PROBLEM 4
def score_game_prediction(pred, games):
    """
    Checks whether a team won a round, as predicted.
    Returns a score based on the true outcome of the game.

    Parameters:
        pred (dict): information about the predicted outcome of a basketball game
        games (list): information about the true outcome of multiple basketball games

    Returns:
        integer: Score based on whether a winner was predicted correctly in a round;
            0 if prediction does not align with reality
     """

    points = {'round of 64': 1,
        'round of 32': 2,
        'sweet 16': 4,
        'elite 8': 8,
        'final 4': 16,
        'national championship': 32}
    for game in games:
        if pred['ROUND'] == game['ROUND']:
            if pred['WTEAM'] == game['WTEAM']:
                return points[game['ROUND']]
    return 0


# PROBLEM 6
def subtract_scores(game):
    """
    Subtracts the losing score from the winning score and returns the value.

    Parameters:
        game (dict): information about one basketball game

    Returns:
        integer: difference between winning and losing score (nonnegative)
     """
    diff = int(game['WSCORE']) - int(game['LSCORE'])
    return diff


# PROBLEM 7
def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Uses csv.DictWriter() to write a list of dictionaries to a target CSV file as row data.
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)


def main():
    """Orchestrates program workflow.

    WARN: The < global > keyword has been employed in order to change the scope of certain variables
    such as < underdogs > from local to global. This allows the auto grader to inspect the value
    assigned to each variable designated as global. After each global declaration you must assign a
    value to the variable per the assignment instructions as the following example illustrates:

    global underdogs # Do not erase
    underdogs = [] # accumulator
    ...

    Parameters:
        None

    Returns:
        None
    """

    # PROBLEM 1
    games_2021 = read_csv_to_dicts("march_madness_2021.csv")
    dk_pred_2021 = read_csv_to_dicts("dk_predictions_2021.csv")

    print(f'\nProblem 1: games_2021 =\n{games_2021[:5]}')
    print(f'\nProblem 1: dk_pred_2021 =\n{dk_pred_2021[:5]}')


    # PROBLEM 2

    for game in games_2021:
        clean_row(game)
    for game in dk_pred_2021:
        clean_row(game)
    
    print(f'\nProblem 2: games_2021 =\n{games_2021[:5]}')
    print(f'\nProblem 2: dk_pred_2021 =\n{dk_pred_2021[:5]}')

    # PROBLEM 3

    global underdogs # Do not erase
    underdogs = []
    for row in games_2021:
        cur_dict = {}
        if row['WSEED'] > row['LSEED']:
            cur_dict[row['WTEAM']] = row['WSEED']
            cur_dict[row['LTEAM']] = row['LSEED']
            underdogs.append(cur_dict)

    print(f'\nProblem 3: underdogs =\n{underdogs[:5]}')
    # PROBLEM 4

    global total_points # Do not erase
    total_points = 0
    for pred_game in dk_pred_2021:
        a = score_game_prediction(pred_game, games_2021)
        pred_game['BRACKETSCORE'] = a
        total_points += a 

    print(f'\nProblem 4: dk_pred_2021 =\n{dk_pred_2021[:5]}')
    print(f'\nProblem 4: total_points =\n{total_points}')


    # PROBLEM 5

    global champ_count # Do not erase
    champ_count = {}
    championships_1985_2021 = read_csv_to_dicts("championships_1985_2021.csv")
    for game in championships_1985_2021:
        clean_row(game)

    for champ in championships_1985_2021:
        if champ['WTEAM'] not in champ_count.keys():
            champ_count[champ['WTEAM']] = 0
        champ_count[champ['WTEAM']] +=1

    
    print(f'\nProblem 5: championships_1985_2021 =\n{championships_1985_2021[:5]}')
    print(f'\nProblem 5: champ_count =\n{champ_count}')

    # PROBLEM 6
    global max_diff
    global max_diff_game
    max_diff = 0
    max_diff_game = {}


    for game in championships_1985_2021:
        cur_score = subtract_scores(game)
        if cur_score > max_diff:
            max_diff = cur_score
            max_diff_game = game

    print(f'\nProblem 6: max_diff =\n{max_diff}')
    print(f'\nProblem 6: max_diff_game =\n{max_diff_game}')

    # PROBLEM 7
    write_fieldnames =dk_pred_2021[0].keys()
    write_dicts_to_csv('stu_updated_predictions.csv', dk_pred_2021, write_fieldnames)

if __name__ == '__main__':
    main()