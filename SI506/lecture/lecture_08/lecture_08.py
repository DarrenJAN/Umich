# SI 506 Lecture 08

# 1.0 BREAK AND CONTINUE

elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Company', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
    ['Kandi Technologies Group', 'Kandi', 'K27', 2021, 59, 51.6, 64.3, 102, 7.0],
    ['General Motors Co.', 'Chevrolet', 'Bolt EV', 2021, 259, 235.1, 277.7, 108, 9.3],
    ['Volkswagen AG', 'Audi', 'e-tron', 2021, 222, 221.9408, 222.74, 77, 10.0],
    ['Nissan Motor Co.', 'Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149, 131.3, 163.2, 99, 8.0],
    ['Tesla, Inc.', 'Tesla', 'Model 3 Performance AWD', 2021, 315, 299.0, 328.7, 107, 10.0],
    ['Volvo Group', 'Volvo', 'XC40 AWD BEV', 2021, 208, 188.0, 223.6, 72, 8.0],
    ['Volkswagen AG', 'Volkswagen', 'ID.4 1st', 2021, 250, 230.1587, 266.7659, 89, 7.5],
    ['Volvo Group', 'Polestar', '2', 2021, 233, 222.1, 241.9, 88, 8.0],
    ['Bayerische Motoren Werke AG', 'BMW', 'i3s', 2021, 153, 136.4, 166.5, 102, 7.0],
    ['Bayerische Motoren Werke AG', 'Mini', 'Cooper SE Hardtop 2 door', 2021, 110, 101.9, 116.9, 100, 4.0],
    ['Tesla, Inc.', 'Tesla','Model S Performance (19in Wheels)', 2021, 387, 373.2, 398.3, 106, 14.7]
]

# 1.1 BREAK STATEMENT EXAMPLE

headers = elec_vehicles[0] # column headers

has_kandi = False
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('automaker')].lower() == 'kandi technologies group':
        has_kandi = True
        break # exit loop

# print(f"\n1.1 Has Kandi Technology Group = {has_kandi}")


# CHALLENGE 01 BREAK STATEMENT

fast_charge = 3.0 # battery charge (hours)
can_fast_charge = False

# TODO Implement loop

# print(f"\nCh 01 Has {fast_charge} hr battery charge vehicle = {can_fast_charge}")


# 1.2 CONTINUE STATEMENT EXAMPLE

outliers = []
for vehicle in elec_vehicles[1:]:
    city_range = vehicle[headers.index('range_city')]
    if 75.0 < city_range < 275.0:
        continue # proceed to next iteration (skip)
    outliers.append(vehicle)

# print(f"\n1.2 City range outliers\n{outliers}")


# CHALLENGE 02 CONTINUE STATEMENT

us_automakers = ('ford motor company', 'general motors co.', 'tesla, inc.') # tuple
non_us_vehicles = []

# TODO Implement loop

# print(f"\nCh 02 Asian/European automakers' vehicles (n={len(non_us_vehicles)})\n{non_us_vehicles}")


# 3.0 WHILE LOOP

# TODO Uncomment

# print(f"\n3.0 while loop")
# i = 0
# while i < 5:
#     print(i)
#     i += 1 # increment

# print(f"\n3.1 while True")
# i = 0
# while True:
#     print(i, 'infinite loop triggered')
#     if i == 5:
#         print(i, 'infinite loop terminated\n')
#         break # exit the loop
#     i += 1 # increment (note indention)

# print(f"\n3.2 while loop with else")
# i = 0
# while i < 5:
#     print('I want an EV.')
#     i += 1 # increment
# else:
#     print('Enough said. We believe you.')

# print(f"\n3.3.1 while loop if-else (increment)")
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i += 1 # increment

# print(f"\n3.3.2 while loop if-else (decrement)")
# i = 10
# while i >= 0:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i -= 1 # decrement


# 3.4 WHILE LOOP AND RANGE

# TODO Uncomment
# print(f"\n3.3. while loop and range()")
# i = 0
# while i in range(0, 10, 2):
#     print(f"{i} is an even number.")
#     i += 2 # increment by 2


