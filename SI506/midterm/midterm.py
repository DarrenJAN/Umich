import csv
from email import header


def classify_county_vax_level(county, headers, column_name):
    """Classifies a county according to a three-tiered ranking scheme.
    Classification of a target population (e.g., residents 65 years and older)
    is based on the corresponding "Series_Complete_*" column name passed in by
    the caller. Delegates to < get_county_attribute > the task of returning the
    (converted) percentage value of the county's target population who are fully
    vaccinated.

    Classifying a county is based on the following scheme.

    Tiers:
        High: greater than or equal to 75% of target population vaccinated fully
        Moderate: greater than or equal to 50% but less than 75% of target population
                  vaccinated fully
        Low: less than 50% of target population vaccinated fully

    Once the county is classified the function returns to the caller one of
    three labels: 'High', 'Moderate', 'Low'.

    Parameters:
        county (list): county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        str: classification label
    """
    num = get_county_attribute(county, headers, column_name)
    if num >= 75:
        return 'High'
    elif num < 50:
        return 'Low'
    else:
        return 'Moderate'


def clean_county_data(county):
    """Mutates the passed in < county> list by converting numbers masquerading as
    strings to either an integer or float depending on whether or not the string
    representing a number that contains a fractional component (i.e., decimal).

    Checks each string element in the < county > list. Delegates to the function
    < is_floating_point_number > the task of confirming whether or not the string represents a
    float. If the expression evaluates to True, the string is converted to a
    float and assigned to the element. Delegates to the function < is_whole_number > the
    task of confirming whether or not the string represents an integer. If the
    expression evaluates to True, the string is converted to a
    int and assigned to the element. If the string does not represent a number
    it is ignored.

    Parameters:
      county (list): county-specific vaccination data

    Returns:
        None
    """

    for i in range(len(county)):
        if is_floating_point_number(county[i]):
            county[i] = float(county[i])
        elif is_whole_number(county[i]):
            county[i] = int(county[i])


def count_vax_adults_18to64(counties, headers):
    """Accumulates a count of all residents considered fully vaccinated between the
    ages of 18 and 64 (inclusive) across all < counties > provided by the caller.
    Delegates to < get_county_attribute > the task of retrieving each county's
    "Series_Complete_18Plus" and "Series_Complete_65Plus" values.

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file

    Returns
        int: count of fully vaccinated residents between the ages of 18 and 64
    """

    result = 0
    for country in counties:
        num65 = get_county_attribute(country, headers, 'Series_Complete_65Plus')
        num18 = get_county_attribute(country, headers, 'Series_Complete_18Plus')
        result += (num18- num65)
    return result


def get_counties_by_ur_codes_and_vax_level(counties, headers, ur_codes, vax_level='Low'):
    """Returns a list comprising zero or more formatted strings representing counties
    filtered on a tuple of urban/rural < ur_codes > and a < vax_level > code. The
    passed in < headers > list is employed to look up index values associated with
    the nested county elements.

    String format:
        Each "county" list element string is formatted as follows:

        < Recip_County > (< UR_Code >-< UR_Code_Name >) vax level: < Vax_Level >

        Example: "Lapeer County (2-Large fringe metro) vax level: Low"

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        ur_codes (tuple): comprises one or more integer UR Code items
        vax_level (str): Three-tiered ranking scheme: High, Moderate, Low.
                         Default = "Low"

    Returns:
        list: formatted "county" strings
    """
    recip_index = headers.index("Recip_County")
    vax_index = headers.index("Vax_Level")
    code_index = headers.index("UR_Code")
    name_index = headers.index("UR_Code_Name")
    result = []

    for country in counties:
        if (country[code_index] in ur_codes) and country[vax_index] == vax_level:
            str = f"{country[recip_index]} ({country[code_index]}-{country[name_index]}) vax level: {country[vax_index]}"
            result.append(str)
    return result

