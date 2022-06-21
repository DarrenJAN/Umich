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

    print(f"\n1.0 Sites list length = {len(sites)}")

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
    write_dicts_to_csv('stu-china-earliest.csv', china_sites, china_sites[0].keys())


    # 2.0 DICTIONARIES AND THE ACCUMULATOR PATTERN

    china_counts = {}
    for site in sites:
        if site['states_name_en'].lower() == 'china':
            year = site['date_inscribed'] # str
            if year not in china_counts.keys():
                china_counts[year] = 1 # seed
            else:
                china_counts[year] += 1 # increment

    print(f"\n2.0 China counts (unordered) = {china_counts}")

    # Write to file
    filepath = 'stu-china-counts.csv'
    # WARN: must pass a list of dictionaries
    write_dicts_to_csv(filepath, [china_counts], china_counts.keys())

    # BONUS: reorder dictionary by keys (year)
    china_counts = dict(sorted(china_counts.items(), key=lambda x: x[0]))

    # Alternative: dictionary comprehension (preferred)
    # china_counts = {k: v for k, v in sorted(china_counts.items(), key=lambda x: x[0])}

    print(f"\n2.0 China counts sorted = {china_counts}")

    # Write to file
    filepath = 'stu-china-counts_sorted.csv'
    # WARN: must pass a list of dictionaries
    write_dicts_to_csv(filepath, [china_counts], china_counts.keys())


    # CHALLENGE 01

    usa_sites = []
    for site in sites:
        if site['undp_code'] == 'usa' and site['category'] in ('Natural', 'Mixed'):
            usa_sites.append(site)

    # Alternative
    # usa_sites = []
    # for site in sites:
    #     if (site['undp_code'] == 'usa' and
    #         (site['category'] == 'Natural' or site['category'] == 'Mixed')):
    #         usa_sites.append(site)


    print(f"\nTYPE = {type(usa_sites[0].keys())}")

    # Write to file
    filepath = 'stu-usa-nat_mix.csv'
    write_dicts_to_csv(filepath, usa_sites, usa_sites[0].keys())


    # CHALLENGE 02

    region_counts = {}
    for site in sites:
        region = site['region_en']
        if region not in region_counts.keys():
            region_counts[region] = 1
        else:
            region_counts[region] += 1

    print(f"Ch 02. Region counts\n")
    pp.pprint(region_counts)

    # BONUS: sort by value
    region_counts = {k: v for k, v in sorted(region_counts.items(), key=lambda x: x[1], reverse=True)}

    print(f"Ch 02. Region counts (sorted)\n")
    pp.pprint(region_counts)


    # CHALLENGE 03

    endangered_sites = []
    for site in sites:
        if site['endangered'] == '1':
            endangered_sites.append(
                {
                    'id_no': site['id_no'],
                    'category': site['category'],
                    'name_en': site['name_en'],
                    'region_en': site['region_en'],
                    'states_name_en': site['states_name_en']
                }
            )

    # Write to file
    filepath = 'stu-endangered.csv'
    write_dicts_to_csv(filepath, endangered_sites, endangered_sites[0].keys())


    # CHALLENGE 04

    endangered_counts = {}
    for site in endangered_sites:
        if site['region_en'] not in endangered_counts.keys():
            endangered_counts[site['region_en']] = 1 # seed
        else:
            endangered_counts[site['region_en']] += 1 # increment

    # BONUS: sort counts descending order
    endangered_counts = dict(sorted(endangered_counts.items(), key=lambda x: x[1], reverse=True))

    print(f"\nCh 04. Endangered site counts by region\n")
    pp.pprint(endangered_counts)

    # Add 3 Ukrainian sites to the Europe and North America count
    endangered_counts['Europe and North America'] += 3

    print(f"\nCh 04. Endangered site counts by region + Ukraine\n")
    pp.pprint(endangered_counts)

    # Total count of endangered sites.
    count = sum(endangered_counts.values()) # call functions once, not multiple times inside loop

    print(f"\nCh 04. Endangered site count = {count}")

    for key, val in endangered_counts.items():
        endangered_counts[key] = round(int(val)/count * 100, 2)

    print(f"\nCh 04. Endangered site by region (percent)\n")
    pp.pprint(endangered_counts)


if __name__ == '__main__':
    main()
