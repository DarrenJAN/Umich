import sw_utils as utl


def assign_crew_members(starship, crew_positions, personnel):
    """Maps crew members by position to the passed in < starship > 'crew_members'
    key. Both the < crew_positions > and < personnel > lists should contain the same number
    of elements. The individual < crew_positions > and < personnel > elements are then paired
    by index position and stored in a dictionary structured as follows:

    {< crew_position[0] >: < personnel[0] >, < crew_position[1] >: < personnel[1] >, ...}

    The crew members dictionary is mapped (i.e., assigned) to the passed in
    starship's 'crew_members' key and the crewed starship is returned to the caller.

    WARN: The number of crew members that can be assigned to the passed in < starship > is
    limited by the starship's "crew_size" value. No additional crew members are permitted
    to be assigned to the < starship >.

    WARN: A single line dictionary comprehension that assigns a new dictionary to the passed in
    < starship >'s "crew_members" key must be written in order to earn full credit. Utilize the
    parameter names in the dictionary comprehension (DO NOT assign the passed in dictionary
    and lists to local variables and then reference them in the comprehension).

        Parameters:
            starship (dict): Representation of a starship
            crew_positions (list): crew positions (e.g., 'pilot', 'copilot', etc.)
            personnel (list): persons to be assigned to the crew positions

        Returns:
            dict: starship with assigned crew members
    """

    starship['crew_members'] = {crew_positions[i]: personnel[i] for i in range(starship['crew_size'])}
    return starship


def board_passengers(starship, passengers):
    """Assigns < passengers > to the passed in < starship > but limits boarding to less than
    or equal to the starship's "max_passengers" value. The passengers list (in whole or in part)
    is then mapped (i.e., assigned) to the passed in starship's 'passengers_on_board' key. After
    boarding the passengers the starship is returned to the caller.

    WARN: The number of passengers permitted to board a starship is limited by the starship's
    "max_passengers" value. If the number of passengers attempting to board exceeds the starship's
    "max_passengers" value only the first n passengers (where `n` = "max_passengers") are
    permitted to board the vessel.

        Parameters:
            starship (dict): Representation of a starship
            passengers (list): passengers to transport aboard starship

        Returns:
            dict: starship with assigned passengers
    """

    count = 0 
    for passenger in passengers:
        if count == starship["max_passengers" ]:
            break
        else:
            count += 1
            if(starship['passengers_on_board'] == None ):
                starship['passengers_on_board'] = []
            starship['passengers_on_board'].append(passenger)
    
    return starship


def calculate_articles_mean_word_count(articles):
    """Calculates the mean (e.g., average) word count of the passed in list of < articles >.
    Excludes from the calculation any article with a word count of zero (0). Word counts
    are summed and then divided by the number of non-zero word count articles. The resulting mean
    value is rounded to the second (2nd) decimal place and returned to the caller.

    WARN: Add a local variable to hold a count of the number of articles with a word count of
    zero (0). Then subtract the zero word count from the total number of passed in articles in
    order to ensure that the divisor reflects the actual number of articles upon which to
    compute the mean.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        float: mean word count rounded to the second (2nd) decimal place
    """

    zero_count = 0
    total_count = 0
    word_count = 0

    for article in articles:
        total_count += 1
        if article['word_count'] == 0:
            zero_count += 1
        else:
            word_count += article['word_count']
    
    return round(word_count / (total_count - zero_count), 2)


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the < utl.convert_to_* > functions the task of
    converting the specified strings to either int, float, or list (or None if utl.convert_to_none
    is eventually called).

    Conversions:
        str to int: 'series_season_num', 'series_episode_num', 'season_episode_num'
        str to float: 'episode_prod_code', 'episode_us_viewers_mm'
        str to list: 'episode_writers'

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """

    for episode in episodes:
        for key, value in episode.items():
            if key == 'series_season_num' or key == 'series_episode_num' or key == 'season_episode_num':
                episode[key] = utl.convert_to_int(value)
            elif key == 'episode_prod_code' or key == 'episode_us_viewers_mm':
                episode[key] = utl.convert_to_float(value)
            elif key == 'episode_writers':
                episode[key] = utl.convert_to_list(value, ', ')
    return episodes

def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director_name_01 >: < episode_count >,
            < director_name_02 >: < episode_count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """

    episodes_by_director = {}
    for episode in episodes:
        director_name = episode['episode_director']
        if director_name in episodes_by_director:
            episodes_by_director[director_name] += 1
        else:
            episodes_by_director[director_name] = 1
    return episodes_by_director