def get_counties_with_lowest_vax_rate(counties, headers, column_name):
    """Returns a list comprising one or more formatted strings representing counties
    with the lowest vaccination rate for a designated age group. Ties are accomodated.
    Delegates to < get_county_attribute > the task of returning the county vaccination
    rate for a given age group. The age group is determined by passing to
    < get_county_attribute > the < headers > and a "*_Pop_Pct" < column_name > string
    as arguments.

    Acceptable < column_name > values include:

    Series_Complete_Pop_Pct
    Series_Complete_12PlusPop_Pct
    Series_Complete_18PlusPop_Pct
    Series_Complete_65PlusPop_Pct

    String format:
        Each "county" list element string is formatted as follows:

        < Recip County > (< rate >%)

        Example: "Hillsdale County (70.9%)"

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        list: formatted "county" strings
    """
    list = []
    min_percentage =  1000
    min_name = ""
    for country in counties:
        percentage = get_county_attribute(country, headers, column_name)
        if(percentage < min_percentage):
            list = []
            min_name = country[3]
            min_percentage = percentage
            str = f"{min_name} ({min_percentage}%)"
            list.append(str)
        elif(percentage == min_percentage):
            str = f"{country[3]} ({min_percentage}%)"
            list.append(str)
    return list


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

    for country in counties:
         if country[3].lower() == county_name.lower():
            return country


def get_county_attribute(county, headers, column_name):
    """Returns a < county > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        county (list): county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        str: element sourced from passed in publication list
    """
    return county[headers.index(column_name)]


def get_county_nchs_codes(nchs_codes, county):
    """Returns the NCHS urban/rural codes and descriptors, comprising the
    < cbsa_title >, < ur code > (converted to int), and < ur code_name >
    associated with the matching county name value derived from the passed in
    < county > list. Name matching is case-insensitive. If no match is
    obtained the function returns None.

    Parameters:
        nchs_codes (list): nested lists of NCHS urban/rural codes and descriptors
        county (list): county-specific vaccination data

    Returns:
        tuple: three-item tuple containing the < cbsa_title >, < code >, and
               < code_name > for a given county
    """
    for code in nchs_codes:
        if code[1].lower() == county[3].lower():
            cur_tuple = tuple([code[2], code[3], code[4]])
    
    return cur_tuple


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


