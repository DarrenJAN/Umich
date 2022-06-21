import json


def categorize_economy(country):
    """Combines The World Bank's Lower and Upper middle income categories into a
    single "Middle income" category. Returns an income group: "High income",
    "Middle income' or "Low income".

    Parameters:
        country (dict): representation of a country's economy

    Returns
       str: income group
    """

    if country['income_group'].lower() == 'high income':
        return 'High income'
    elif country['income_group'].lower() in ('lower middle income', 'upper middle income'):
        return 'Middle income'
    else:
        return 'Low income'

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
    """Entry point for program. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # 0.0 GET DATA
    countries = read_json('./wb-economies-2021_2022.json')
    groups = read_json('./wb-groups-2021_2022.json')
    country_indicators = read_json('./wb-indicators-dict-2019.json')


    # 1.2 SIMPLE EXAMPLE

    data = [
        ('Benin', 'BEN'),
        ("Cote d'Ivoire", 'CIV'),
        ('Gambia', 'GMB'),
        ('Ghana', 'GHA'),
        ('Guinea', 'GIN'),
        ('Guinea-Bissau', 'GNB'),
        ('Liberia', 'LBR'),
        ('Nigeria', 'NGA'),
        ('Senegal', 'SEN'),
        ('Sierra Leone', 'SLE'),
        ('Togo', 'TGO')
    ]

    west_africa_atlantic = None # TODO dict comp

    # print(f"\n1.2: List of tuples to dict = {west_africa_atlantic}")


    # 1.3 TRANSFORM VALUES

    data = {
        '2021': 0.024,
        '2020': 0.0125,
        '2019': 0.0181,
        '2018': 0.024399999999999998,
        '2017': 0.0213,
        '2016': 0.0126,
        '2015': 0.0012,
        '2014': 0.016200000000000003,
        '2013': 0.0146,
        '2012': 0.0207,
        '2011': 0.0316,
        '2010': 0.016399999999999998,
        '2009': -0.0036,
        '2008': 0.0384,
        '2007': 0.0285,
        '2006': 0.0323,
        '2005': 0.0339,
        '2004': 0.0268,
        '2003': 0.0227,
        '2002': 0.0159,
        '2001': 0.028300000000000002,
        '2000': 0.0338
    }

    inflation_rates = None # TODO list comp

    # print(f"\n1.3: US inflation rates = {inflation_rates}")


    # 2.0 CONDITIONAL STATEMENTS

    inflation_rates = None # TODO list comp

    # print(f"\n2.0: US inflation rates 2010-2021 = {inflation_rates}")

    # CHALLENGE 01

    south_asian_economies = {} # TODO implement list comp

    # Write to file
    # TODO Uncomment
    # write_json('./stu-south_asian_economies.json', south_asian_economies)


    # 2.1 IF-ELSE

    # south_asian_groups = {
    #     key: ('Middle income' if val['income_group'] in ('Upper middle income', 'Lower middle income')
    #     else 'Low income') for key, val in south_asian_economies.items()
    # }

    # # Write to file
    # write_json('./stu-south_asian_income_groups.json', south_asian_groups)

    south_asian_lending = {
        key: ('IDA' if val['lending_category'] in ('IDA', 'Blend') else 'IBRD')
        for key, val in south_asian_economies.items()
    }

    # Write to file
    # TODO Uncomment
    # write_json('./stu-south_asian_lending.json', south_asian_lending)


    # 2.2 IF-ELIF-ELSE (IF-ELSE-ELSE)

    country_income = {
        country['country_code'].upper(): ('High income' if country['income_group'] == 'High income'
        else 'Middle income' if country['income_group'] in ('Upper middle income', 'Lower middle income')
        else 'Low income')
        for country in countries
    }

    # Write to file
    # TODO Uncomment
    # write_json('./stu-country_income.json', country_income)

    # Delegate business logic to function
    country_income = None # TODO list comp

    # Write to file
    # TODO Uncomment
    # write_json('./stu-country_income-fx.json', country_income)


    # 2.3 NESTED LOOPS

    eu_countries = {}
    for group in groups:
        if group['group_code'] == 'EUU':
            for country in country_indicators:
                if group['country_code'] == country['country_code']:
                    eu_countries[country['country_code']] = country

    # print(f"\n2.3.1 for loop: EU country indicators (n={len(eu_countries)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-eu_country_indicators-for.json', eu_countries)

    eu_countries = {
        country['country_code']: country
        for group in groups
        for country in country_indicators
        if group['group_code'] == 'EUU' and group['country_code'] == country['country_code']
    }

    # print(f"\n2.3.2 dict comp: EU country indicators (n={len(eu_countries)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-eu_country_indicators-comp.json', eu_countries)


    # CHALLENGE 2.0

    china = read_json('./wb-indicators-dict-china-2019.json')

    china_pop_indicators = {} # TODO Implement list comp

    # Write to file
    write_json('./stu-china-pop_indicators.json', china_pop_indicators)


    # CHALLENGE 03

    east_asia_pop_indicators = {} # TODO Implement list comp

    # Write to file
    write_json('./stu-east_asia-pop_indicators-comp.json', east_asia_pop_indicators)


if __name__ == '__main__':
    main()