# PROBLEM SET 07
import json

books = [
    {'title': 'Atomic habits', 'language': 'English', 'rating': '4.8',
    'weight_ounces': '12.3', 'num_reviews': 68878},
    {'title': 'The seven husbands of evelyn hugo', 'language': 'English',
    'rating': '4.6', 'weight_ounces': '10.9', 'num_reviews': 54882},
    {'title': 'It Ends with Us', 'language': 'English', 'rating': '4.7',
    'num_reviews': 67548},
    {'title': 'Reminders of Him', 'language': 'English', 'rating': '4.7',
    'weight_ounces': '11.2', 'num_reviews': 42222},
    {'title': 'Verity', 'language': 'English', 'rating': '4.6',
    'weight_ounces': '9.6', 'num_reviews': 67091},
    {'title': "Little Blue Truck's Valentine", 'language': 'English',
    'rating': '4.9', 'weight_ounces': '17.92', 'num_reviews': 6397},
    {'title': "The Complete Maus: A Survivor's Tale", 'language': 'English',
    'rating': '4.8', 'weight_ounces': '30.88', 'num_reviews': 4982},
    {'title': "I Love You to the Moon and Back", 'language': 'English',
    'rating': '4.9', 'weight_ounces': '10.4', 'num_reviews': 50419},
    {'title': "The Very Hungry Caterpillar", 'language': 'English',
    'rating': '4.9', 'weight_ounces': '6.4', 'num_reviews': 46699},
    {'title': "The Last Thing He Told Me", 'language': 'English',
    'rating': '4.3', 'weight_ounces': '17.12', 'num_reviews': 75366},
    {'title': "How to Catch a Leprechaun", 'language': 'English',
    'rating': '4.8', 'weight_ounces': '9.9', 'num_reviews': 5631}
]

# PROBLEM 1
def convert_to_float(books, keys):
    """Mutates the passed in < books > list by converting numbers
    masquerading as strings to float.

    Loop over each dictionary in the < books > list, then loop over each
    string element in the < keys > list. Inside the second loop, utilize
    each string element in the < keys > list as a key to access the value
    in the dictionary and convert it to a floating-point number.

    Parameters:
        books (list): a list of dictionaries, each containing information
        about a book.

        keys (list): a list of strings, each representing an attribute
        of the book (e.g., title, language, rating, etc).

    Returns:
        None
    """
    for book in books:
        for keyword in keys:
            if keyword in book.keys():
                book[keyword] = float(book[keyword])

# PROBLEM 2
def get_books_by_rating(books, rating, num_reviews=50000):
    """Collects a list of book titles from the passed in < books > list.

    Initialize an empty list. Then loop over each dictionary in the < books >
    list and check whether the book's rating is greater than the given rating
    and the number of reviews greater than the given num_reviews. If both
    conditions are met, add the book title to the list.

    Parameters:
        books (list): a list of dictionaries, each containing information
        about a book.

        rating (float): a floating-point number representing the average
        rating of a book.

        num_reviews (int): an integer number representing the number of
        reviews that a book has been received. The default value is 50000.

    Returns:
        list: a list of book titles.
    """
    list = []
    for book in books:
        if book['rating'] > rating and book['num_reviews'] > num_reviews:
            list.append(book['title'])
    return list

# PROBLEM 3
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON file and convert it to a Python dictionary

    Parameters:
        filepath (str): a path to the JSON file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# PROBLEM 4
def update_books(books, details):
    """Updates the < books > list by adding new key-value pairs to each
    dictionary element in the list.

    Iterate over the < details > dictionary, then iterate over the < books >
    list. In each iteration, check whether the title in < details > is the same
    as the title in < books > (case-insensitive comparison). If they are the
    same, update the dictionary in < books > list by adding the key-value pairs
    from the nested dictionaries in < details >

    Parameters:
        books (list): a list of dictionaries, each containing information
        about a book.

        details (dict): a dictionary of dictionaries, each containing
        information about a book.

    Returns:
        None
    """
    for value in details.values():
        for book in books:
            if book['title'].lower() == value['title'].lower():
                book.update(value)
                break

# PROBLEM 5
def get_book_price(books, title, format):
    """Checks the price for a particular book

    Loop over each element in the < books > list. If the book's title is the
    same as the given title (case-insensitive comparison) and the book's format
    is the same as the given format (case-insensitive comparison), return a
    dictionary with the title as the key and price as the value. Otherwise,
    return None.

    Parameters:
        books (list): a list of dictionaries, each containing information
        about a book.

        title (str): a string representing book title

        format (str): a string representing book format (e.g., Kindle,
        hardcover, paperback, etc.)

    Returns:
        dict or None: book title as the key and price as the value if the
        book's price is found; otherwise, return None.
    """

    for book in books:
        if book['title'].lower() == title.lower():
            for key in book['price'].keys():
                if key.lower() == format.lower():
                    value = book['price'][key]
                    dict = {book['title']: value}
                    return dict
    return None

# PROBLEM 6
def get_books_by_genres(books, genres):
    """Returns a dictionary of books by given genres.

    Initialize an empty dictionary. Then loop over each dictionary in the
    < books > list and check whether the book's genre is in the given genres
    list. If the book's genre is in the < genres > list, add the key-value
    pair with the book title as the key and book author as the value to the
    initialized dictionary. Return the dictionary until all matching books
    are found.

    Parameters:
        books (list): a list of dictionaries, each containing information
        about a book.

        genres (list): a list of strings each representing a book's genre

    Returns:
        dict: a dictionary of books that has the book titles as the keys and
        the book authors as the values.
    """
    dict = {}
    for book in books:
        for cur_genre in book['genre']:
            if cur_genre in genres:
                cur = book['author']
                dict[book['title']] = cur
    return dict

# PROBLEM 7
def write_json(filepath, data, encoding='utf-8', indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)

# Entry
def main():

    #problem 1.2: call convert_to_float
    convert_to_float(books, ['rating', 'weight_ounces'])
    print(f"\nProblem 1: books = \n{books}")

    #problem 2.3: call get_books_by_rating
    highly_rated = get_books_by_rating(books, 4.5)
    print(f"\nProblem 2: highly_rated = \n{highly_rated}")

    #problem 3.2: call read_json
    details = read_json('details.json')
    print(f"\nProblem 3: details = \n{details}")

    #problem 4.3: call update_books
    update_books(books, details)
    print(f"\nProblem 4: update_books = \n{books}")

    #problem 5.3: call get_book_price
    atomic_habits = get_book_price(books, 'atomic habits', 'hardcover')
    print(f"\nProblem 5: atomic_habits = \n{atomic_habits}")

    #problem 6.2: call get_books_by_genres
    requested_books = get_books_by_genres(books, ["Children’s Picture Books", "Thriller"])
    print(f"\nProblem 6: requested_books = \n{requested_books}")

    #problem 7.2: call write_json
    write_json('updated_books.json', books)


if __name__ == "__main__":
    main()