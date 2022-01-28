# SI 506 Lecture 07

# EV attributes: automaker, model, model year, range (miles)
elec_vehicles = [
    'Ford, Mustang Mach-E AWD, 2021, 211',
    'Kandi, K27, 2021, 59',
    'Chevrolet (GM), Bolt EV, 2021, 259',
    'Audi (Volkswagen), e-tron, 2021, 222',
    'Nissan, Leaf (40 kW-hr battery pack), 2021, 149',
    'Tesla, Model 3 Performance AWD, 2021, 315',
    'Volvo, XC40 AWD BEV, 2021, 208',
    'Volkswagen, ID.4 1st, 2021, 250',
    'BMW, i3s, 2021, 153',
    'MINI (BMW), Cooper SE Hardtop 2 door, 2021, 110',
    'Tesla, Model S Performance (19in Wheels), 2021, 387'
    ]

models = []
for element in elec_vehicles:
    vehicle = element.split(', ')
    # vehicle = element.split(', ')[:2] # a new list comprising the first two elements only
    models.append(f"{vehicle[0]} {vehicle[1]}")

# print(f"\n1.0.1 EV models = {models}")

# EV attributes: automaker, model, model year, range (miles)
elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', '2021', '211'],
    ['Kandi', 'K27', '2021', '59'],
    ['Chevrolet (GM)', 'Bolt EV', '2021', '259'],
    ['Audi (Volkswagen)', 'e-tron', '2021', '222'],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', '2021', '149'],
    ['Tesla', 'Model 3 Performance AWD', '2021', '315'],
    ['Volvo', 'XC40 AWD BEV', '2021', '208'],
    ['Volkswagen', 'ID.4 1st', '2021', '250'],
    ['BMW', 'i3s', '2021', '153'],
    ['MINI (BMW)', 'Cooper SE Hardtop 2 door', '2021', '110'],
    ['Tesla', 'Model S Performance (19in Wheels)', '2021', '387']
    ]

models = []
for vehicle in elec_vehicles:
    models.append(f"{vehicle[0]} {vehicle[1]}")

# print(f"\n1.0.2 EV models = {models}")


# 2.0 LOOPING AND COUNTING

bmw_count = 0
for vehicle in elec_vehicles:
    if 'bmw' in vehicle[0].lower():
        bmw_count += 1 # assignment addition equivalent to bmw_count = bmw_count + 1

# print(f"\n2.0 BMW count = {bmw_count}")


# CHALLENGE 01

mpg_count = 0

# TODO Implement loop
for vehicle in elec_vehicles:
    if int(vehicle[-1]) >= 250:
        mpg_count += 1;
# print(f"\nCh 01 mpg > 250 mi = {mpg_count}")


# 3.0 LOOPING WITH RANGE()

# 3.1 range() behaviors

seq = range(10)

print(f"\n3.1.1 seq (type={type(seq)}) = {seq}") # <class 'range'>

seq = list(range(10)) # convert range object to a list

print(f"\n3.1.2 range seq = {seq}")

seq = list(range(5, 10))

print(f"\n3.1.3 range seq start/stop = {seq}")

seq = list(range(5, 21, 5))

print(f"\n3.1.4 range seq start/stop/step = {seq}")

seq = list(range(20, 4, -5))

print(f"\n3.1.5 range seq start/stop/step reversed = {seq}")

# TODO Uncomment
print(f"\n3.1.6 for loop with range()\n")
for i in range(5):
    print("I want to own an EV!")


# 3.2 The `for` loop and `range`

automakers = [
    'Bayerische Motoren Werke AG',
    'Ford Motor Co.',
    'General Motors Co.',
    'Kandi Technologies Group',
    'Nissan Motor Co.',
    'Volkswagen AG',
    'Volvo Group',
    'Tesla, Inc.'
    ]

# TODO Uncomment
# print(f"\n3.2 access automakers with range()\n")
# for i in range(len(automakers)):
    # print(f"{i} {automakers[i]}")

# TODO Uncomment
# Replace immutable string value (fail)
# for automaker in automakers:
#     automaker = automaker.upper() # assigns new string to loop variable only


# print(f"\n3.3.1 automaker to uppercase (fail) = {automakers}")

# Replace immutable element value (success)
# TODO Uncomment
# for i in range(len(automakers)):
#     automakers[i] = automakers[i].upper() # assigns new string to element

