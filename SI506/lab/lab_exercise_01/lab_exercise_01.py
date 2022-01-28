# START LAB EXERCISE 01
print('Lab Exercise 01 \n')

# PROBLEM 1 (2 points)
north_quad = "North Quad"
ccrb = "Central Campus Recreation Building"
kelsey_museum = "Kelsey Museum of Archaeology"
mason_hall = "Mason Hall"

locations = [north_quad, ccrb, kelsey_museum, mason_hall]


# PROBLEM 2 (2 points)
num_locations = len(locations)


# PROBLEM 3 (2 points points)
north_quad_study_areas = 30
ccrb_study_areas = 0
kelsey_museum_study_areas = 9
mason_hall_study_areas = 22

total_study_areas = north_quad_study_areas + ccrb_study_areas + kelsey_museum_study_areas + mason_hall_study_areas


# PROBLEM 4 (2 points)
avg_study_areas = total_study_areas // num_locations
print(f"\n{avg_study_areas}")


# PROBLEM 5 (4 points)
study_areas = 'Central Campus Recreation Building; 0, Kelsey Museum of Archeology; 9, Mason Hall; 22, North Quad; 30'
fixed_locations = study_areas.replace(';', ':')


# PROBLEM 6 (4 points)
study_area_locations = fixed_locations.split(', ')
print(f"\n{study_area_locations}")

# PROBLEM 7 (2 points)
statement = "The locations and the number of study areas they contain are ['Central Campus Recreation Building: 0', 'Kelsey Museum of Archeology: 9', 'Mason Hall: 22', 'North Quad: 30']"


# PROBLEM 8 (2 points)
two_smallest_buildings = study_area_locations[0:2]
print(f"\n{two_smallest_buildings}")

# END LAB EXERCISE
