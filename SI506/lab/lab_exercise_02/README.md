# SI 506: Lab Exercise 02

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on loops and conditional statements.

## Background
Netflix has a top 10 list of TV shows and movies that change weekly. The following lab utilizes data from the top 10 streamed TV shows in the world on Netflix on the day of January 14, 2021. (Source: https://collider.com/top-10-netflix-tv-shows-list/)
For this lab, you are provided with a short list named `shows` that includes some basic information about
the top 10 TV shows. The list contains several string elements. Each string contains the show's name, genre, latest season number, and a one word description of the show provided by Netflix. (in the order listed). You are going to use `for` loops and `conditional statements` to complete each problem.

```python
shows = [
    "Action Pack, Kids, 1, exciting",
    "The Queen of Flow, Telenovela, 2, Emotional",
    "Hype House, Reality, 1, scandalous",
    "Queer Eye, Lifestyle, 6, Feel-good",
    "Cocomelon, Kids, 4, educational",
    "Emily in Paris, Romantic Comedy, 2, Quirky",
    "The Witcher, Fantasy, 2, Exciting",
    "Stay Close, Crime, 8, emotional",
    "Cobra Kai, Dramedy, 4, exciting",
    "Cheer, Reality, 2, exciting"
]
```

## 1.0 Problem 01 (3 points)

Loop over the `shows` list and access each show's genre (a substring of each string element). Append the genre value to the empty list named `genres`.

:bulb: Convert each string encountered to a list and access the genre element using list indexing.

## 2.0 Problem 02 (4 points)

Implement an `if` statement inside a `for` loop that identifies each show described as emotional.
Loop over the `shows` list; if the show is described as "emotional", append _only_ the show's name to the new list named `emotional_shows`.

:bulb: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage. You might need to use a built-in str method to convert the uppercase letters to lowercase when performing string matching.

## 3.0 Problem 03 (4 points)

Implement an `if` statement inside a `for` loop that evaluates whether or not the name of the show comprises more than one word.
Loop over the `shows` list; if the show has more than one word in its name, increment the variable `count` by one (1).

## 4.0 Problem 04 (4 points)

Implement an `if` statement inside a `for` loop and that evaluates whether or not a show's run is less than three (3) seasons.
Loop over the `shows` list and if the number of seasons in the show is less than 3 (exclusive), then append the show's name to a list named `new_shows`.

:bulb: Recall that you can utilize the built-in function `print()` to check on the values being appended to the new and established show lists. When satisfied with your conditional statements you can comment out `print()` or remove the expression from your code.

## 5.0 Problem 05 (5 points)

Implement an `if` statement inside a `for` loop in order to identify the longest-running show.
Loop over the `shows` list and check the number of seasons for each show. Assign the name of the show with the most seasons to the new variable named `longest_show`.
