# SI 506: Problem Set 5

## This week's Problem Set

This week's problem set will focus on reading and writing CSV files, creating and using functions and using the `main()` function.

## Background

This week we'll be working with election data! Specifically data from the last two general elections in South Africa. You have been given three (3) files that contain different pieces of information about South African elections.

- `election_data_2014.csv`: Each row contains the name, seats won and party information about a party from the 2014 election.
- `election_data_2019.csv`: Each row contains the name, seats won and party information about a party from the 2019 election.
- `leader_home_provinces.csv`: Each row contains the name of a party leader and their home province in South Africa.

## Problem 1 (20 Points)

1. Write a function called `read_csv` that defines two parameters:

    `filepath` (str): A filepath of a csv file to be read from.

    `encoding` (str): Name of encoding used to decode file. Has a *default value* of `utf-8-sig`.

    This function should load a csv file and return its contents in a list of lists, where each list is one row from the csv file.

2. Inside `main()`, call `read_csv` to load `election_data_2014.csv` and `election_data_2019.csv` into variables called `election_data_2014` and `election_data_2019`, respectively. Do **not** conduct any data cleaning in the `read_csv` function.

If steps 1 and 2 are implemented correctly, `election_data_2014` should look like this:

```python
    [
        ['Party', 'Seat', 'Party Info'],
        ['  African National Congress', '249', 'Centre left/JACOB Zuma'],
        ['Democratic Alliance ', '89', 'Centre/Helen zille'],
        ...
    ]
```

## Problem 2 (25 Points)

1. Create a function called `clean_data` that defines one parameter:

    `data` (list): A list of lists, each representing a party's election results.

    This function must loop over `data` (excluding the header) and perform the following operations on *each* row of data:

    1. Remove any leading or trailing whitespaces from 'Party' values.
    2. Convert 'Seats' to integer values.
    3. Split 'Party Info' into a list using the correct delimiter. Assign the **first** value from the split list to the **third** value in the row.
    4. Using a built-in `str` method, reformat the second value from the split list to have each word start with an uppercase letter followed by all lowercase letters (e.g. **N**elson **M**andela). Add this reformatted value to the end of the row.

    After the loop, assign the string 'Position' to the third value in the "header" element in `data`. Also add the string 'Party Leader' to the end of "header" element.

:exclamation: This function does not include a return statement (it implicitly returns `None`).

2. Inside `main()`, call `clean_data` on `election_data_2014` and `election_data_2019`.

If steps 1 and 2 are implemented correctly, `election_data_2014` should look like this:

```python
    [
        ['Party', 'Seat', 'Position', 'Party Leader'],
        ['African National Congress', 249, 'Centre left', 'Jacob Zuma'],
        ['Democratic Alliance', 89, 'Centre', 'Helen Zille'],
        ...
    ]
```

## Problem 3 (20 Points)

1. Create a function called `get_leader_province` that defines two parameters:

    `leader_provinces` (list): A list of lists, each containing the names of party leaders and their home provinces.

    `party_info` (list): A list containing a party's information(i.e., party name, seats, position and leader).

    This function should:
    1. Loop over the data in `leader_provinces` (exclude the header).
    2. Check if the leader's name from the current list in the loop matches the name in `party_info`.
    3. If a match is found, add the name of the province to the end of the `party_info` list.

:exclamation: This function does not have a return value associated with it (it implicitly returns `None`).

2. Inside `main()`, call `read_csv` on `leader_home_provinces.csv` and assign the returned list to a variable called `home_provinces`.

3. Add the string 'Leader Home Province' to the "header" element of `election_data_2014`. Loop over the *data* in `election_data_2014` (exclude the header) and call `get_leader_province` to add provincial data to each row.

4. Add the string 'Leader Home Province' to the "header" element of `election_data_2019`. Loop over the *data* in `election_data_2019` (exclude the header) and call `get_leader_province` to add provincial data to each row.

## Problem 4 (20 Points)

1. Create a function called `get_seats_by_province` that defines two parameters:

    `election_data` (list): A list of lists, each containing a party's information from a specific election(i.e., party name, seats, position, leader and leader home province).

    `province` (str): The name of a province.

    This function should:
    1. Initialize a variable called `province_seats` assigning it a value of zero (0).
    2. Skipping the header, loop over `election_data` and use an accumulator pattern to sum up the total number of seats won by leaders from the given province.

        :exclamation: Your accumulator pattern should be able to match province values in different cases (uppercase/lowercase/camel case).

    3. After the loop, **return** the final value of `province_seats`.

2. In `main()`, call `get_seats_by_province` passing to it as arguments `election_data_2014` and the string `'kwazulu-natal'`. Assign the returned value to a variable named `kn_seats_2014`.

3. Similarly, call `get_seats_by_province` passing to it as arguments `election_data_2019` and the string `'GAUTENG'`. Assign the returned value to a variable named `gauteng_seats_2019`.

## Problem 5 (20 Points)

1. Create a function called `get_seat_difference` that defines two parameters:

    `prev_election_data` (list): A list of lists, each containing a party's information from a specific election(i.e., party name, seats, position, leader and leader home province).

    `party_info` (list): A list containing a party's information (i.e., party name, seats, position, leader and leader home province).

    This function should:
    1. Loop over the data in `prev_election_data` (exclude the header).
    2. Check if the 'Party' from the current list in the loop matches the 'Party' in `party_info`.
    3. If a match is found, find the difference between the 'Seats' in `party_info` and the 'Seats' in the current list in the loop. **Return** the difference as the return value of this function.

2. Inside `main()`, add the string 'Seat Difference' to the end of the "header" element of `election_data_2019`. Loop over the `data` in `election_data_2019` (exclude the header), call `get_seat_difference` passing to it as arguments `election_data_2014` and the loop variable, and add the returned value to the end of each row of data.

Prior to Problem 6, your `election_data_2019` should look like:

```python

    [
        ['Party', 'Seat', 'Position', 'Party Leader', 'Leader Home Province', 'Seat Difference'],
        ['African National Congress', 230, 'Centre left', 'Cyril Ramaphosa', 'Gauteng', -19],
        ['Democratic Alliance', 84, 'Centre', 'Mmusi Maimane', 'Gauteng', -5],
        ...
    ]
```

## Problem 06 (20 Points)

1. Write a function called `write_csv` that defines five parameters:

    `filepath` (str): Path to target file (if file does not exist it will be created)

    `data` (list | tuple): Sequence to be written to the target file

    `headers` (seq): Optional header row list or tuple. Has a *default value* of `None`.

    `encoding` (str): Name of encoding used to encode the file. Has a *default value* of `utf-8-sig`.

    `newline` (str): Specifies replacement value for newline '\n'
                    or '\r\n' (Windows) character sequences. Has an empty string (`''`) as its *default value*.

    This function writes data to a csv file in filepath, where each list is a row in the csv file.

2. In `main()`, call `write_csv` using the "header" element as the header argument and the *data* (exclude the header) from `election_data_2019` to a new file called `final_election_data_2019.csv`.

    - Use `list` indexing to extract the "header" element from `election_data_2019` *inside* the function call.
    - Use the correct *keyword argument* when passing in the "header" element. Do **not** use keyword arguments for the other two arguments while calling the function.