def create_droid(data):
    """Returns a new dictionary representation of a droid from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Key order:
        url
        name
        model
        manufacturer
        create_year
        height_cm
        mass_kg
        equipment
        instructions

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'model': data.get('model'),
        'manufacturer': data.get('manufacturer'),
        'create_year': data.get('create_year'),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'equipment': utl.convert_to_list(data.get('equipment'), '|'),
        'instructions': data.get('instructions')
    }


def create_person(data, planets=None):
    """Returns a new dictionary representation of a person from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Both the person's "homeworld" and "species" values are used to retrieve SWAPI dictionary
    representations of the planet and specie values. Retrieving the SWAPI homeworld and
    species data is delegated to the function < utl.get_resource >.

    If an optional Wookieepedia-sourced < planets > list is provided, the task of retrieving
    the appropriate nested dictionary (filters on the passed in homeworld planet
    name) is delegated to the function < get_wookieepedia_data >.

    Before the homeworld and species data is mapped (e.g. assigned) to the person's "homeworld"
    and "species" keys, the functions < create_planet > and < create_species > are called
    in order to provide new dictionary representations of the person's homeworld and species.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to dict)
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        height_cm
        mass_kg
        homeworld
        species
        force_sensitive

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        dict: new dictionary
    """

    homeworld = utl.convert_to_none(data.get('homeworld'))
    species = utl.convert_to_none(data.get('species'))

    species_value = utl.get_resource(utl.SWAPI_SPECIES, {'search':species})['results'][0]
    homeworld_value = utl.get_resource(utl.SWAPI_PLANETS, {'search':homeworld})['results'][0]

    if planets:
        additional_value = get_wookieepedia_data(planets, homeworld)
        for key, value in additional_value.items():
            homeworld_value[key] = value

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'birth_year': utl.convert_to_none(data.get('birth_year')),

        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),

        'homeworld': create_planet(homeworld_value),
        'species': create_species(species_value),

        'force_sensitive': utl.convert_to_none(data.get('force_sensitive')),
    }


def create_planet(data):
    """Returns a new dictionary representation of a planet from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moon -> moons (str->int)
        orbital_period -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Key order:
        url
        name
        region
        sector
        suns
        moons
        orbital_period_days
        diameter_km
        gravity_std
        climate
        terrain
        population

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'region': utl.convert_to_none(data.get('region')),
        'sector': utl.convert_to_none(data.get('sector')),
        'suns': utl.convert_to_int(data.get('suns')),
        'moons': utl.convert_to_int(data.get('moons')),
        'orbital_period_days': utl.convert_to_float(data.get('orbital_period')),
        'diameter_km': utl.convert_to_int(data.get('diameter')),
        'gravity_std': utl.convert_gravity_value(data.get('gravity')),
        'climate': utl.convert_to_list(data.get('climate'), ', '),
        'terrain': utl.convert_to_list(data.get('terrain'), ', '),
        'population': utl.convert_to_int(data.get('population'))
    }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)
        average_height -> average_height_cm (str to float)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        average_height_cm
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    
    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'classification': utl.convert_to_none(data.get('classification')),
        'designation': utl.convert_to_none(data.get('designation')),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'average_height_cm': utl.convert_to_float(data.get('average_height')),
        'language': utl.convert_to_none(data.get('language')),
    }


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        starship_class
        manufacturer
        length_m
        max_atmosphering_speed
        hyperdrive_rating
        top_speed_mglt
        armament
        crew_size
        crew_members
        max_passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'model': utl.convert_to_none(data.get('model')),
        'starship_class': utl.convert_to_none(data.get('starship_class')),
        'manufacturer': utl.convert_to_none(data.get('manufacturer')),
        'length_m': utl.convert_to_float(data.get('length')),
        'max_atmosphering_speed': utl.convert_to_int(data.get('max_atmosphering_speed')),
        'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
        'top_speed_mglt': utl.convert_to_int(data.get('MGLT')),
        
        'armament': utl.convert_to_list(data.get('armament'), ","),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'crew_members': utl.convert_to_int(data.get('crew_members')),
        'max_passengers': utl.convert_to_int(data.get('passengers')),
        'passengers_on_board': utl.convert_to_none(data.get('passengers_on_board')),
        'cargo_capacity_kg': utl.convert_to_int(data.get('cargo_capacity')),
        'consumables': utl.convert_to_none(data.get('consumables'))
    }


