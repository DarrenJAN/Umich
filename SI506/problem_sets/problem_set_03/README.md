# SI 506: Problem Set 03

## This week's Problem Set

This week's problem set will focus on conditional statements, definite and indefinite iterations, and the `break` statement. Some topics from previous sections (e.g., methods and indexing) are also included.

## Background
Each year, China has seven public holidays enjoyed by all citizens: New Year, the Spring Festival (Chinese New Year), the Qingming Festival, Labor Day, the Dragon Boat Festival, the Mid-Autumn Festival, and National Day. The Spring Festival is the biggest holiday in China. For this problem set, you are provided with two nested lists named `chinese_holidays` and `activities`.

The list `chinese_holidays` contains several lists. Each list inside of `chinese_holidays` contains the holiday name, the holiday date, the number of days that people can take off from work for that holiday, and whether it is an official public holiday. The list `activities` contains different activities that people in China would like to do on various holidays.

```python
chinese_holidays = [
    ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
    ["New Year's Day", '2022-01-01', '3 days off', False],
    ['Spring Festival', '2022-02-01', '7 days off', True],
    ['Lantern Festival', '2022-02-15', '0 days off', False],
    ['Qingming Festival', '2022-04-05', '3 days off', True],
    ['Labor Day', '2022-05-01', '5 days off', True],
    ['Dragon Boat Festival', '2022-06-03', '3 days off', True],
    ['Qixi Festival', '2022-08-04', '0 days off', True],
    ['Mid-Autumn Festival', '2022-09-10', '3 days off', True],
    ['National Day', '2022-10-01', '7 days off', False],
    ['Double Ninth Festival', '2022-10-04', '0 days off', True]
]

activities = [
    ["New Year's Day", 'Decorating Houses | Eating Dumplings'],
    ['Spring Festival', 'Exchanging Red Envelopes | Family Reunion Dinner'],
    ['Lantern Festival', 'Watching Lanterns | Eating Tangyuan'],
    ['Qingming Festival', 'Tomb Sweeping | Spring Outing'],
    ['Labor Day', 'Visiting Tourist Spots | Shopping'],
    ['Dragon Boat Festival', 'Dragon Boat Racing | Eating Zongzi'],
    ['Qixi Festival', 'Dating | Shopping'],
    ['Mid-Autumn Festival', 'Eating Mooncakes | Family Reunion Dinner'],
    ['National Day', 'Military Parade | Visiting Tourist Spots'],
    ['Double Ninth Festival', 'Climbing Mountain | Eating Chongyang Cakes']
]
```
### Problem 01 (15 Points)

As you may notice, the list `chinese_holidays` has some data-entry errors. Some of the holidays shown in the list are official public holidays, but it is recorded as `False`. And some of them are not public holidays, but it is recorded as `True`. So we need to clean our data before moving on to perform some calculations later.

The rule that we need to follow to clean our data is this: if the number of days that people can take time off from work is greater than 0, then it is a public holiday. Otherwise, it is not a public holiday but just one of the traditional Chinese holidays.

1. Using a `for` loop, iterate over each list element in `chinese_holidays` ignoring the "header" element.

    :bulb: You need to utilize a list slicing notation to access all sublists except the "header".

2. In the loop, access the number of days off from each list and convert the string to an integer. For example, '3 days off' should be replaced by 3.

3. In the loop, check whether the number of days off in each list is 0. If it is 0, change the last element in that list to `False`. Otherwise, change it to `True`.

After you clean the data, the `chinese_holidays` *must* look like the nested list below:

```python
    [
        ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
        ["New Year's Day", '2022-01-01', 3, True],
        ['Spring Festival', '2022-02-01', 7, True],
        ['Lantern Festival', '2022-02-15', 0, False],
        ['Qingming Festival', '2022-04-05', 3, True],
        ['Labor Day', '2022-05-01', 5, True],
        ['Dragon Boat Festival', '2022-06-03', 3, True],
        ['Qixi Festival', '2022-08-04', 0, False],
        ['Mid-Autumn Festival', '2022-09-10', 3, True],
        ['National Day', '2022-10-01', 7, True],
        ['Double Ninth Festival', '2022-10-04', 0, False]
    ]
```

### Problem 02 (15 points)

Using a `for` loop and a conditional statement, calculate how many official public holidays are in `chinese_holidays` and assign the value to the variable named `num_holidays`.

1. Initialize a numerical variable called `num_holidays`.

2. Using a `for` loop, iterate over each list in `chinese_holidays` ignoring the "header" element.

3. In the loop, check whether each holiday is an official public holiday. If it is an official public holiday, increment the value of `num_holidays` by 1.


### Problem 03 (20 points)
Using a `for` loop and conditional statements, assign the name of each official public holiday to a list called `public_holidays` and the others to a list called `other_holidays`.

1. Create two empty lists: one called `public_holidays` and another called `other_holidays`.

2. Using a `for` loop, iterate over each list in `chinese_holidays` ignoring the "header" element.

3. In the loop, check whether each holiday is an official public holiday. If it is, add the name of the holiday to `public_holidays`. Otherwise, add the name of the holiday to `other_holidays`.

    :bulb: You need to utilize the subscript notation to extract each holiday's name.