# 3.5 WHILE LOOP AND INPUT()

ev_automakers = (
    'audi',
    'bmw',
    'ford',
    'gm',
    'yyundai',
    'kandi',
    'kia',
    'jaguar',
    'nissan',
    'tesla',
    'volkswagen',
    'volvo'
    )

# TODO Uncomment
# while True:
#     automaker = input('\nName your favorite EV automaker: ')
#     if automaker.lower() in ev_automakers:
#         print(f"\nThanks for selecting {automaker}.\n\nFinis.")
#         break # terminate loop

#     # print() can accept a comma-delimited set of strings
#     print(
#         f"\n'{automaker}' is not listed among the EV manufacturers.",
#         f"Please check spelling and enter again or provide a different automaker."
#         )


# CHALLENGES 03-05

data = [
    ['station_name', 'street_address', 'ev_connector_types', 'ev_network'],
    ['Ann Arbor Downtown Development Authority - Library Parking Structure', '319 S Fifth Ave', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', '120 W Ann St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', '121 Catherine St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Forrest Parking Structure', '650 Forrest St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Maynard Parking Structure', '316 Maynard St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - William Street Parking Structure', '115 William St', 'J1772', 'Non-Networked'],
    ['U-M ANN ARBOR Ann Street #2', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR ICL EDU #1', '1000 Greene St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR Walgreen #1', '1300 Murfin Ave', 'J1772', 'ChargePoint Network'],
    ['BMW ANN ARBOR Station 01', '501 Auto Mall Dr', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR Wall Street #2', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["Domino's Farms Domino's Farms 2", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', '215 W Washington', 'J1772', 'Non-Networked'],
    ['Meadowlark Bldg Station 2', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['Shell', '2991 S State St', 'CHADEMO, J1772COMBO', 'eVgo Network'],
    ['Meijer - Tesla Supercharger', '3145 Ann Arbor-Saline Rd', 'TESLA', 'Tesla'],
    ['Sheraton Ann Arbor Hotel - Tesla Destination', '3200 Boardwalk Dr', 'J1772, TESLA', 'Tesla Destination'],
    ['Meijer Stores 064 Saline Rd 1', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC Station 2', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['Fleet Services City Hall Sta 4', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['173 - Ann Arbor', '5645 Jackson Road', 'CHADEMO, J1772COMBO', 'Greenlots'],
    ['Car & Driver - Tesla Destination', '1585 Eisenhower Place', 'TESLA', 'Tesla Destination'],
    ['U-M ANN ARBOR Ann Street #1', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR Ann Street #3', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR Wall Street #1', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["Domino's Farms Domino's Farms", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['Meadowlark Bldg Station 1', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['Meijer Stores 064 Saline Rd 2', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC Station 1', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['Fleet Services Police Space #5', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['Beekman Beekman St 1', '1200 Broadway St', 'J1772', 'ChargePoint Network']
    ]

# Example: index chaining
chargepoint_count = 0
i = 0
while i < len(data[1:]):
    if data[i][-1] == 'ChargePoint Network':
        chargepoint_count += 1
    i += 1 # increment

# print(f"\nCh 03 example: Chargepoint Network count = {chargepoint_count}")


# CHALLENGE 03

charging_stations = None # TODO Access charging stations
um_count = 0 # TODO Initialize
i = 0 # TODO Initialize

# TODO Implement loop

# print(f"\nCh 03 while loop: UMich charging stations = {um_count} ({um_count/len(charging_stations):.2}%)")


# CHALLENGE 04

i = None # TODO Intialize

# TODO Implement loop

# print(f"\nCh 05 while loop: Ann Arbor mixed case (slice) = {charging_stations[7:13]}")


# CHALLENGE 05

headers = None # TODO Access headers
i = None # TODO Intialize

# TODO Implement loop

# print(f"\nCh 05 while loop: convert str to list (slice) = {charging_stations[-4:-2]}")
