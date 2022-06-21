# LAB EXERCISE 10
import swapi_utils as utl

print('Lab Exercise 10\n')

# SETUP CODE

hero_homeworlds = {
    'luke': 'tatooine',
    'leia': 'alderaan',
    'chewbacca': 'kashyyyk',
    'han solo': 'corellia',
    'lando calrissian': 'socorro'
}

planet_filters = ('name', 'diameter', 'climate', 'terrain', 'population')

# END SETUP

# PROBLEM 3 (5 points)
def create_planet(planet, filters):
    """Loops over < planet >, then loops over < filters >. For each key in
    < planet > that exists in < filters >, converts data and assigns converted
    value to the same key in < new_planet > dictionary. If data is numeric,
    converts to type < int >. For data in the 'climate' and 'terrain' keys,
    splits data.

    Parameters:
        planet (dict): A SWAPI representation of a planet.
        filters (tuple): A tuple containing the names of the planet features.

    Returns:
        new_planet (dict): A dictionary containing filtered, converted planet data.
    """

    new_planet = {}
    
    for key, value in planet.items():
        if key in filters:
            if key == 'diameter' or key == 'population':
                planet[key] = int(value)
            elif key == 'climate' or key == 'terrain':
                planet[key] = value.split(', ')
            new_planet[key] = planet[key]
    return new_planet

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 02 (4 points)
    print("\nProblem 02:\n")
    homeworlds = []
    for key in hero_homeworlds.keys():
        value = hero_homeworlds[key]
        swapi_homeworld = utl.get_swapi_resource(f"{utl.ENDPOINT}/planets", {'search': value})['results'][0]
        homeworlds.append(swapi_homeworld)

    print(homeworlds)

    # Problem 03 (5 points)
    print("\nProblem 03:\n")
    # clean_homeworlds = []
    # for homeworld in homeworlds:
    #     temp = create_planet(homeworld, planet_filters)
    #     clean_homeworlds.append(temp)
    
    clean_homeworlds = [create_planet(homeworld, planet_filters) for homeworld in homeworlds]
    print(clean_homeworlds) 

    # Problem 04 (4 points)
    print("\nProblem 04:\n")
    # large_homeworlds = {}
    # for homeworld in clean_homeworlds:
    #     if homeworld['diameter'] >= 11000:
    #         name = homeworld['name']
    #         large_homeworlds[name] = homeworld
    
    large_homeworlds = {homeworld['name']:homeworld for homeworld in clean_homeworlds if homeworld['diameter'] >= 11000 }
    print(large_homeworlds) 

    # Problem 05 (3 points)
    print("\nProblem 05:\n")
    utl.write_json('stu_large_homeworlds.json', large_homeworlds)
if __name__ == "__main__":
    main()
