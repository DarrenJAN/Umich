# SI 506 Lecture 19

import csv
import json


def get_article_subjects(article):
    """Returns a list of "subject" string values retrieved from the passed in
    < article >'s "keywords" list.

    Parameters:
        article (dict): representation of an article

    Returns:
        list: list of "subject" strings associated with the < article >
    """

    subjects = []
    for keyword in article['keywords']:
        if keyword['name'] == 'subject':
            subjects.append(keyword['value'])
    return subjects


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


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


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    # Get articles
    articles = read_json('./nyt-articles-200.json')

    print(f"\nCh 01 Articles (n={len(articles)})")

    subject_counts = {}
    for article in articles:
        article_subjects = get_article_subjects(article)
        for subject in article_subjects:
            if subject not in subject_counts.keys():
                subject_counts[subject] = 1 # seed
            else:
                subject_counts[subject] += 1 # increment

    # Sort by value (reversed = -x[1]), then by key (x[0])
    subject_counts = {k: v for k, v in sorted(subject_counts.items(), key=lambda x: (-x[1], x[0]))}

    # Write to file
    write_json('stu-nyt-subject_counts.json', subject_counts)


    # CHALLENGE 02

    authors = []
    for article in articles:
        for person in article['byline']['person']:
            name = (person['lastname'], person['firstname'], person['middlename'])
            if name not in authors:
                authors.append(name)

    print(f"\nauthors (n={len(authors)})")

    # Sort Authors
    # WARN: convert None to empty string to avoid runtime exception (middlename value)
    # str(x or '') returns '' if x is falsy
    # TypeError: '<' not supported between instances of 'NoneType' and 'str'
    authors = [author for author in sorted(authors, key=lambda x: (x[0], x[1], str(x[2] or '')))]

    # print(f"\nAuthors = {authors}")

    write_csv('stu-nyt-authors.csv', authors, ['last_name', 'first_name', 'middle_name'])


    # CHALLENGE 03

    citations = {}
    for article in articles:
        for person in article['byline']['person']:
            name = [person['lastname'], person['firstname'], person['middlename']]

            # Clean: At least one duplicate entry due to uppercase last name
            for i in range(len(name)):
                if name[i] and name[i].isupper():
                    name[i] = name[i].capitalize()

            # Clean: At least one duplicate entry due to uppercase last name
            # WARN: this alternative changes DeWall to Dewall (suboptimal)
            # name = (person['lastname'].capitalize(), person['firstname'].capitalize(), str(person['middlename'] or '').capitalize())

            # Format key
            if name[2]:
                key = '_'.join(name)
            else:
                key = f"{name[0]}_{name[1]}" # Ignore blank middle name

            # Format value
            val  = f"{article['pub_date']} - {article['headline']['main']}"

            if key not in citations.keys():
                citations[key] = [val] # new list literal
            else:
                citations[key].append(val)

    # Sort Authors
    citations = {k: v for k, v in sorted(citations.items(), key=lambda x: x[0])}

    write_json('stu-nyt-citations.json', citations)


    # CHALLENGE 04

    # TODO Refactor Challenge 03 loop

    # TODO Uncomment after refactor
    # print(f"\nCh 03 Benedict Carey authored articles = {len(citations['Carey_Benedict'])}")


if __name__ == '__main__':
    main()