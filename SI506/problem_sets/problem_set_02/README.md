# SI 506: Problem Set 02

## This week's Problem Set

This week's problem set will focus on conditional statements, `for` loops, and the `range()` type.
Some topics from previous sections (e.g. methods and indexing) are also included.

## Background

This week's problem set incorporates information about Hulu's popular shows and movies from
[Rotten Tomatoes](https://editorial.rottentomatoes.com/guide/best-hulu-shows-and-movies-to-binge-watch-now/),
[TV Guide](https://www.tvguide.com/news/best-movies-on-hulu-right-now/), and
[Paste Magazine](https://www.pastemagazine.com/movies/hulu/best-movies-hulu/#44-we-need-to-talk-about-kevin).
You are asked to iterate over two different lists to extract information.

## Part 01

You are provided with a list called `top_shows` that has details from Rotten Tomatoes about the five
best television shows on Hulu. In order, each element of this list contains the following
information:

- Show Name
- Starring Actor
- Genre
- Average Audience Rating
- Year of Release

### Problem 01 (10 Points)

Use an accumulator pattern to add the starring actors from `top_shows` to a new list called `stars`.

1. Create an empty list called `stars`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, extract the name of the starring actor from each string in `top_shows`. Add this
   name to the `stars` list.

   :bulb: Consider splitting each string encountered into a list and extracting the information
   required using indexing.

The `stars` list you create will contain the following elements:

```python
    ['Steve Martin',
    "D'Pharaoh Woon-a-Tai",
    'Timothy Olyphant',
    'Matt Berry',
    'Pamela Adlon']
```

### Problem 02 (11 points)

Using an accumulator pattern with a conditional statement, add the names of comedy shows to a new
list called `comedies`.

1. Create an empty list called `comedies`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, check whether each show is a comedy.

   :bulb: Python is a case-sensitive programming language. For this problem ensure that your `if`
   statement performs a *case-insensitive* comparison of the string values.

4. Add the names of the comedy shows to the `comedies` list.

   :bulb: Consider splitting each string encountered into a list and extracting the information
   required using indexing.

The `comedies` list you create will contain the following elements:

```python
    ['Only Murders in the Building',
    'Better Things']
```

### Problem 03 (10 points)

Using an accumulator pattern, calculate the average audience rating across all television shows in
`top_shows`. Assign this average to a variable called `avg_rating`.

1. Initialize a numerical variable called `total_ratings`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, extract the rating from each string and add it to `total_ratings`.

4. Calculate the average and assign it to the variable `avg_rating`.

### Problem 04 (12 Points)

Using a `for` loop and conditional statements, compare the audience rating for each show to
`avg_rating`. Categorize the shows as below average or above average based on this comparison.

1. Create two empty lists: one called `above_avg` and another called `below_avg`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, compare the rating for each show to `avg_rating`.

4. Add the names of shows that have a rating greater than average to the `above_avg` list.
   Otherwise, add the name to the `below_avg` list.

   :bulb: You will need an `if-else` statement here.

### Problem 05 (19 points)

Using a `for` loop, calculate a rating between 0 and 5 for each show. Attach this rating to the
string that has information about the show. Add this updated string to a new list called
`top_shows_new`.

1. Create an empty list called `top_shows_new`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, extract the rating, divide it by 20, and round the quotient to one decimal point by
   passing it to the built-in function `round()`.

   :bulb: The built-in function `round()` accepts two arguments: the value to be rounded and the
   number of decimal points to retain. The function returns a `float`. For a working example see
   the w3schools ["Python round() function"](https://www.w3schools.com/python/ref_func_round.asp)
   page.

4. Using an f-string literal, add this newly calculated rating to the end of the string that
   contains the show's information. Remember to include the appropriate separator between the old
   string and the new rating.

5. Add this string to `top_shows_new`.

The `top_shows_new` list you create will contain the following elements:

```python
    ['Only Murders in the Building | Steve Martin | comedy | 93 | 2021 | 4.7',
    "Reservation Dogs | D'Pharaoh Woon-a-Tai | Crime | 88 | 2021 | 4.4",
    'Justified | Timothy Olyphant | crime | 95 | 2010 | 4.8',
    'What We Do in the Shadows | Matt Berry | horror | 92 | 2019 | 4.6',
    'Better Things | Pamela Adlon | Comedy | 84 | 2016 | 4.2']
```

### Problem 06 (15 Points)

Using a `for` loop, find the oldest show in `top_shows`.

1. Create a numerical variable called `min_year`.

2. Using a `for` loop, iterate over each string in `top_shows`.

3. In the loop, extract the release year for each show. Compare this year to `min_year` to find the
   oldest show.

4. Assign the name of the oldest show to a variable called `oldest_show`.

## Part 02

You are provided with a list called `content`. It contains the name of a show or film from Hulu and
its category.

### Problem 07 (10 Points)

Using a `for` loop with the `range()` type, create a list that contains *every other* string in
`content`.

1. Initialize an empty list variable called `select_content`.

2. Create a `for` loop that iterates over the `range()` type. Adjust the start, stop, and step
   arguments to return *every other* string from the `content` list.

3. Add these strings to the `select_content` list.

The `select_content` list you create will contain the following elements:

```python
    ['Parasite: Film',
    'Akira: filM',
    'Minding the Gap: Film',
    'Summer of Soul: FiLm',
    'The Mole Agent: FILM',
    'The Great: SHOW']
```

### Problem 08 (13 Points)

Using a `for` loop and conditional statements, separate the films from the shows.

1. Create two empty lists: one called `films` and another called `shows`.

2. Using a `for` loop, iterate over each string in `content`.

3. In the loop, check the category of each each element in `content`.  Add names of shows to the
   `shows` list. Add the names of films to the `films` list.

   :bulb: You will need an `if-else` statement here.
