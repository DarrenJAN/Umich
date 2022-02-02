# SI 506 Lecture 06

# 2.0 DEFINITE ITERATION

# https://www.fueleconomy.gov/feg/ws/index.shtml#ft7

elec_vehicles = [
    'Ford Mustang Mach-E AWD',
    'Kandi K27',
    'Chevrolet (GM) Bolt EV',
    'Audi (Volkswagen) e-tron',
    'Nissan Leaf (40 kW-hr battery pack)',
    'Tesla Model 3 Performance AWD',
    'Volvo XC40 AWD BEV',
    'Volkswagen ID.4 1st',
    'Polestar (Volvo) 2',
    'BMW i3s',
    'Mini (BMW) Cooper SE Hardtop 2 door',
    'Tesla Model S Performance (19in Wheels)'
]

# 2.0 CREATE LIST OF TESLA VEHICLES
tesla_vehicles = []
tesla_vehicles.append(elec_vehicles[5])
tesla_vehicles.append(elec_vehicles[-1])

print(f"\n2.0 Tesla vehicles (n={len(elec_vehicles)}) = {tesla_vehicles}")


# 2.1 FOR LOOP
print(f"\n2.1 elec_vehicles (loop)")

for vehicle in range(3):
    print(vehicle)


# 2.2 IF STATEMENT

print(f"\n2.2.1 Volo vehicles")

# Find "volvo" string
for vehicle in elec_vehicles:
    if vehicle.lower().find('volvo') > -1:
        print(vehicle)

# Get Volkswagens
print(f"\n2.2.2 Volkswagen EVs")
for vehicle in elec_vehicles:
    if 'volkswagen' in vehicle.lower():
        print(vehicle)

# Get non-Volkswagens
print(f"\n2.2.2 Non-Volkswagen EVs")
for vehicle in elec_vehicles:
    if 'volkswagen' not in vehicle.lower():
        print(vehicle)


## CHALLENGE 01

print(f"\nCh 01 Tesla EVs (membership in)")
for vehicle in elec_vehicles:
    if 'tesla' in vehicle.lower():
        print(vehicle)

# Alternative (str.startswith())
print(f"\nCh 01 Tesla EVs (str.startswith()")
for vehicle in elec_vehicles:
    if vehicle.lower().startswith('tesla'):
        print(vehicle)

# Alternative (str.find())
print(f"\nCh 01 Tesla EVs (str.find()")
for vehicle in elec_vehicles:
    if vehicle.lower().find('tesla') > -1:
        print(vehicle)


# 3.0 THE ACCUMULATOR PATTERN

teslas = [] # accumulator
for vehicle in elec_vehicles:
    if 'tesla' in vehicle.lower():
        teslas.append(vehicle)

print(f"\n3.0.1 Tesla EVs = {teslas}")

# Data: Automaker, Model, Year, mileage
elec_vehicles = [
    'Ford, Mustang Mach-E AWD, 2021, 211',
    'Kandi, K27, 2021, 59',
    'Chevrolet (GM), Bolt EV, 2021, 259',
    'Audi (Volkswagen), e-tron, 2021, 222',
    'Nissan, Leaf (40 kW-hr battery pack), 2021, 149',
    'Tesla, Model 3 Performance AWD, 2021, 315',
    'Volvo, XC40 AWD BEV, 2021, 208',
    'Volkswagen, ID.4 1st, 2021, 250',
    'Polestar (Volvo), 2, 2021, 233',
    'BMW, i3s, 2021, 153',
    'Mini (BMW), Cooper SE Hardtop 2 door, 2021, 110',
    'Tesla, Model S Performance (19in Wheels), 2021, 387'
    ]

vehicle_max_range = None
num = 0
for element in elec_vehicles:
    vehicle = element.split(', ') # split the string
    if int(vehicle[-1]) > num:
        num = int(vehicle[-1]) # WARN: ignores ties
        vehicle_max_range = vehicle

print(f"\n3.0.2 Max range (max={num} mi) = {vehicle_max_range}")


# CHALLENGE 02

vehicle_min_range = None
num = 1000 # brittle but works
# num = float('inf') # represents infinity (better)
for vehicle in elec_vehicles:
    vehicle = element.split(', ') # split the string
    if int(vehicle[-1]) < num:
        num = int(vehicle[-1]) #WARN: ignores ties
        vehicle_min_range = vehicle

print(f"\nCh 02: min range (min={num} mi) = {vehicle_min_range}")


# 4.0 LOOPING AND SLICING

# CHALLENGE 03

# Contains "headers" element
elec_vehicles = [
    'automaker,brand,model,year,range,range_hwy,range_city,highway_08_mpg,charge_240v_hrs',
    'Ford Motor Co.,Ford,Mustang Mach-E AWD,2021,211,193.7,225.5,86,8.5',
    'Kandi Technologies Group,Kandi,K27,2021,59,51.6,64.3,102,7.0',
    'General Motors Co.,Chevrolet,Bolt EV,2021,259,235.1,277.7,108,9.3',
    'Volkswagen AG,Audi,e-tron,2021,222,221.9408,222.74,77,10.0',
    'Nissan Motor Co.,Nissan,Leaf (40 kW-hr battery pack),2021,149,131.3,163.2,99,8.0',
    'Tesla Inc.,Tesla,Model 3 Performance AWD,2021,315,299.0,328.7,107,10.0',
    'Volvo Group,Volvo,XC40 AWD BEV,2021,208,188.0,223.6,72,8.0',
    'Volkswagen AG,Volkswagen,ID.4 1st,2021,250,230.1587,266.7659,89,7.5',
    'Volvo Group,Polestar,2,2021,233,222.1,241.9,88,8.0',
    'Bayerische Motoren Werke AG,BMW,i3s,2021,153,136.4,166.5,102,7.0',
    'Bayerische Motoren Werke AG,MINI,Cooper SE Hardtop 2 door,2021,110,101.9,116.9,100,4.0',
    'Tesla Inc.,Tesla,Model S Performance (19in Wheels),2021,387,373.2,398.3,106,14.7'
    ]

# Split "headers" element into a list
headers = elec_vehicles[0].split(',')

print(f"\nCh 03 Headers = {headers}")

# Loop over vehicles (only) and accumulate values
hi_range_elec_vehicles = [] # accumulator
for element in elec_vehicles[1:]:
    vehicle = element.split(',') # split the string
    if int(vehicle[4]) > 250: # lookup header
        hi_range_elec_vehicles.append(f"{vehicle[2]} range: {vehicle[4]} mpg")

print(f"\nCh 03 Bonus: EV's (range > 250 mi) = {hi_range_elec_vehicles}")

# BONUS: look up index values using headers
hi_range_elec_vehicles = [] # accumulator
for element in elec_vehicles[1:]:
    vehicle = element.split(',') # split the string
    if int(vehicle[headers.index('range')]) > 250: # lookup header
        hi_range_elec_vehicles.append(f"{vehicle[headers.index('model')]} range: {vehicle[headers.index('range')]} mpg")

print(f"\nCh 03 Bonus: EV's (range > 250 mi) = {hi_range_elec_vehicles}")
