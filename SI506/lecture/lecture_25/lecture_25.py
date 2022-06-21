# SI 506 Lecture 25

import lecture_25_utils as utl


def create_film(data):
    """Returns a new film dictionary from the passed in < data >.

    Key order:
        url
        title
        director
        release_date
        opening_crawl

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    pass # TODO Implement


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible. Delegates to the function
    < create_film > the task of creating film dictionaries.

    Type conversions:
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> top_speed_mglt (str to int)
        crew -> crew_size (str to int)
        armament -> armament (str to list)

    Key order:
        url
        name
        model
        starship_class
        hyperdrive_rating
        top_speed_mglt
        crew_size
        armament
        film_credits

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    pass # TODO Implement


def main():
    """Entry point for the script.

    Paramters:
        None

    Returns:
        None
    """

    # CHALLENGES 01-06

    swapi_starships = None # TODO Call function
    wookiee_starships = None # TODO Call function

    # WARN: Run first then comment out
    starships = [] # TODO Create new list

    # Write to file
    utl.write_json('stu-starships.json', starships)
    utl.write_json('stu-cache.json', utl.cache)


if __name__ == '__main__':
    main()
