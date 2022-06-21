import csv

# LAB EXERCISE 07
print('Lab Exercise 07 \n')

# SETUP
new_books = [
    ["little Blue Truck's Valentine", 'clarion Books', 'english', '4.9', '17.9'],
    ['verity', 'grand Central Publishing', 'english', '4.6', '9.6'],
    ['life Force: How New Breakthroughs in Precision Medicine Can Transform the Quality of Your Life & Those You Love', 'simon & Schuster', 'english', '4.4', '28.8']
]

# END SETUP

#Problem 01
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

    pass


# Problem 02
def add_books(books, new_books):
    """
    This function takes in a list of dictionaries and a nested list, creates a dictionary for each new book, and adds the new dictionary to the existing books list.

    Parameters:
        books (list): A list of dictionaries containing book data.
        new_books (list): A nested list containing book data.

    Returns:
        None
    """

    pass


# Problem 03
def clean_books(books):
    """
    Updates the values inside a list of dictionaries to the appropriate conventions listed below:

        rating and weight_ounces should be converted to a float
        All remaining strings should have each word capitalized

    Parameters:
        books (list): A list of dictionaries containing book data.

    Returns:
        None
    """

    pass


# Problem 04
def get_heavy_books(books):
    """
    This function takes a list of dictionaries as an argument and returns a list of book titles for books that are heavier than a pound (16 ounces).

    Parameters:
        books (list): books (list): A list of dictionaries containing book data.
    Returns:
        heavy_books (list): A list containing book titles that weighs more than 16 ounces
    """

    pass


# Problem 05
def add_weight_category(books):
    """
    This function takes a list of dictionaries as an argument, determines which books are heavy using < get_heavy_books >, and adds the 'weight' key and whether the book is heavy or light.

    Parameters:
        books (list): A list of dictionaries containing book data.
    Returns:
        None
    """

    pass


# Problem 06
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

    pass


# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")


    # Problem 02
    print("Problem 02:\n")


    # Problem 03
    print("Problem 03:\n")


    # Problem 04
    print("Problem 04:\n")


    # Problem 05
    print("Problem 05:\n")


    # Problem 06
    print("Problem 06:\n")


if __name__ == "__main__":
    main()