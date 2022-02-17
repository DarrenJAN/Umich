# SI 506: Problem Set 04

## This week's Problem Set

This week's problem set will focus on creating functions, including the use of
positional and keyword arguments.

## Background

In honor of Black History Month, this problem set features some data from
Wikipedia about different jazz musicians. Jazz is a music genre started by
Afican American communities in New Orleans during the early 1900's.
It has spread around the world and continues to evolve and inspire musicians
to this day.

You are provided with a list of lists called `musicians`. The nested lists
contain the information specified by the header.

- name: Commonly recognized name of the musician (`str`)
- city: City where the musician was born (`str`)
- state: State where the musician was born (`str`)
- instruments: List of some instruments played by the musician(`list`)
- inspiration: An artist who inspires the musician (`str`)
- birth_date: Date when the musician was born (`str`)
- death_date: Date when the musician died, if applicable (`str`)


### Problem 01 (16 Points)

Create a `clean_list` function that cleans some elements of the data for each musician. Skipping the
header, loop through `musicians` and call `clean_list` on each list that contains musician data.

1. Create a function called `clean_list` that takes one argument `info` (a list of musician data).
This function should do the following:

    1. Some lists do not have a death date (i.e. they have a length of 6). In this case, add `None`
    to the end of the list. Otherwise, extract the year from a person's death date and convert it into
    an integer.
    2. Remove the leading and trailing spaces from a person's name.
    3. Make the state lowercase.
    4. Extract the year from each person's birth date and convert it into an integer.

    The function returns `None`.

    :bulb: The `None` object (type=`NoneType`) denotes the absence of a value. It is neither a string
    nor equal to zero (0). Refer to [W3Schools](https://www.w3schools.com/python/ref_keyword_none.asp)
    for more information.

2. Using a `for` loop that skips the header list, iterate over the elements that represent musicians in the `musicians` list.
In the loop code block, call the `clean_list` function on each element in `musicians`.

After the loop terminates, the `musicians` list will contain the following elements:

```python
    [
        ['name', 'city', 'state', 'instruments', 'inspiration', 'birth_date', 'death_date'],
        ['Christian Scott Atunde Adjuah', 'New Orleans', 'la', ['trumpet'], 'Miles Davis', 1983, None],
        ['Ron Carter', 'Ferndale', 'mi', ['double bass', 'cello'], 'Miles Davis', 1937, None],
        ['Alice Coltrane', 'Detroit', 'mi', ['piano', 'harp', 'vocals'], 'Ernest Farrow', 1937, 2007],
    ...
    ]
```


### Problem 02 (16 Points)

Create a function called `get_state` that returns the state that a musician is from.
Using an accumulator pattern with a conditional statement, add the names of Michiganders to a new
list called `mi_musicians`.

1. Create a function called `get_state` that takes one argument `info` (a list of musician data).
This function returns the two-letter state code from the info list.

2. Using a `for` loop, iterate over `musicians`. In the loop code block, call the `get_state` function
to check whether each musician is from Michigan. Add the relevant **names** to a new list
called `mi_musicians`.

    :bulb: The state code for Michigan is 'mi'.

The `mi_musicians` list you create will contain the following elements:

```python
    ['Ron Carter',
    'Alice Coltrane',
    'Dorothy Ashby',
    'Roy Brooks']
```


### Problem 03 (16 Points)

Create a function called `is_from_region` that returns a boolean (True/False) of whether a musician
is from a given region. Using an accumulator pattern with an `if-elif` statement, add tuples
containing the musician's name and home state to a `southerners` list and a `northeasterners` list,
based on the region where each musician was born.

1. Create a function called `is_from_region` that takes two arguments `info` (a list of musician
data) and `region` (a list of states within a region). This function calls the `get_state` function
to find the state where a musician was born and then checks whether that state is among those in
the region given.

2. Using a `for` loop, iterate over `musicians`. In an `if statement` call the `is_from_region`
function. If the `if` statement evaluates to `True`, append a tuple containing the musician's name
and state as items to a list called `southerners`. Pass to this function the data for each musician
and the given `south_states` list employing **keyword arguments in reverse order**.

3. Otherwise, if the musician is from the Northeastern United States, append a tuple containing
the musician's name and state as items to a list called `northeasterners`. For this step, you will
need the given `northeastern_states` list. When calling the `is_from_region` function in your
`elif` statement, pass the **keyword arguments in reverse order**.

    :exclamation: Be mindful of spacing when using keyword arguments.

The `southerners` list you create will contain the following elements:

```python
    [
        ('Christian Scott Atunde Adjuah', 'LA'),
        ('Robert Glasper', 'tx'),
        ('Walter Smith III', 'Tx'),
        ('Cecile McLorin Salvant', 'fL'),
        ('John Coltrane', 'Nc'),
        ('Bobbi Humphrey', 'TX'),
        ('Thelonius Monk', 'NC')
    ]
```

The `northeasterners` list you create will contain the following elements:

```python

    [
        ('Sarah Elizabeth Charles', 'MA'),
        ('Wayne Shorter', 'nj')
    ]
```


### Problem 04 (16 Points)

Among the inspirational artists included in the musicans list, the name Miles Davis appears the
most. Create a function called `is_inspired` that returns a boolean value indicating whether or not
one musician inspired another. Using an accumulator pattern with the newly defined function, count
the number of musicians whom Miles Davis has inspired. Calculate the percent as well.

1. Create a function called `is_inspired` that takes three arguments `info` (a list of musician
data), `inspo` (the name of an artist as a string), and a **default** `idx` (an integer representing
the index where the inspirational artist is located in `info`). This function returns a boolean
value indicating whether or not the inspirational artist provided matches the inspirational artist
in `info`.

    :exclamation: When checking the inspirational artist in `is_inspired`, be sure to use *case-insensitive* matching to avoid certain errors that could arise from typos.

2. Initialize a numeric variable called `davis_count`. Using a `for` loop and skipping the headers
list, iterate over the information in `musicians`. In an `if` statement, call the `is_inspired`
function. Increment `davis_count` by 1 for every musician inspired by 'Miles Davis'.

3. Calculate the percentage of musicians who are inspired by Miles Davis. Assign this number
(rounded to 2 decimal places) to the variable `davis_percent`. You can use the following formula to
calculate the percentage:
    - musicians inspired by Davis / all musicians * 100

### Problem 05 (16 Points)

Create a function called `calculate_age` that returns a tuple containing a person's name and their
approximate age. Using an accumulator pattern with the newly defined function, find the youngest
musicians from the musicians list.

1. Create a function called `calculate_age` that takes two arguments `info` (a list of musician
data) and `end_year` (a string or integer of the year used to calculate the age; default value is
2022). This function recturns a **tuple** containing the musician's **name and age** for a given
year.

2. Initialize a `min_age` variable and `youngest_musicians` list. Using a `for` loop, iterate over
`musicians`. In the loop code block, call the `calculate_age` function, unpacking the tuple returned
into two variables. With the help of `min_age` and the output from the function, find the youngest
people and add their **names** to `youngest_musicians`. You should clear out your accumulator list
whenever your loop finds a person who is younger than the last.

The `youngest_musicians` list you create will contain the following elements:

```python
    ['Cecile McLorin Salvant',
    'Sarah Elizabeth Charles']
```


### Problem 06 (20 Points)

Using an accumulator pattern with the `calculate_age` function and an **indefinite** loop, find the current age of the living
musicians. For those who are no longer alive, calculate their age when they passed away.

1. Initialize two lists: `past_musicians` and `current_musicians`.

2. Iterate over `musicians` (excluding the headers) using a **while** loop. Check for a death date. If there is one,
append the output of the `calculate_age` function to the `past_musicians` list, passing their year
of death as an argument.

3. Otheriwse, append the output of the `calculate_age` function to the `current_musicians` list,
using the default year.

The `past_musicians` list you create will contain the following elements:

```python
    [
        ('Alice Coltrane', 70),
        ('Dorothy Ashby', 54),
        ('Miles Davis', 65),
        ('John Coltrane', 41),
        ('Roy Brooks', 67),
        ('Thelonius Monk', 65)
    ]
```

The `current_musicians` list you create will contain the following elements:

```python
    [
        ('Christian Scott Atunde Adjuah', 39),
        ('Ron Carter', 85),
        ('Esperanza Spalding', 38),
        ('Robert Glasper', 44),
        ('Marquis Hill', 35),
        ('Walter Smith III', 42),
        ('Cecile McLorin Salvant', 33),
        ('Sarah Elizabeth Charles', 33),
        ('Herbie Hancock', 82),
        ('Wayne Shorter', 89),
        ('Bobbi Humphrey', 72)
    ]
```


### Problem 07 (25 Points)

Create a function called `plays_woodwind` that returns a boolean value indicating whether or not a
musician plays a woodwind instrument. Using an accumulator pattern with the newly created function,
count the number of musicians who play woodwind instruments.

1. Create a function called `plays_woodwind` that takes two arguments `info` (a list of musician
data) and a **default** `idx` (the index where the list of instruments is located in `info`).
The function loops through the musician's instruments list to check whether any are in the
`woodwinds` list provided. This function returns `True` if a musician plays any woodwind
instruments.

2. Initialize a numeric variable called `wind_musicians`. Using a `for` loop, and skipping the
headers list, iterate over the information in `musicians`. In an `if statement`, call the
`plays_woodwind` function. Increment `plays_woodwind` by 1 for every musician who plays a woodwind
instrument.