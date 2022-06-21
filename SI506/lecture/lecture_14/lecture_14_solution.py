import csv


def convert_to_float(county):
    """Mutates the passed in < county> list by converting floating point numbers
    (i.e., numbers containing a fractional component) masquerading as strings
    to type float.

    Checks each string element in the < county > list. Delegates to the function
    < is_floating_point_number > the task of confirming whether or not the string
    represents a float. If the expression evaluates to True, the string is
    converted to a float and assigned to the element. If the string does not
    represent a floating point number it is ignored.

    Parameters:
      county (list): county-specific vaccination data

    Returns:
        None
    """

    for i in range(len(county)):
        if is_floating_point_number(county[i]):
            county[i] = float(county[i])


def get_county(counties, county_name):
    """Employs the passed in < county_name > as a filter in order to return
    the corresponding county element from the passed in list of counties. Name
    matching is case-insensitive. If no match is obtained the function returns
    None.

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        county_name (str): name of county

    Returns:
        county (list): county list with a name value that matches the < county_name >
    """

    for county in counties:
        if county[3].lower() == county_name.lower():
            return county


def get_attribute(county, headers, column_name):
    """Returns a < county > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        county (list): county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): provides header value used to look up the index value
                           of the target element

    Returns:
        str: element sourced from passed in publication list
    """

    return county[headers.index(column_name)]


def get_nchs_code(nchs_codes, county):
    """Returns the NCHS urban/rural codes and descriptors, comprising the
    < code > and < code_name > associated with the matching
    county name value derived from the passed in < county > list. Name matching
    is case-insensitive. If no match is obtained the function returns None.

    Parameters:
        nchs_codes (list): nested lists of NCHS urban/rural codes and descriptors
        county (list): county-specific vaccination data

    Returns:
        tuple: tuple containing the < code >, and < code_name > for a given county
    """

    for code in nchs_codes:
        if code[0].lower() == county[3].lower():
            # return tuple(code[1:]) # Nice
            return code[1], code[2]


def is_floating_point_number(string):
    """Checks if a floating point number (e.g., a number that includes a fractional
    component) is masquerading as a string.

    WARN: function relies on str.isnumeric() behavior. Strings like "24.5" and
    "-1" are not considered numeric due to the presence of the period ('.') and
    the dash ('-') respectively.

    Parameters:
        string (str): Non-decimal number (e.g., '55363') cast as a string

    Returns:
        bool: True if string is a number with a decimal component; False otherwise.
    """

    try:
        return True if not string.isnumeric() and float(string) else False # ternary operator
    except ValueError:
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
    """Entry point for script.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    # Washtenaw County COVID-19 community spread data
    wash_data = read_csv('mi-covid-washtenaw-202111.csv')

    # print(f"\nChallenge 01 Washtenaw Cty Community Spead\n{wash_data}")

    # Source: https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T/8396-v7yb

    # Test Percent Positivity Metric: day with hightest percentage of positive tests over the
    # previous 7 days (column = percent_test_results_reported_positive_last_7_days)

    max_pos_tests = wash_data[-2]
    # max_pos_tests = wash_data[19] # Alternative

    # print(f"\nChallenge 01: Nov. highest test positivity = {max_pos_tests} ")

    # Return data for week of 07-13 November using slicing (no loop)
    week_02 = wash_data[7:14]
    # week_02 = wash_data[-14:-7] # Alternative

    # print(f"\nChallenge 01: Nov. week 02 data = {week_02} ")

    # Reverse order (includes header row)
    reverse_order = wash_data[::-1]

    # print(f"\nChallenge 01: Reverse order = {reverse_order}")

    # Reverse order of daily records, excluding header row
    days_len = len(wash_data[1:])
    wash_data_reversed = wash_data[days_len:0:-1]
    wash_data_reversed.insert(0, wash_data[0]) # add header row

    # print(f"\nChallenge 01: BONUS wash_data_reversed = {wash_data_reversed}")


    # CHALLENGE 02

    # CDC County vaccination data
    vax_data = read_csv('mi-covid-vax_counties-202111.csv')
    vax_headers = vax_data[0]

    # print(f"Challenge 02. vax headers = {vax_headers}")

    vax_counties = vax_data[1:]

    # print(f"\nChallenge 02 Vax data\n{vax_data}")

    washtenaw_cty = get_county(vax_counties, 'washtenaw county') # Pass in lower case

    print(f"\nChallenge 02: Washtenaw County = {washtenaw_cty}")


    # CHALLENGE 03

    washtenaw_cty_vax_complete_pct = float(get_attribute(washtenaw_cty, vax_headers, 'Series_Complete_Pop_Pct'))

    # print(f"\nChallenge 03: Washtenaw County vax complete pct = {washtenaw_cty_vax_complete_pct}")


    # CHALLENGE 04

    for county in vax_counties:
        convert_to_float(county)

    print(f"\nCh 04 Clean counties = {vax_counties}")


    # CHALLENGE 05

    outliers = []
    for county in vax_counties:
        rate = get_attribute(county, vax_headers, 'Series_Complete_18PlusPop_Pct')
        if 50.0 < rate < 70.0:
            continue # proceed to next iteration immediately
        outliers.append(county)

    print(f"\nCh05 Outlier counties = {outliers}")


    # CHALLENGE 06

    # NCHS County UR codes
    nchs_codes_data = read_csv('mi-nchs-urban_rural_codes.csv')
    nchs_codes = nchs_codes_data[1:]

    # for code in nchs_codes:
    #     print(f"CODE LIST LEN = {len(code)}")

    # for row in vax_counties:
    #     print(f"COUNTY LIST LEN = {len(row)}")

    for i in range(len(vax_counties)):
        code, descriptor = get_nchs_code(nchs_codes, vax_counties[i])
        vax_counties[i].insert(5, code)
        vax_counties[i].insert(6, descriptor)

        # Alternative (Pythonic)
        # vax_counties[i][5:5] = code, descriptor # slice assignment

    # Update the headers
    vax_headers.insert(5, 'UR_Code')
    vax_headers.insert(6, 'UR_Code_Name')

    # Alternative (Pythonic)
    # vax_headers[5:5] = 'UR_Code', 'UR_Code_Name' # slice assignment

    # Write to file
    write_csv('stu-vax_ur_counties.csv', vax_counties, vax_headers)


if __name__ == '__main__':
    main()