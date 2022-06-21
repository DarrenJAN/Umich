import csv
from os import remove
import string

print('PROBLEM SET 5\n')

# PROBLEM 1
def read_csv(filepath, encoding='utf-8-sig'):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file

    Returns:
        list: nested "row" lists
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        data = []
        reader = csv.reader(file_obj)
        for row in reader:
            data.append(row)
    return data

# PROBLEM 2
def clean_data(data):
    """
    Strips strings of leading and trailing whitespaces, converts numbers to integers,
    splits strings on a delimiter and converts the case of a string from the split string.

    Parameters:
        data (list): A list of lists, each representing a party's election results
    Returns:
        None
    """
    for info in data[1:]:
        info[0] = info[0].strip()
        info[1] = int(info[1])
        partylist = info[2].split('/')
        del info[2]
        info.append(partylist[0])
    
        name = partylist[1].split(' ')
        name = name[0].capitalize() + ' ' + name[1].capitalize()
        info.append(name)
    del data[0][-1]
    data[0].append('Position')
    data[0].append('Party Leader')

# PROBLEM 3
def get_leader_province(leader_provinces, party_info):
    """
    Adds the home province of a party leader to the list containing their party's election info.

    Parameters:
        leader_provinces (list): A list containing the names of party leaders and their home provinces.
        party_info (list): A list containing a party's information from a specific election.
    Returns:
        None
    """
    for info in leader_provinces[1:]:
        if(party_info[-1] == info[0]):
            party_info.append(info[1])

# PROBLEM 4
def get_seats_by_province(election_data, province):
    """
    Gets the total seats for parties whose leaders are from a specific province.

    Parameters:
        election_data (list): A list of lists containing information from a specific election.
        province (str): The name of a province.
    Returns:
        (int): The total number of seats for parties whose leaders are from the given province.
    """
    province_seats = 0
    for ele in election_data[1:]:
        if ele[-1].lower() == province.lower():
            province_seats += ele[1]
    return province_seats


# PROBLEM 5
def get_seat_difference(prev_election_data, party_info):
    """
    Adds the difference in seats between two elections for a party to that party's info list.

    Parameters:
        prev_election_data (list): A list of lists containing information from a specific election.
        party_info (list): A list containing a party's information from a specific election.
    Returns:
        (int): An integer value of the seat difference for a party between the current and previous election.
    """

    for prev_data in prev_election_data[1:]:
        if prev_data[0] == party_info[0]:
            return party_info[1] - prev_data[1]

# PROBLEM 6
def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

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
    """
    Serves as the main point of entry point of the program.
    """

    #PROBLEM 1.2
    print('\nProblem 1:\n')
    filepath2014 = './election_data_2014.csv'
    filepath2019 = './election_data_2019.csv'
    election_data_2014 = []
    election_data_2019 = []

    election_data_2014 = read_csv(filepath2014)
    election_data_2019 = read_csv(filepath2019)
    print(f"\nelection_data_2014 = {election_data_2014}")
    print(f"\nelection_data_2019 = {election_data_2019}")

    #PROBLEM 2.2
    print("\nProblem 2:\n")
    clean_data(election_data_2014)
    clean_data(election_data_2019)
    print(f"\nelection_data_2014 = {election_data_2014}")
    print(f"\nelection_data_2019 = {election_data_2019}")

    # PROBLEM 3.2
    print('\nProblem 3:\n')
    home_provinces = []
    home_provinces = read_csv('./leader_home_provinces.csv')

    for  ele in election_data_2014[1:]:
        get_leader_province(home_provinces, ele) 
    for  ele in election_data_2019[1:]:
        get_leader_province(home_provinces, ele)

    print(f"\nhome_provinces = {home_provinces}")
    print(f"\nelection_data_2014 = {election_data_2014}")
    print(f"\nelection_data_2019 = {election_data_2019}")

    # PROBLEM 4.2
    print('\nProblem 4:\n')
    kn_seats_2014 = get_seats_by_province(election_data_2014, 'kwazulu-natal')
    gauteng_seats_2019 = get_seats_by_province(election_data_2019, 'GAUTENG')
    print(f"\nkn_seats_2014 = {kn_seats_2014}")
    print(f"\ngauteng_seats_2019 = {gauteng_seats_2019}")

    # PROBLEM 5.2
    print('\nProblem 5:\n')
    for cur_ele_data in election_data_2019:
        difference = get_seat_difference(election_data_2014, cur_ele_data)
        cur_ele_data.append(difference)
    print(f"\nelection_data_2019 = {election_data_2019}")

    # PROBLEM 6.2
    filepathnew2019 = './final_election_data_2019.csv'
    write_csv(filepathnew2019, election_data_2019[1:], headers=election_data_2019[0])

# WARN: do not modify or remove the following if statement.


if __name__ == '__main__':
    main()