# print(f"\n3.3.2 automaker to uppercase (fail) = {automakers}")


# 3.4 Subscript notation chaining

# TODO Uncomment
# tesla_s_range = elec_vehicles[-1][-1]
# tesla_s_range = elec_vehicles[-1][3] # Alternative
# tesla_s_range = elec_vehicles[10][3] # Alternative
# tesla_s_range = elec_vehicles[10][-1] # Alternative

# print(f"\n3.4.1 Tesla Model S range (mpg) = {tesla_s_range}")

tesla_s_range = 0
for i in range(len(elec_vehicles)):
    if elec_vehicles[i][1] == 'Model S Performance (19in Wheels)':
        tesla_s_range = elec_vehicles[i][-1]

# print(f"\n3.4.2 Tesla Model S range (mpg) = {tesla_s_range}")


# CHALLENGE 02

elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', '2021', '211'],
    ['Kandi', 'K27', '2021', '59'],
    ['Chevrolet (GM)', 'Bolt EV', '2021', '259'],
    ['Audi (Volkswagen)', 'e-tron', '2021', '222'],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', '2021', '149'],
    ['Tesla', 'Model 3 Performance AWD', '2021', '315'],
    ['Volvo', 'XC40 AWD BEV', '2021', '208'],
    ['Volkswagen', 'ID.4 1st', '2021', '250'],
    ['BMW', 'i3s', '2021', '153'],
    ['MINI (BMW)', 'Cooper SE Hardtop 2 door', '2021', '110'],
    ['Tesla', 'Model S Performance (19in Wheels)', '2021', '387']
    ]

# TODO Implement loop

# print(f"\nCh 02 Automaker + Model name = {elec_vehicles}")


## CHALLENGE 03 (BONUS)

elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Co.', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
    ['Kandi Technologies Group', 'Kandi', 'K27', 2021, 59, 51.6, 64.3, 102, 7.0],
    ['General Motors Co.', 'Chevrolet', 'Bolt EV', 2021, 259, 235.1, 277.7, 108, 9.3],
    ['Volkswagen AG', 'Audi', 'e-tron', 2021, 222, 221.9408, 222.74, 77, 10.0],
    ['Nissan Motor Co.', 'Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149, 131.3, 163.2, 99, 8.0],
    ['Tesla Inc.', 'Tesla', 'Model 3 Performance AWD', 2021, 315, 299.0, 328.7, 107, 10.0],
    ['Volvo Group', 'Volvo', 'XC40 AWD BEV', 2021, 208, 188.0, 223.6, 72, 8.0],
    ['Volkswagen AG', 'Volkswagen', 'ID.4 1st', 2021, 250, 230.1587, 266.7659, 89, 7.5],
    ['Bayerische Motoren Werke AG', 'BMW', 'i3s', 2021, 153, 136.4, 166.5, 102, 7.0],
    ['Bayerische Motoren Werke AG', 'MINI', 'Cooper SE Hardtop 2 door', 2021, 110, 101.9, 116.9, 100, 4.0],
    ['Tesla Inc.', 'Tesla','Model S Performance (19in Wheels)', 2021, 387, 373.2, 398.3, 106, 14.7]
]

select_vehicles = []

# TODO Implement loop

# print(f"\nCh 03 every other vehicle using range()\n{select_vehicles}")


# 4.0 IF-ELSE

headers = elec_vehicles[0] # Extract header row

short_charge = []
long_charge = []
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('charge_240v_hrs')] < 8.0:
        short_charge.append(vehicle)
    else:
        long_charge.append(vehicle)

# print(f"\n4.0.1 short charge = {short_charge}")
# print(f"\n4.0.2 long charge = {long_charge}")

standard_charge = []
outliers = []
for vehicle in elec_vehicles[1:]:
    if 6.0 < vehicle[headers.index('charge_240v_hrs')] < 10.0:
        standard_charge.append(vehicle)
    else:
        outliers.append(vehicle)

# print(f"\n4.0.3 standard charge = {standard_charge}")
# print(f"\n4.0.4 outliers = {outliers}")

# CHALLENGE 04

range_high = 0
range_low = 0

# TODO Implement loop

# print(f"\nCh 04 EV high range count = {range_high}")
# print(f"\nCh 04 EV low range count = {range_low}")
