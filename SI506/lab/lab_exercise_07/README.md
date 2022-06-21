# SI 506: Lab Exercise 07

## This week's Lab Exercise

This week's lab exercise includes six (6) problems that focus on nested data structures and reading data from a CSV file.

## Background

For this lab, you are provided with a CSV file with data that represent the four (4) best selling books on Amazon so far in 2022 and a list of lists containing three (3) additional best selling books (https://www.amazon.com/gp/bestsellers/2022/books/ref=zg_bs_tab_t_bsar/ref=zg_bs_tab_t_bsar)

Once read in from the CSV, the dictionaries within the list contain the book title, publisher, language, rating, and weight in ounces.

```python
books = [
    {'title': 'atomic Habits', 'publisher': 'avery', 'language': 'english', 'rating': '4.8', 'weight_ounces': '12.3'},
    {'title': 'the Seven Husbands of Evelyn Hugo', 'publisher': 'washington Square Press', 'language': 'english', 'rating': '4.6', 'weight_ounces': '10.9'},
    {'title': 'it Ends With Us', 'publisher': 'atria', 'language': 'english', 'rating': '4.7', 'weight_ounces': '10.4'},
    {'title': 'reminders of Him', 'publisher': 'montlake', 'language': 'english', 'rating': '4.7', 'weight_ounces': '11.2'}
]
```

The lists within the list contain the same information, but are just lists, not dictionaries.

```python
new_books = [
    ["little Blue Truck's Valentine", 'clarion Books', 'english', '4.9', '17.9'],
    ['verity', 'grand Central Publishing', 'english', '4.6', '9.6'],
    ['life Force: How New Breakthroughs in Precision Medicine Can Transform the Quality of Your Life & Those You Love', 'simon & Schuster', 'english', '4.4', '28.8']
]
```

## 1.0 Problem 01 (2 points)

1. Write a function called `read_csv_to_dicts` that defines four parameters:

    * `filepath` (str): A filepath of a csv file to be read from.

    * `encoding` (str): Name of encoding used to decode file. Has a *default value* of `utf-8`.

    * `newline` (str): Replacement value for newline; *default value* is `''`.

    * `delimiter` (str): Delimiter that separates row values; *default value* is `','`.

    This function should load a csv file and return its contents in a list of dictionaries,
    where each dictionary is one row from the csv file.

2. Inside of the `main()` function, create a variable called `top_amazon_books` and assign the value to the result of `read_csv_to_dicts`. Set the filepath to `top_amazon_books.csv`.

## 2.0 Problem 02 (4 points)

1. Implement a function called `add_books()` that accepts two parameters:

    * `books` (list): A list of dictionaries containing book data.

    * `new_books` (list): A nested list containing book data.

    This function must loop over `new_books` and add each nested list to `books` as a dictionary. This function will return `None`.

:bulb: You can assume that `new_books` will always have the same seven elements as the dictionaries in `top_amazon_books`.

2. Inside of the `main()` function, call `add_books` passing it the list of dictionaries `top_amazon_books` and the list of lists `new_books`.

:bulb: After calling this function on `top_amazon_books` and `new_books`, `top_amazon_books` should match the following:

```python
[
{'title': 'atomic Habits', 'publisher': 'avery', 'language': 'english', 'rating': '4.8', 'weight_ounces': '12.3'},
{'title': 'the Seven Husbands of Evelyn Hugo', 'publisher': 'washington Square Press', 'language': 'english', 'rating': '4.6', 'weight_ounces': '10.9'},
{'title': 'it Ends With Us', 'publisher': 'atria', 'language': 'english', 'rating': '4.7', 'weight_ounces': '10.4'},
{'title': 'reminders of Him', 'publisher': 'montlake', 'language': 'english', 'rating': '4.7', 'weight_ounces': '11.2'},
{'title': "little Blue Truck's Valentine", 'publisher': 'clarion Books', 'language': 'english', 'rating': '4.9', 'weight_ounces': '17.9'},
{'title': 'verity', 'publisher': 'grand Central Publishing', 'language': 'english', 'rating': '4.6', 'weight_ounces': '9.6'},
{'title': 'life Force: How New Breakthroughs in Precision Medicine Can Transform the Quality of Your Life & Those You Love', 'publisher': 'simon & Schuster', 'language': 'english', 'rating': '4.4', 'weight_ounces': '28.8'}
]
```


## 3.0 Problem 03 (4 points)

1. Implement a function called `clean_books()` that accepts one parameter:

    * `books` (list): A list of dictionaries containing book data.

     All of the appropriate words in the CSV are capitalized except the first word and two of the values should be floats. Loop over each of the keys, convert `rating` and `weight_ounces` to floats, and iterate over the other strings to make sure the first word in each string is capitalized. This funciton will return `None`.

2. Inside of the `main()` function, call `clean_books` and pass the list `top_amazon_books` to it.

:bulb: You can assume that `rating` and `weight_ounces` will always be able to get converted to floats properly.

:bulb: You should focus on breaking the string up so you can get the first word in the string to capitalize and then put the string back together. If you use `.capitalize()` on the whole string, it will change any properly capitalized letters to lowercase.


## 4.0 Problem 04 (4 points)

1. Implement a function called `get_heavy_books()` that accepts one parameter:

    * `books` (list): A list of dictionaries containing book data.

    Loop over `books` and check the values that belong to the key `"weight_ounces"` to determine whether a book is heavy or not. A book is considered heavy if it weights more than one pound (16 ounces). The function returns a list of the heavy book titles.

2. Inside of the `main()` function, call `get_heavy_books` and pass it `top_amazon_books` as an argument. Assign the return value to a variable called `heavy_book_list`.

:bulb: You can assume that all the dictionaries contain a `title` and a `weight_ounces`. You can also assume that `weight_ounces` is always a string that can be cast to a float.

:bulb: After calling this function on `top_amazon_books`, the return value must match the following list:

```python
["Little Blue Truck's Valentine",
'Life Force: How New Breakthroughs in Precision Medicine Can Transform the Quality of Your Life & Those You Love']
```

## 5.0 Problem 05 (4 points)

1. Implement a function called `add_weight_category()` that accepts one parameter:

    * `books` (list): A list of dictionaries containing book data.

    Utilizing `get_heavy_books()`, loop over all the dictionaries in `books` and add a new key, `"weight"`. If a book is heavy, the value for `"weight"` should be `'heavy'`. If it's light, the value for `"weight"` should be `'light'`. This function returns `None`.

2. Inside of the `main()` function, call `add_weight_category()` and pass it the list `top_amazon_books`. You can check your work by printing `top_amazon_books`.

:bulb: After calling this function on `top_amazon_books`, the list should look like this:

```python
[{'title': 'Atomic habits', 'publisher': 'Avery', 'language': 'English', 'rating': '4.8', 'weight_ounces': '12.3', 'weight': 'light'},
{'title': 'The seven husbands of evelyn hugo', 'publisher': 'Washington Square Press', 'language': 'English', 'rating': '4.6', 'weight_ounces': '10.9', 'weight': 'light'},
{'title': 'It Ends with Us', 'publisher': 'Atria', 'language': 'English', 'rating': '4.7', 'weight_ounces': '10.4', 'weight': 'light'},
{'title': 'Reminders of Him', 'publisher': 'Montlake', 'language': 'English', 'rating': '4.7', 'weight_ounces': '11.2', 'weight': 'light'},
{'title': 'Little Blue Truck\'s Valentine', 'publisher': 'Clarion Books', 'language': 'English', 'rating': '4.9', 'weight_ounces': '17.9', 'weight': 'heavy'},
{'title': 'Verity', 'publisher': 'Grand Central Publishing', 'language': 'English', 'rating': '4.6', 'weight_ounces': '9.6', 'weight': 'light'},
{'title': 'Life Force: How New Breakthroughs in Precision Medicine Can Transform the Quality of Your Life & Those You Love', 'publisher': 'Simon & Schuster', 'language': 'English', 'rating': '4.4', 'weight_ounces': '28.8', 'weight': 'heavy'}]
```

## 6.0 Problem 06 (2 points)

1. Write a function called `write_dicts_to_csv` that defines five parameters:

    `filepath` (str): Path to target file

    `data` (list): List of dictionaries to be written to the target file

    `fieldnames` (seq): Sequence that indicates the order of the columns.

    `encoding` (str): Name of encoding used to encode the file. Has a *default value* of `utf-8`.

    `newline` (str): Specifies replacement value for newline. Has an empty string (`''`)
    as its *default value*.

    This function writes data to a csv file in filepath, where each dictionary
    is a row in the csv file.

2. In `main()`, create a variable `fieldnames` that has as its value a list representing the column names in `top_amazon_books`.

3. Call `write_dicts_to_csv` to write `top_amazon_books` to the filepath
`stu_updated_amazon_books.csv` using positional arguments. Include the `fieldnames` variable in your function call.

:bulb: In VS Code you can compare or "diff" the file you generate (`stu_updated_amazon_books.csv`) against `fxt_updated_amazon_books.csv`.