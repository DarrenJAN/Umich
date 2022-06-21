# SI 506 Lecture 17

import csv
import pprint
from datetime import datetime


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
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

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


    # 1.0 CSV.READER() AND CSV.WRITER()

    # Get UNESCO World heritage sites
    sites = read_csv_to_dicts('./whc-countries-2022.csv')

    # print(f"\n1.0 Sites list length = {len(sites)}")

    china_sites = []
    year = datetime.today().year # Return current year
    for site in sites:
        date_inscribed = int(site['date_inscribed']) # convert
        if site['states_name_en'].lower() == 'china' and date_inscribed < year:
            china_sites.clear() # reset
            china_sites.append(site)
            year = date_inscribed
        elif site['states_name_en'].lower() == 'china' and date_inscribed == year:
            china_sites.append(site)
        else:
            continue # else optional but explicit

    # Write to file
    # TODO Uncomment
    # write_dicts_to_csv('stu-china-earliest.csv', china_sites, china_sites[0].keys())


    # 2.0 DICTIONARIES AND THE ACCUMULATOR PATTERN

    china_counts = {}

    # TODO Implement loop

    # print(f"\n2.0 China counts (unordered) = {china_counts}")

    # Write to file
    filepath = 'stu-china-counts.csv'
    # WARN: must pass a list of dictionaries
    # TODO Uncomment
    # write_dicts_to_csv(filepath, [china_counts], china_counts.keys())

    # BONUS: reorder dictionary by keys (year)
    # TODO Uncomment
    # china_counts = dict(sorted(china_counts.items(), key=lambda x: x[0]))

    # Alternative: dictionary comprehension (preferred)
    # TODO Uncomment
    # china_counts = {k: v for k, v in sorted(china_counts.items(), key=lambda x: x[0])}

    # print(f"\n2.0 China counts sorted = {china_counts}")

    # Write to file
    filepath = 'stu-china-counts_sorted.csv'
    # WARN: must pass a list of dictionaries
    # TODO Uncomment
    # write_dicts_to_csv(filepath, [china_counts], china_counts.keys())


    # CHALLENGE 01

    usa_sites = []

    # TODO Implement loop

    # Write to file
    filepath = 'stu-usa-nat_mix.csv'

    # TODO Call function


    # CHALLENGE 02

    region_counts = {}

    # TODO Implement loop

    # print(f"Ch 02. Region counts\n")
    # pp.pprint(region_counts)

    # BONUS: sort by value
    region_counts = None # TODO sort or comment out

    # print(f"Ch 02. Region counts (sorted)\n")
    # pp.pprint(region_counts)


    # CHALLENGE 03

    endangered_sites = []

    # TODO Implement loop

    # Write to file
    filepath = 'stu-endangered.csv'

    # TODO Call function

    # CHALLENGE 04

    endangered_counts = {}

    # TODO Implement loop

    # BONUS: sort counts descending order
    endangered_counts = None # TODO sort or comment out

    # print(f"\nCh 04. Endangered site counts by region\n")
    pp.pprint(endangered_counts)

    # Add 3 Ukrainian sites to the Europe and North America count

    # TODO Europe and North America increment count

    # print(f"\nCh 04. Endangered site counts by region + Ukraine\n")
    # pp.pprint(endangered_counts)

    # Total count of endangered sites.
    count = None # call functions once, not multiple times inside loop

    # print(f"\nCh 04. Endangered site count = {count}")

    # TODO Implement loop

    # print(f"\nCh 04. Endangered site by region (percent)\n")
    # pp.pprint(endangered_counts)


if __name__ == '__main__':
    main()