def is_whole_number(string):
    """Checks if a whole number (i.e., an integer) is masquerading as a string.

    WARN: function relies on str.isnumeric() behavior. Strings like "24.5" and
    "-1" are not considered numeric due to the presence of the period ('.') and
    the dash ('-') respectively.

    Parameters:
        string (str): Non-decimal number (e.g., '55363') cast as a string

    Returns:
        bool: True if string can be converted to an integer; False otherwise.

    """

    try:
        return True if string.isnumeric() and int(string) else False # ternary operator
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
    filepath = './mi-covid-washtenaw-20220220.csv'
    
    wash_data = read_csv(filepath) # TODO Call function

    max_positivity_rates = wash_data[1:7] # TODO Assign

    # week_04 = wash_data[13:20] # TODO Assign
    week_04 = wash_data[-8:-1] # TODO Assign

    odd_days = wash_data[1::2] # TODO Assign

    print(f"\nelection_data_2014 = {wash_data}")
    print(f"\nmax_positivity_rates = {max_positivity_rates}")
    print(f"\nweek_04 = {week_04}")
    print(f"\nwodd_days = {odd_days}")
    # CHALLENGE 02

    # CDC County vaccination data
    vax_data = read_csv('./mi-covid-vax_counties-20220219.csv') # TODO Call function
    vax_headers = vax_data[0] # TODO Assign
    vax_counties = vax_data[1:] # TODO Assign

    # TODO Implement function < get_county >

    jackson_cty = get_county(vax_counties, 'jackson county') # TODO Call function


    print(f"\n vax_data = {vax_data}")
    print(f"\n jackson_cty = {jackson_cty}")
    # CHALLENGE 03

    # TODO Implement function < get_county_attribute >

    jackson_cty_vax_complete_pct = float(get_county_attribute(jackson_cty, vax_headers, 'Series_Complete_Pop_Pct')) # TODO Call function
    print(f"\nChallenge 03: jackson_cty_vax_complete_pct = {jackson_cty_vax_complete_pct}")


    # CHALLENGE 04

    # TODO Implement function < clean_county_data >

    # TODO Implement loop
    for country in vax_counties:
        clean_county_data(country)
    print(f"\nChallenge 04: vax_counties = {vax_counties}")

    # CHALLENGE 05

    vax_adults_18to64 = count_vax_adults_18to64(vax_counties, vax_headers) # TODO Call function

    print(f"\nChallenge 05: vax_adults_18to64 = {vax_adults_18to64}")


    # CHALLENGE 06

    # TODO Implement function < classify_county_vax_level >

    # TODO Implement loop
    for country in vax_counties:
        label = classify_county_vax_level(country, vax_headers, 'Series_Complete_Pop_Pct')
        country.insert(5, label)
    
    # TODO Update headers
    vax_headers.insert(5, "Vax_Level")
    # TODO Write to file
    write_csv('stu-vax_levels.csv', vax_counties, vax_headers)
    print(f"\nChallenge 06: vax_counties[1] = {vax_counties[1]}")

    # CHALLENGE 07

    # NCHS County UR codes
    nchs_codes_data = read_csv('./mi-nchs-urban_rural_codes.csv')  # TODO Call function
    nchs_codes_headers = nchs_codes_data[0] # TODO Assign
    nchs_codes = nchs_codes_data[1:] # TODO Assign
    print(f"\nChallenge 07: nchs_codes[1] = {nchs_codes[1]}")

    # TODO Implement function < get_county_nchs_codes >

    ingham_cty = get_county(vax_counties, 'Ingham County') # TODO Call function
    ingham_cty_ur_code = get_county_nchs_codes(nchs_codes, ingham_cty) # TODO Call function
    print(f"\nChallenge 07: ingham_cty = {ingham_cty}")
    print(f"\nChallenge 07: ingham_cty_ur_code = {ingham_cty_ur_code}")


    # CHALLENGE 08

    # TODO Implement function < get_counties_with_lowest_vax_rate >

    lowest_vax_rates_12_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, "Series_Complete_12PlusPop_Pct") # TODO Call function

    lowest_vax_rates_18_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, "Series_Complete_18PlusPop_Pct")  # TODO Call function

    lowest_vax_rates_65_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, "Series_Complete_65PlusPop_Pct")  # TODO Call function
    print(f"\nChallenge 08: lowest_vax_rates_12_plus = {lowest_vax_rates_12_plus}")
    print(f"\nChallenge 08: lowest_vax_rates_18_plus = {lowest_vax_rates_18_plus}")
    print(f"\nChallenge 08: lowest_vax_rates_65_plus = {lowest_vax_rates_65_plus}")


    # CHALLENGE 09

    # TODO Implement loop
    for vax_country in vax_counties:
        cur_tuple = get_county_nchs_codes(nchs_codes, vax_country)
        (cbsa_title, ur_code, ur_code_name) = cur_tuple
        vax_country.insert(5, cbsa_title)
        vax_country.insert(6, int(ur_code))
        vax_country.insert(7, ur_code_name)

    # TODO Update headers
    vax_headers.insert(5, 'CBSA_Title')
    vax_headers.insert(6, 'UR_Code')
    vax_headers.insert(7, 'UR_Code_Name')
    # TODO Write to file
    write_csv('stu-ur_vax_levels.csv', vax_counties, vax_headers)

    print(f"\nChallenge 09: vax_header = {vax_headers}")
    print(f"\nChallenge 09: vax_counties[1] = {vax_counties[1]}")


    # CHALLENGE 10

    # TODO Implement function < get_counties_by_ur_codes_and_vax_level >

    tuple1 = tuple([1,2])
    tuple2 = tuple([6])
    metro_moderate_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, tuple1, "Moderate") # TODO Call function

    metro_low_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, tuple1) # TODO Call function

    noncore_low_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, tuple2) # TODO Call function
   
    print(f"\nChallenge 10: metro_moderate_vax_rates = {metro_moderate_vax_rates}")
    print(f"\nChallenge 10: metro_low_vax_rates = {metro_low_vax_rates}")
    print(f"\nChallenge 10: noncore_low_vax_rates = {noncore_low_vax_rates}")

    dict = {'1':2}
    dict[3] = 10
    dict['jack'] = 3
    print(f"dict[1]={dict['jack']}")
    for k, v in dict.items():
        print(f"k, v = {k} {v} ")

    a = [100,4,5]
    a.sort()
    print(a)
    

# Do not modify or remove this if statement
if __name__ == '__main__':
    main()

