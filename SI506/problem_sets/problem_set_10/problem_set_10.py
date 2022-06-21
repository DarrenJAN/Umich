import swapi_entities as ent

def main():
    # Problem 1.0
    planet_data = ent.read_json('swapi_planets.json')
    # print(planet_data)
    people = []
    
    for planet in planet_data:
        urls = planet['residents']
        for url in urls:
            person  = ent.get_resource(ent.CACHE_NAME, url)
            # print(person)
            convert_data_return = ent.convert_data(person, planet_data)
            # print(convert_data_return)
            create_person_return = ent.create_person(convert_data_return)
            people.append(create_person_return)
    # print(people[0])
    ent.write_json('full_residents.json', people)



if __name__ == '__main__':
    main()
