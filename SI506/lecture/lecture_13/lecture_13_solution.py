# SI 506: Lecture 13

import csv
import os
import re


def get_attribute(publication, headers, column_name):
    """Returns a < publication > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the header
    value.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from the CSV
        column_name (str): name of the "headers" column

    Returns:
        str: element sourced from passed in publication list
    """

    return publication[headers.index(column_name)]


def get_citation_count_by_year(publications, headers, year):
    """Returns the annual citation count across all < publications > per
    the provided < year >. Delegates the task of accessing each publication's
    yearly citation count to the function < get_attribute >.

    Parameters:
        publications (list): nested list of publications
        headers (list): column names sourced from the CSV
        year (str): column name (e.g., '1995')

    Returns:
        int: citation count across all publications for a given year
    """

    count = 0
    for publication in publications:
        count += int(get_attribute(publication, headers, year))
    return count


def format_string(string):
    """Converts passed in string to mixed case. Reformats individual words using
    str.lower(), str.capitalize(), or str.upper() according the following rules.

    Rules:
        1. < acronyms > are converted to uppercase.
        2. < stopwords > are converted to lowercase unless the stopword constitutes
           the first word in the string in which case the first letter is capitalized.
        3. < ordinals > are converted to lowercase (34TH -> 34th).
        4. Otherwise, the first letter of all other words are capitalized.

    Parameters:
        string (str): String to convert

    Returns:
        str: new mixed case string
    """

    acronyms = ('ACM', 'CHI', 'CIKM', 'ICER', 'ISDN', 'PLOS',
                'RECSYS', 'SIGCHI', 'SIGIR', 'WWW')
    stopwords = ('a', 'an', 'and', 'as', 'do', 'for', 'from', 'how', 'in',
                 'is', 'it', 'on', 'or', 'of', 'to', 'the', 'that', 'with')
    ordinals = ('5th', '6th', '10th', '15th', '24th', '25th', '26th', '28th',
                ' ', '37th', '45th') # replace with regular expression (more Pythonic)

    words = string.split()
    for i in range(len(words)):
        word = words[i] # access word
        if word.upper() in acronyms:
            words[i] = word.upper()
        elif i == 0 and word.lower() in stopwords:
            words[i] = word.capitalize() # first word (capitalize first letter)
        elif i > 0 and word.lower() in stopwords:
            words[i] = word.lower() # lowercase only
        elif word.lower() in ordinals:
            words[i] = word.lower() # lowercase only
        else:
            words[i] = word.capitalize()
    return ' '.join(words) # WARN: convert list back to a string

    # Alternative: built-in enumerate() function
    # words = string.split()
    # for i, word in enumerate(words):
    #     word = words[i] # access word
    #     if word.upper() in acronyms:
    #         words[i] = word.upper()
    #     elif i == 0 and word.lower() in stopwords:
    #         words[i] = word.capitalize() # first word (capitalize first letter)
    #     elif i > 0 and word.lower() in stopwords:
    #         words[i] = word.lower() # lowercase only
    #     elif word.lower() in ordinals:
    #         words[i] = word.lower() # lowercase only
    #     else:
    #         words[i] = word.capitalize()
    # return ' '.join(words) # WARN: convert list back to a string

    # Alternative: regular expression
    # regex = re.compile(r'[0-9]+(th|TH)') # ordinal match
    # words = string.split()
    # for i, word in enumerate(words):
    #     word = words[i] # access word
    #     if word.upper() in acronyms:
    #         words[i] = word.upper()
    #     elif i == 0 and word.lower() in stopwords:
    #         words[i] = word.capitalize() # first word (capitalize first letter)
    #     elif i > 0 and word.lower() in stopwords:
    #         words[i] = word.lower() # lowercase only
    #     elif regex.match(word):
    #         words[i] = word.lower() # lowercase only
    #     else:
    #         words[i] = word.capitalize()
    # return ' '.join(words) # WARN: convert list back to a string