def get_wookieepedia_data(wookiee_data, filter):
    """Attempts to retrieve a Wookieepedia sourced dictionary representation of a
    Star Wars entity (e.g., droid, person, planet, species, starship, or vehicle)
    from the < wookiee_data > list using the passed in filter value. The function performs
    a case-insensitive comparison of each nested dictionary's "name" value against the
    passed in < filter > value. If a match is obtained the dictionary is returned to the
    caller; otherwise None is returned.

    Parameters:
        wookiee_data (list): Wookieepedia-sourced data stored in a list of nested dictionaries
        filter (str): name value used to match on a dictionary's "name" value

    Returns
        dict|None: Wookieepedia-sourced data dictionary if match on the filter is obtained;
                   otherwise returns None
    """

    for wookiee in wookiee_data:
        if filter.lower() == wookiee['name'].lower():
            return wookiee
    return None



def get_most_viewed_episode(episodes):
    """Identifies and returns a list of one or more episodes with the highest recorded
    viewership. Ignores episodes with no viewship value. Includes in the list only those
    episodes that tie for the highest recorded viewership. If no ties exist only one
    episode will be returned in the list. Delegates to the function < has_viewer_data >
    the task of determining if the episode includes viewership "episode_us_viewers_mm"
    numeric data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: episode(s) with the highest recorded viewership.
    """

    top_view = 0
    result = []
    for episode in episodes:
        cur_view = has_viewer_data(episode)
        if cur_view:
            if episode["episode_us_viewers_mm"] > top_view:
                result = []
                top_view = episode["episode_us_viewers_mm"]
                result.append(episode)
            elif episode["episode_us_viewers_mm"] == top_view:
                result.append(episode)
    return result

def get_nyt_news_desks(articles):
    """Returns a list of New York Times news desks sourced from the passed in < articles >
    list. Accesses the news desk name from each article's "news_desk" key-value pair. Filters
    out duplicates in order to guarantee uniqueness.

    Delegates to the function < utl.convert_to_none > the task of converting "news_desk"
    values that equal "None" (a string) to None. Only news_desk values that are "truthy"
    (i.e., not None) are returned in the list.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        list: news desk strings (no duplicates)
    """

    result = []
    for article in articles:
        value = utl.convert_to_none(article["news_desk"])
        if value != None and value not in result:
            result.append(value)
    return result

