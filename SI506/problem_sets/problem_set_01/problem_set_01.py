# START PROBLEM SET 1
print('Problem Set 1 \n')

# PROBLEM 1 (15 points)
print('\nPROBLEM 1')

frita_batidos = 'Frita Batidos'
# zingerman's Delicatessen = "Zingerman's Delicatessen"
# nypd = New York Pizza Depot
hopcat = 'Hopcat'
fleetwood_diner = "Fleetwood Diner"
# tomukun_noodle_bar = 'Tomukun Noodle Bar

cottage_inn = 'Cottage Inn Pizza'
madras_masala = 'Madras Masala'

# PROBLEM 2 (10 points)
print('\nPROBLEM 2')
restaurants = [frita_batidos, hopcat, fleetwood_diner]

#TODO: Add cottage_inn
restaurants.append(cottage_inn)

#TODO: Add madras_masala
restaurants.append(madras_masala)

print(restaurants) #UNCOMMENT TO CHECK

# PROBLEM 3 (20 points)
print('\nPROBLEM 3')

all_restaurants = ','.join(restaurants)
print(all_restaurants) #UNCOMMENT TO CHECK

all_restaurants_with_spaces = all_restaurants.replace(',', ', ')
print(all_restaurants_with_spaces) #UNCOMMENT TO CHECK

# PROBLEM 4 (20 points)
print('\nPROBLEM 4')

restaurants_reversed = restaurants[::-1]
print(restaurants_reversed) #UNCOMMENT TO CHECK

# TODO: Create variable every_other_restaurant
every_other_restaurant = restaurants_reversed[::2]
print(every_other_restaurant) #UNCOMMENT TO CHECK

# PROBLEM 5 (20 points)
print('\nPROBLEM 5')

restaurant_checks = [12.67, 22.30, 8.86, 11.84, 15.53]

# TODO: Update restaurant_checks
restaurant_checks[2] = 9.56

max_check = max(restaurant_checks)

max_check_index = restaurant_checks.index(max_check)

#TODO: Create variable max_check_restaurant
max_check_restaurant = restaurants[max_check_index]

print(max_check_restaurant) #UNCOMMENT TO CHECK

# PROBLEM 6 (15 points)
print('\nPROBLEM 6')

# DO NOT ALTER
extra_restaurants = """Panera Bread
Jagged Fork
Wolverine Sushi
aMa Bistro
Stray Hen Cafe"""

new_restaurants = extra_restaurants.splitlines()
print(new_restaurants) #UNCOMMENT TO CHECK

#TODO: Add elements of new_restaurants to restaurants
final_restaurants = restaurants + new_restaurants
print(final_restaurants) #UNCOMMENT TO CHECK

# END PROBLEM SET