def has_umsi_faculty_author(umsi_faculty, coauthors, ignore=None):
    """Identifies whether or not a publication's < coauthors > includes at least
    one member of the UMSI faculty other than the faculty member flagged to
    < ignore >. If a match is obtained the function returns True; other False
    is returned.

    Comparing the names of faculty members and publication coauthors requires
    adoption of the following string format:

    `<last name>, <first name>`

    Parameters:
        umsi_faculty (list): nested list of UMSI faculty members
        authors (list): list of a publication's coauthors
        ignore (str): name of a UMSI faculty member to ignore. Default = None

    Returns:
        bool: True if a match is obtained; False otherwise
    """

    for faculty_member in umsi_faculty:
        name = ', '.join(faculty_member)
        # name = f"{faculty_member[0]}, {faculty_member[1]}" # alternative
        if name != ignore and name in coauthors:
            return True
    return False


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """
    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """
    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point. Orchestrates execution flow.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 FILE PATHS WITH OS.PATH

    # Current working directory
    cwd = os.getcwd()

    print(f"\n1.0.1 Current working directory = {cwd}")

    # Absolute path to directory in which *.py is located.
    abs_path = os.path.dirname(os.path.abspath(__file__))

    print(f"\n1.0.2 Absolute directory path = {abs_path}")

    # Construct macOS and Windows friendly paths
    faculty_path = os.path.join(abs_path, 'umsi-faculty.txt')
    resnick_path = os.path.join(abs_path, 'resnick-citations.csv')

    # Relative paths
    # faculty_path = './umsi-faculty.csv'
    # resnick_path = './resnick-citations.csv'

    print(f"\n1.0.3 umsi-faculty.csv path = {faculty_path}")
    print(f"\n1.0.4 resnick-citations.csv path = {resnick_path}")


    # 2.0 CHALLENGES

    # CHALLENGE 01 GET ATTRIBUTE

    # Read CSV file and retrieve data
    publications = read_csv(resnick_path)

    print(f"\nCh 01 example publication\n{publications[1]}")

    # Get headers
    headers = publications[0] # header row

    print(f"\nCh 01 Headers\n{headers}")

    # Test function
    total_citations = get_attribute(publications[9], headers, 'Total Citations')

    # Title: Enquiring Minds: Early Detection of Rumors in Social Media from Enquiry Posts
    print(f"\nCh 01 Enquiring Minds total citations\n{total_citations}")


    # CHALLENGE 02 MOST CITATIONS (TIES PERMITTED)

    max_citations = []
    max_count = 0
    for publication in publications[1:]:
        citation_count = int(get_attribute(publication, headers, 'Total Citations'))
        if citation_count > max_count:
            max_citations.clear()
            max_count = citation_count
            max_citations.append(publication)
        elif citation_count == max_count:
            max_citations.append(publication)
        else:
            continue # else is optional but explicit

    # Write to file
    filepath = './resnick-citations-max_citations.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-max_citations.csv')
    write_csv(filepath, max_citations, headers)


    # CHALLENGE 03 FEWEST CITATIONS (TIES PERMITTED)

    min_citations = []
    min_count = float('inf')
    for publication in publications[1:]:
        citation_count = int(get_attribute(publication, headers, 'Total Citations'))
        if citation_count < min_count:
            min_citations.clear()
            min_count = citation_count
            min_citations.append(publication)
        elif citation_count == min_count:
            min_citations.append(publication)
        else:
            continue # else is optional but explicit

    # Write to file
    filepath = './resnick-citations-min_citations.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-min_citations.csv')
    write_csv(filepath, min_citations, headers)


    # CHALLENGE 04

    filepath = './umsi-faculty.csv'
    # input_path = os.path.join(abs_path, 'umsi-faculty.csv')
    umsi_faculty = read_csv(filepath) # includes header row

    umsi_coauthored_publications = []
    for publication in publications[1:]:
        authors = get_attribute(publication, headers, 'Authors').split('; ')
        if has_umsi_faculty_author(umsi_faculty[1:], authors, ignore='Resnick, Paul'):
            umsi_coauthored_publications.append(publication)

    # Write to file
    filepath = './resnick-citations-umsi_coauthored.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-umsi_coauthors.csv')
    write_csv(filepath, umsi_coauthored_publications, headers)


    # CHALLENGE 05

    # Slice out the years
    idx = headers.index('1995') # first column with annual citation counts
    years = headers[idx:] # slice

    annual_counts = []
    for year in years:
        count = get_citation_count_by_year(publications[1:], headers, year)
        annual_counts.append((year, count)) # tuple

    # Write to file
    filepath = './resnick-citations-annual_counts.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-annual_counts.csv')
    write_csv(filepath, annual_counts, ['year', 'citations'])


    # CHALLENGE 06: CLEAN DATA, CSV READER/WRITER

    title_idx = headers.index('Title')
    authors_idx = headers.index('Authors')
    source_idx = headers.index('Source Title')

    for publication in publications[1:]:
        publication[title_idx] = format_string(publication[title_idx])
        publication[authors_idx] = format_string(publication[authors_idx])
        publication[source_idx] = format_string(publication[source_idx])

    # Write to file
    filepath = './resnick-citations-cleaned.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-cleaned.csv')
    write_csv(filepath, publications[1:], headers)


if __name__ == '__main__':
    main()