def group_nyt_articles_by_news_desk(news_desks, articles):
    """Returns a dictionary of "news desk" key-value pairs that group the passed in
    < articles > by their parent news desk. The passed in < news_desks > list provides
    the keys while each news desk's < articles > are stored in a list and assigned to
    the appropriate "news desk" key. Each key-value pair is structured as follows:

    {
        < news_desk_name_01 >: [{< article_01 >}, {< article_05 >}, ...],
        < news_desk_name_02 >: [{< article_20 >}, {< article_31 >}, ...],
        ...
    }

    Each dictionary that represents an article is a "thinned" version of the New York Times
    original and consists of the following key-value pairs ordered as follows:

    Key order:
        web_url
        headline_main (new name)
        news_desk
        byline_original (new name)
        document_type
        material_type (new name)
        abstract
        word_count
        pub_date

    Parameters:
        news_desks (list): list of news_desk names
        articles (list): nested dictionary representations of New York Times articles

    Returns
        dict: key-value pairs that group articles by their parent news desk
    """

    news_desk_articles = {}
    for new_desk in news_desks:
        news_desk_articles[new_desk] = []

    for article in articles:
        desk = utl.convert_to_none(article["news_desk"])
        if desk != None:
            new_article  = {}
            new_article['web_url'] = article['web_url']
            new_article['headline_main'] = article['headline']['main']
            new_article['news_desk'] = article['news_desk']
            new_article['byline_original'] = article['byline']['original']
            new_article['document_type'] = article['document_type']
            new_article['material_type'] = article['type_of_material']
            new_article['abstract'] = article['abstract']
            new_article['word_count'] = article['word_count']
            new_article['pub_date'] = article['pub_date']
            news_desk_articles[desk].append(new_article)
    return news_desk_articles


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """
    if episode["episode_us_viewers_mm"]:
        return True
    else:
        return False

def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 9.1 CHALLENGE 01

    # TODO Refactor utl.read_csv()
    print('Problem 9.1:\n')
    clone_wars = utl.read_csv('clone_wars.csv')
    print(f"clone_wars = {clone_wars}\n") 



    clone_wars_22 = clone_wars[1:5]
    clone_wars_2012 = clone_wars[4:6]
    clone_wars_url = clone_wars[-2][6]
    clone_wars_even_num_seasons = clone_wars[2::2]

    print(f"clone_wars_22 = {clone_wars_22}\n") 
    print(f"clone_wars_2012 = {clone_wars_2012}\n") 
    print(f"clone_wars_url = {clone_wars_url}\n") 
    print(f"clone_wars_even_num_seasons = {clone_wars_even_num_seasons}\n") 

    # 9.2 Challenge 02

    # TODO Implement convert_to_none(), convert_to_int(), convert_to_float(), convert_to_list()
    print(f"\nconvert_to_none -> None = {utl.convert_to_none('N/A')}")
    print(f"\nconvert_to_none -> None = {utl.convert_to_none('')}")
    print(f"\nconvert_to_none -> no change = {utl.convert_to_none(5.5)}")
    print(f"\nconvert_to_none -> no change = {utl.convert_to_none((1, 2, 3))}")
    print(f"\nconvert_to_int -> int = {utl.convert_to_int('506 ')}")
    print(f"\nconvert_to_int -> None = {utl.convert_to_int(' unknown')}")
    print(f"\nconvert_to_int -> no change = {utl.convert_to_int([506, 507])}")

# Devise additional tests yourself for convert_to_float and convert_to_list

    # 9.3 CHALLENGE 03
    print('Problem 9.3:\n')
    # TODO Refactor utl.read_csv_to_dicts()

    clone_wars_episodes = utl.read_csv_to_dicts('clone_wars_episodes.csv')

    # TODO Implement has_viewer_data()

    # TODO Implement loop
    episode_count = 0
    for episode in clone_wars_episodes:
        if has_viewer_data(episode):
            episode_count += 1

    print(f"clone_wars_episodes = {clone_wars_episodes}\n") 
    print(f"episode_count = {episode_count}\n") 

    # 9.4 Challenge 04
    print('Problem 9.4:\n')
    # TODO Implement convert_episode_values()
    
    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    utl.write_json('stu-clone_warsepisodes_converted.json', clone_wars_episodes)
    print(f"clone_wars_episodes = {clone_wars_episodes}\n") 

    # 9.5 Challenge 05

    # TODO Implemennt get_most_viewed_episode()
    print('Problem 9.5:\n')
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)
    print(f"most_viewed_episode = {most_viewed_episode}\n") 

    # 9.6 Challenge 06
    print('Problem 9.6:\n')
    # TODO Implement count_episodes_by_director()

    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    utl.write_json('stu-clone_warsdirector_episode_counts.json', director_episode_counts)
    print(f"director_episode_counts = {director_episode_counts}\n")

    # 9.7 CHALLENGE 07
    print('Problem 9.7:\n')
    articles = utl.read_json('nyt_star_wars_articles.json')

    # TODO Implement get_nyt_news_desks()

    news_desks = get_nyt_news_desks(articles)
    print(f"news_desks = {news_desks}\n")

    utl.write_json('stunyt_news_desks.json', news_desks)

    # 9.8 CHALLENGE 08
    print('Problem 9.8:\n')
    # TODO Implement group_nyt_articles_by_news_desk()

    news_desk_articles = group_nyt_articles_by_news_desk(news_desks, articles)
    print(f"news_desk_articles = {news_desk_articles}\n")

    utl.write_json('stunyt_news_desk_articles.json', news_desk_articles)

    # 9.9 CHALLENGE 09
    print('Problem 9.9:\n')
    # TODO Implement calculate_articles_mean_word_count()

    ignore = ('Business Day', 'Movies')

    # TODO Implement loop
    mean_word_counts = {}
    for key, value in news_desk_articles.items():
        if key != 'Business Day' and key != 'Movies':
            mean = calculate_articles_mean_word_count(value)
            mean_word_counts[key] = mean
    
    utl.write_json('stunyt_news_desk_mean_word_counts.json', mean_word_counts)

    # 9.10 CHALLENGE 10
    print('Problem 9.10:\n')
    # TODO Implement convert_gravity_value()
    print(f"\nconvert_gravity_value -> float = {utl.convert_gravity_value('1standard')}")
    print(f"\nconvert_gravity_value -> None = {utl.convert_gravity_value('N/A')}")
    print(f"\nconvert_gravity_value -> float = {utl.convert_gravity_value('0.98')}")

    # 9.11 CHALLENGE 11
    print('Problem 9.11:\n')
    # TODO Implement get_wookieepedia_data()

    wookiee_planets = utl.read_csv_to_dicts('wookieepedia_planets.csv')

    wookiee_dagobah = get_wookieepedia_data(wookiee_planets, 'dagobah')
    wookiee_haruun_kal = get_wookieepedia_data(wookiee_planets, 'HARUUN KAL')
    print(f"wookiee_planets = {wookiee_planets}\n")
    print(f"wookiee_dagobah = {wookiee_dagobah}\n")

    utl.write_json('stuwookiee_dagobah.json', wookiee_dagobah)
    utl.write_json('stu-wookiee_haruun_kal.json', wookiee_haruun_kal)


    # 9.12 CHALLENGE 12
    print('Problem 9.12:\n')
    # TODO Implement create_planet()
    tatooine_params = {'search': "Tatooine"}

    swapi_tatooine = utl.get_resource(utl.SWAPI_PLANETS, tatooine_params)['results'][0]
    wookiee_tatooine = get_wookieepedia_data(wookiee_planets, "Tatooine")

    print(f"swapi_tatooine = {swapi_tatooine}\n")
    print(f"wookiee_tatooine = {wookiee_tatooine}\n")

    for key, value in wookiee_tatooine.items():
        if value != None:
            swapi_tatooine[key] = value

    tatooine = create_planet(swapi_tatooine)
    print(f"tatooine = {tatooine}\n")
    utl.write_json('stu-tatooine.json', tatooine)


    # 9.13 CHALLENGE 13
    print('Problem 9.13:\n')
    # TODO Implement create_droid()

    wookiee_droids = utl.read_json('wookieepedia_droids.json')

    swapi_r2_d2 = utl.get_resource(utl.SWAPI_PEOPLE, {'search': "R2-D2"})['results'][0]
    wookiee_r2_d2 = get_wookieepedia_data(wookiee_droids, "R2-D2")

    print(f"swapi_r2_d2 = {swapi_r2_d2}\n")
    print(f"wookiee_r2_d2 = {wookiee_r2_d2}\n")

    for key, value in wookiee_r2_d2.items():
        if value != None:
            swapi_r2_d2[key] = value

    r2_d2 = create_droid(swapi_r2_d2)
    utl.write_json('stu-r2_d2.json', r2_d2)


    # 9.14 Challenge 14
    print('Problem 9.14:\n')
    # TODO Implement create_species()

    swapi_human_species = utl.get_resource(utl.SWAPI_SPECIES, {'search': "HUMAN"})['results'][0]

    human_species = create_species(swapi_human_species)

    print(f"swapi_human_species = {swapi_human_species}\n")
    print(f"human_species = {human_species}\n")

    utl.write_json('stu-human_species.json', human_species)


    # 9.15 Challenge 15
    print('Problem 9.15:\n')
    # TODO Implement create_person()

    # 9.15.2
    wookiee_people = utl.read_json('wookieepedia_people.json')

    swapi_anakin = utl.get_resource(utl.SWAPI_PEOPLE, {'search': "Anakin"})['results'][0]
    wookiee_anakin = get_wookieepedia_data(wookiee_people, "Anakin Skywalker")

    print(f"swapi_anakin = {swapi_anakin}\n")
    print(f"wookiee_anakin = {wookiee_anakin}\n")

    for key, value in wookiee_anakin.items():
        if value != None:
            swapi_anakin[key] = value

    anakin = create_person(swapi_anakin, wookiee_planets)
    utl.write_json('stu-anakin_skywalker.json', anakin)


    # 9.16 CHALLENGE 16
    print('Problem 9.16:\n')
    # TODO Implement create_starship()

    wookiee_starships = utl.read_csv_to_dicts('wookieepedia_starships.csv')

    wookiee_twilight = get_wookieepedia_data(wookiee_starships, "Twilight")

    print(f"wookiee_twilight = {wookiee_twilight}\n")

    twilight = create_starship(wookiee_twilight)
    utl.write_json('stu-twilight.json', twilight)



    # 9.17 CHALLENGE 17
    print('Problem 9.17:\n')
    # TODO Implement board_passengers()

    swapi_padme = utl.get_resource(utl.SWAPI_PEOPLE, {'search': "Padmé"})['results'][0]
    wookiee_padme = get_wookieepedia_data(wookiee_people, "Padmé Amidala")

    for key, value in wookiee_padme.items():
        if value != None:
            swapi_padme[key] = value

    padme = create_person(swapi_padme, wookiee_planets)
    print(f"padme = {padme}\n")

    swapi_c_3po = utl.get_resource(utl.SWAPI_PEOPLE, {'search': "C-3PO"})['results'][0]
    wookiee_c_3po = get_wookieepedia_data(wookiee_droids, "C-3PO")
    for key, value in wookiee_c_3po.items():
        if value != None:
            swapi_c_3po[key] = value

    print(f"swapi_c_3po = {swapi_c_3po}\n")

    c_3po = create_droid(swapi_c_3po)

    # TODO Get passengers aboard the starship Twilight
    passengers = [padme, c_3po, r2_d2]
    twilight = board_passengers(twilight, passengers)

    print(f"twilight = {twilight}\n")
    # 9.18 CHALLENGE 18
    print('Problem 9.18:\n')
    # TODO Implement assign_crew_members()

    swapi_obi_wan = utl.get_resource(utl.SWAPI_PEOPLE, {'search': "Obi-Wan Kenobi"})['results'][0]
    wookiee_obi_wan = get_wookieepedia_data(wookiee_people, "Obi-Wan Kenobi")
    for key, value in wookiee_obi_wan.items():
        if value != None:
            swapi_obi_wan[key] = value

    obi_wan = create_person(swapi_obi_wan, wookiee_planets)

    # TODO Assign crew members to the starship Twilight

    twilight = assign_crew_members(twilight, ["pilot", "copilot"], [anakin,  obi_wan])

    # TODO Add r2_d2 instructions
    r2_d2['instructions'] = ["Power up the engines"]

    # 10.0 ESCAPE

    # TODO Add r2_d2 instruction (2nd order)
    r2_d2['instructions'].append("Release the docking clamp")

    # TODO Escape from the Malevolence (write to file)
    utl.write_json('stu-twilight_departs.json', twilight)

    # PERSIST CACHE (DO NOT COMMENT OUT)
    utl.write_json(utl.CACHE_FILEPATH, utl.cache)


if __name__ == '__main__':
    main()