The completed `public_holidays` *must* look like the list below:
```python
["New Year's Day", 'Spring Festival', 'Qingming Festival', 'Labor Day', 'Dragon Boat Festival', 'Mid-Autumn Festival', 'National Day']
```

And the completed `other_holidays` *must* look like the list below:
```python
['Lantern Festival', 'Qixi Festival', 'Double Ninth Festival']
```

### Problem 04 (20 Points)

Using a `for` loop and conditional statements, categorize the holidays as long break, medium break, short break, or no break.

1. Create four empty lists named `long_break`, `medium_break`, `short_break`, and `no_break`.

2. Using a `for` loop, iterate over each list in `chinese_holidays` ignoring the "header" element.

3. In the loop, check if the number of days off is 0. If it is 0, add the holiday name to `no_break`. If it is both greater than 0 and less than or equal to 3, add the holiday name to `short_break`. If it is both greater than 3 and less than or equal to 5, add the holiday name to `medium_break`. If it is greater than 5, add the holiday name to `long_break`.

   :bulb: You will need to employ `elif` statements together with `if-else` to solve this problem.

Your `long_break` *must* look like the list below:
```python
['Spring Festival', 'National Day']
```

Your `medium_break` *must* look like the list below:
```python
['Labor Day']
```

Your `short_break` *must* look like the list below:
```python
["New Year's Day", 'Qingming Festival', 'Dragon Boat Festival', 'Mid-Autumn Festival']
```

Your `no_break` *must* look like the list below:
```python
['Lantern Festival', 'Qixi Festival', 'Double Ninth Festival']
```

### Problem 05 (15 points)

Using a `while` loop to iterate through `chinese_holidays`, convert the specific date in each holiday to a list. For example, `'2022-01-01'` should be replaced by `['2022', '01', '01']`

1. Initialize a numerical variable named `i`.

2. Using a `while` loop, iterate over each list in `chinese_holidays` ignoring the "header".

3. In the loop, extract the date of each holiday and split it into a list containing three components: year, month, and day. Then assign it to each nested list in `chinese_holidays` as the second element.

   :bulb: If you do not know what condition you should give to the while loop, reviewing this week's lecture notes might give you some inspiration.

Now, the mutated `chinese_holidays` list *must* look like the nested list below:

```python
    [
        ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
        ["New Year's Day", ['2022', '01', '01'], 3, True],
        ['Spring Festival', ['2022', '02', '01'], 7, True],
        ['Lantern Festival', ['2022', '02', '15'], 0, False],
        ['Qingming Festival', ['2022', '04', '05'], 3, True],
        ['Labor Day', ['2022', '05', '01'], 5, True],
        ['Dragon Boat Festival', ['2022', '06', '03'], 3, True],
        ['Qixi Festival', ['2022', '08', '04'], 0, False],
        ['Mid-Autumn Festival', ['2022', '09', '10'], 3, True],
        ['National Day', ['2022', '10', '01'], 7, True],
        ['Double Ninth Festival', ['2022', '10', '04'], 0, False]
    ]
```

### Problem 06 (20 Points)

Using a `for` loop, add the corresponding season to the beginning of each list element in chinese_holidays.

1. Using a `for` loop, iterate over each list in `chinese_holidays` ignoring the "header".

2. If the holiday is between March and May (inclusive), add "Spring" to the beginning of the holiday list. If the holiday is between June and August (inclusive), add "Summer" to the beginning of the list. If the holiday is between September and November (inclusive), add "Fall" to the beginning of the list. If the holiday is between December and February (inclusive), add "Winter" to the beginning of the list.

    :bulb: You need to utilize a list method to solve this problem.

Now, your `chinese_holidays` *must* look like the nested list below:

```python
    [
        ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
        ['Winter', "New Year's Day", ['2022', '01', '01'], 3, True],
        ['Winter', 'Spring Festival', ['2022', '02', '01'], 7, True],
        ['Winter', 'Lantern Festival', ['2022', '02', '15'], 0, False],
        ['Spring', 'Qingming Festival', ['2022', '04', '05'], 3, True],
        ['Spring', 'Labor Day', ['2022', '05', '01'], 5, True],
        ['Summer', 'Dragon Boat Festival', ['2022', '06', '03'], 3, True],
        ['Summer', 'Qixi Festival', ['2022', '08', '04'], 0, False],
        ['Fall', 'Mid-Autumn Festival', ['2022', '09', '10'], 3, True],
        ['Fall', 'National Day', ['2022', '10', '01'], 7, True],
        ['Fall', 'Double Ninth Festival', ['2022', '10', '04'], 0, False]
    ]
```

### Problem 07 (20 Points)

Using a `while` loop, find the corresponding activities for 'Dragon Boat Festival'.

1. Initialize a numerical variable named `j`.

2. Using a `while` loop, iterate over each list in `activities`.

3. In the loop, check whether eating Zongzi is one of the activities for each holiday. If eating Zongzi is found, then extract all activities for that holiday and split it into a list named `dragon_boat_activities`. Then exit the loop.

    :bulb: Remember to increase the value of `j` by 1 if eating Zongzi is not found.

The `dragon_boat_activities` *must* look like the list below:

```python
    ['Dragon Boat Racing', 'Eating Zongzi']
```

