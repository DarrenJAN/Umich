# SI 506: Problem Set 07

## This week's Problem Set

This week's problem set focuses on nested data structures, JSON files, and functions.

## Background

For this week's Problem Set, you will be using a list of dictionaries and a JSON file to represent
[Amazon Best Sellers in Books for 2022 (So Far)](https://www.amazon.com/gp/bestsellers/2022/books/ref=zg_bs_tab_t_bsar/ref=zg_bs_tab_t_bsar).

You have been provided with a list of dictionaries, and each dictionary contains some information
about a book.

## Problem 01 (20 points)

__Task__: Implement a function that can convert numbers masquerading as strings in dictionaries to
float.

1. Implement a function called `convert_to_float` that accepts two parameters:

   * `books`, a list of dictionaries each containing information about a book.
   * `keys`, a list of strings each representing an attribute of a book.

   Mutates the given `books` list by converting numbers masquerading as strings to float. Review the
   docstring to better understand the function's expected behavior.

   :bulb: You need to utilize nested `for` loops and an `if` statement to solve this problem.

   :exclamation: Not every dictionary in the `books` list has the same set of keys.

2. After implementing `convert_to_float`, return to the `main` function. Call the function passing
it the `books` list and the list `['rating', 'weight_ounces']`.

   :bulb: You can call the `print()` function passing it `books`. Check whether the numbers
   masquerading as strings have been converted to `float`. Your `books` list __must__ resemble
   the list below:

   ```python
   [
       {'title': 'Atomic habits',
        'language': 'English',
        'rating': 4.8,
        'weight_ounces': 12.3,
        'num_reviews': 68878},
       {'title': 'The seven husbands of evelyn hugo',
        'language': 'English',
        'rating': 4.6,
        'weight_ounces': 10.9,
        'num_reviews': 54882},
       ...
    ]
   ```

## Problem 02 (20 points)

__Task__: Implement a function that can return a list of book titles by the given rating and number
of reviews.

1. Implement the function named `get_books_by_rating`. The function defines three parameters:

   * `books`, a list of dictionaries each containing information about a book.
   * `rating`, a floating-point number that represents the average rating.
   * `num_reviews`, a whole number that represents the number of reviews of a book, and the default
   value is `50000`.

   Review the docstring to better understand the function's expected behavior.

2. To implement the function, you need to employ a `for` loop and an `if` statement. Iterate over
the `books` list. Add the book title to a list if the book's rating is greater than the passed in
`rating` __and__ the number of reviews is greater than the given `num_reviews`.

3. After implementing `get_books_by_rating`, return to the `main` function. Call the function
passing it the `books` list and rating of `4.5` as arguments. Assign the return value to a variable
named `highly_rated`.

   :bulb: Your `highly_rated` list __must__ look like the list below:

   ```python
   ['Atomic habits',
    'The seven husbands of evelyn hugo',
    'It Ends with Us',
    'Verity',
    'I Love You to the Moon and Back']
   ```

## Problem 03 (20 points)

__Task__: Implement a function that can read a JSON file and convert it into a Python dictionary.

1. Implement the function named `read_json`. The function defines two parameters:

   * `filepath`, a path to a source JSON file.
   * `encoding`, a string representing a character encoding (default value = `'utf-8'`).

   Review the function's docstring for more information about the function's expected behavior.

2. After implementing `read_json`, return to the `main` function. Call the function passing it the
`details.json` filepath. Assign the return value to a variable named `details`.

## Problem 04 (20 points)

__Task__: Implement a function that can update the `books` list by getting new information from the
`details` dictionary.

1. Implement the function named `update_books`. The function defines two parameters:

   * `books`, a list of dictionaries each containing information about a book
   * `details`, a dictionary of dictionaries each containing information about a book.

   Review the docstring to better understand the function's expected behavior.

2. To implement the function, you need to loop over the nested dictionaries in `details`. Compare
the title in each nested dictionary with the title in each dictionary element of the `books` list.
If the title is the same (perform a case-insensitive comparison), add the new key-value pairs
(i.e., 'author': value, 'ISBN_10': value, 'genre': value, 'price': value, 'discount': value) to the
corresponding dictionary in `books` list.

   :bulb: You need to employ nested `for` loops and an `if` statement to solve this problem.

   :bulb: You can utilize a `dict` method to insert the specified items into the dictionary.

3. After implementing `update_books`, return to the `main` function. Call the function passing it
the `books` list and the `details` dictionary.

   :bulb: After updating the `books` list, your `books` __must__ resemble the list below:

```python
[
   {'title': 'Atomic Habits',
    'language': 'English',
    'rating': 4.8,
    'weight_ounces': 12.3,
    'num_reviews': 68878,
    'author': 'James Clear',
    'ISBN_10': '0735211299',
    'genre': ['Nonfiction', 'Self-help'],
    'price': {'Kindle': 13.99, 'Audiobook': 0, 'Hardcover': 11.98, 'Paperback': 18},
    'discount': True},
   {'title': 'The Seven Husbands of Evelyn Hugo',
    'language': 'English',
    'rating': 4.6,
    'weight_ounces': 10.9,
    'num_reviews': 54882,
    'author': 'Taylor Jenkins Reid',
    'ISBN_10': '1501161938',
    'genre': ['Psychological Fiction', 'Romance Novel'],
    'price': {'Kindle': 14.99, 'Audiobook': 0, 'Hardcover': 22.49, 'Paperback': 9.42},
    'discount': False},
    ...
]
```

## Problem 05 (25 points)

__Task__: Implement a function that can check the price of a particular book.

1. Implement the function named `get_book_price`. The function defines three parameters:

   * `books`, a list of dictionaries each containing information about a book.
   * `title`, a string represents the title of the book.
   * `format`, a string represents the book's format.

   Review the docstring to better understand the function's expected behavior.

2. To implement this function, you need to iterate over the `books` list. If the book has the
passed in `format` and `title`, return a dictionary with the title as the key and price as the
value; otherwise, return `None`.

3. After implementing `get_book_price`, return to the `main` function. Call the function passing the
following arguments in order:

   * `books`
   * `'atomic habits'` (lowercase required)
   * `'hardcover'` (lowercase required)

   Assign the return value to a variable named `atomic_habits`.

   :bulb: Your `atomic_habits` __must__ look like the dictionary below:

   ```python
    {'Atomic Habits': 11.98}
   ```

## Problem 06 (25 points)
__Task__: Implement a function that can return a dictionary of books by the given genres.

1. Implement a function called `get_books_by_genres` that accepts two parameters:

   * `books`, a list of dictionaries each containing information about a book.
   * `genres`, a list of strings each representing a book's genre

   Review the docstring to better understand the function's expected behavior.

   :bulb: You need to utilize nested `for` loops and an `if` statement to solve this problem.

2. After implementing `get_books_by_genres`, return to the `main` function. Call the function
passing it the `books` list and the list `["Children’s Picture Books", "Thriller"]`. Assign the
return value to a variable named `requested_books`.

   :bulb: Your `requested_books` list __must__ resemble the list below:

   ```python
    {'Verity': 'Colleen Hoover',
     "Little Blue Truck's Valentine": 'Alice Schertle',
     'I Love You to the Moon and Back': 'Amelia Hepworth',
     'The Very Hungry Caterpillar': 'Eric Carle',
     'The Last Thing He Told Me': 'Laura Dave',
     'How to Catch a Leprechaun': 'Adam Wallace'}
   ```

## Problem 07 (20 points)

__Task__: Implement a function that can write a list of dictionaries to a JSON file.

1. Implement the function named `write_json`. The function defines four parameters:

   * `filepath`, a path to target file.
   * `data`, a list of dictionaries that needs to be written
   into a JSON file;
   * `encoding`, name of encoding used to encode the file (default value = `utf-8`).
   * `indent`: aninteger number of "pretty printed" indention spaces applied to encoded JSON
     (Default value = `2`).

   Review the function's docstring for more information about the function's expected behavior.

2. After implementing `write_json`, return to the main function. Call the function `write_json` and
pass to it as arguments the filepath `updated_books.json`, the `books` list. Compare your output file to
the test fixture file `fxt-updated_books.json`. Both files _must_ match, line for line, and character
for character.
