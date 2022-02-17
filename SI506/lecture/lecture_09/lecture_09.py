# SI 506: Lecture 09

import pprint


# Instantiate a custom PrettyPrinter object
pp = pprint.PrettyPrinter(indent=1, depth=3, width=100, compact=True)

data = [
    ['id', 'station_name', 'facility_type', 'street_address', 'zip_code', 'distance_mi', 'latitude', 'longitude', 'ev_level2_evse_num', 'ev_dc_fast_count', 'ev_network', 'ev_connector_types', 'ev_pricing', 'access_Days_time'],
    ['44282', 'Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', 'PARKING_GARAGE', '120 W Ann St', '48104', '0.09349', '42.282617', '-83.749329', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['74325', 'Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', 'PAY_GARAGE', '215 W Washington', '48104', '0.11908', '42.2805401', '-83.7504773', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['44283', 'Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', 'PARKING_LOT', '121 Catherine St', '48104', '0.15246', '42.283504', '-83.747496', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['199101', 'FLEET SERVICES DCFC-STATION 1', '', '301 E. Huron St', '48104', '0.17856', '42.282108', '-83.74512', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['199102', 'FLEET SERVICES DCFC-STATION 2', '', '301 E Huron St', '48104', '0.18082', '42.28211', '-83.745075', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['200995', 'FLEET SERVICES DCFC-STATION 3', '', '301 E Huron St', '48104', '0.18331', '42.282111', '-83.745025', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['199100', 'FLEET SERVICES DCFC-STATION 4', '', '301 E. Huron St', '48104', '0.18513', '42.282143', '-83.745', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['164865', 'FLEET SERVICES POLICE SPACE #6', '', '301 E. Huron Street', '48104', '0.1884', '42.28181', '-83.74484', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['175800', 'FLEET SERVICES POLICE SPACE #5', '', '301 E Huron St', '48104', '0.1891', '42.281853', '-83.744835', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['158534', 'FLEET SERVICES CITY HALL STA 4', '', '301 E Huron St', '48104', '0.19361', '42.281704', '-83.74472', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['44286', 'Ann Arbor Downtown Development Authority - William Street Parking Structure', 'PARKING_GARAGE', '115 William St', '48104', '0.20763', '42.278461', '-83.747741', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['42726', 'Ann Arbor Downtown Development Authority - Library Parking Structure', 'LIBRARY', '319 S Fifth Ave', '48104', '0.23691', '42.278754', '-83.745565', '9', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['44285', 'Ann Arbor Downtown Development Authority - Maynard Parking Structure', 'PARKING_GARAGE', '316 Maynard St', '48104', '0.35629', '42.278668', '-83.742596', '4', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['201412', 'U-M ANN ARBOR ANN 3', '', '1101-1189 E Ann St', '48104', '0.70073', '42.282487', '-83.734882', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['201411', 'U-M ANN ARBOR ANN 1 & 2', '', '1115 E Ann St', '48104', '0.70651', '42.282455', '-83.734764', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['198009', 'Hover + Greene', 'MULTI_UNIT_DWELLING', '950 Greene St', '48104', '0.8195', '42.2695626419024', '-83.7476275130172', '4', '', 'EV Connect', 'J1772', '', '24 hours daily'],
    ['198073', 'BEEKMAN BEEKMAN ST1', '', '1200 Broadway St', '48105', '0.82522', '42.290061', '-83.737351', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['62417', 'U-M ANN ARBOR WALL STREET #2', '', '1041 Wall St', '48105', '0.83339', '42.287965', '-83.734814', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['171786', 'U-M ANN ARBOR WALL STREET #1', '', '1041 Wall St', '48105', '0.83868', '42.28802', '-83.734739', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['201416', 'U-M ANN ARBOR SC32', '', '1024 Greene St', '48109', '0.87117', '42.268809', '-83.747742', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['44284', 'Ann Arbor Downtown Development Authority - Forrest Parking Structure', 'PARKING_GARAGE', '650 Forrest St', '48104', '0.91935', '42.274044', '-83.733542', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily'],
    ['188119', 'Prentice Partners', '', '830 Henry Street', '48104', '1.49931', '42.26124', '-83.73765', '10', '', 'Greenlots', 'J1772', '', '24 hours daily'],
    ['201417', 'U-M ANN ARBOR NC27 1 & 2', '', '1300 Murfin Ave', '48109', '1.74021', '42.292278', '-83.717833', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['52242', 'Speedway #7867', 'CONVENIENCE_STORE', '1300 N Maple Rd', '48103', '1.88613', '42.294966', '-83.780441', '', '', '', '', '', '24 hours daily'],
    ['80037', 'MEADOWLARK BLDG STATION 2', '', '3250 W Liberty Rd', '48103', '2.40035', '42.274082', '-83.794254', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['172462', 'MEADOWLARK BLDG STATION 1', '', '3250 W Liberty Rd', '48103', '2.40047', '42.274074', '-83.794254', '1', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['174657', 'U-M ANN ARBOR NCRC STATION 1', '', '2800 Plymouth Rd', '48105', '2.57247', '42.301397', '-83.7061', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['147555', 'U-M ANN ARBOR NCRC STATION 2', '', '2800 Plymouth Rd', '48105', '2.57405', '42.301455', '-83.706113', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['198818', 'Shell', '', '2991 S State St', '48104', '2.58016', '42.244709', '-83.738976', '', '1', 'eVgo Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['114460', 'Sheraton Ann Arbor Hotel - Tesla Destination', 'HOTEL', '3200 Boardwalk Dr', '48108', '2.85506', '42.241306', '-83.73488', '4', '', 'Tesla Destination', 'J1772 TESLA', 'Free', '24 hours daily; for customer use only; see front desk for access'],
    ['102221', 'Meijer - Tesla Supercharger', '', '3145 Ann Arbor-Saline Road', '48103', '2.93096', '42.241125', '-83.766522', '', '8', 'Tesla', 'TESLA', '$0.28 per kWh; $0.26 per minute above 60 kW and $0.13 per minute at or below 60 kW', '24 hours daily; for Tesla use only'],
    ['147501', 'MEIJER STORES 064 SALINE RD 1', '', '3145 Ann Arbor-Saline Rd', '48108', '2.96048', '42.240552', '-83.766013', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['174646', 'MEIJER STORES 064 SALINE RD 2', '', '3145 Ann Arbor-Saline Rd', '48108', '2.96178', '42.240525', '-83.765982', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['30246', 'DTE Energy - Meijer #64', 'CONVENIENCE_STORE', '3145 Ann Arbor-Saline Rd', '48103', '2.96568', '42.241184', '-83.768778', '', '', '', '', '', '24 hours daily'],
    ['44287', 'Ann Arbor Nissan', 'CAR_DEALER', '3975 Jackson Rd', '48103', '3.085', '42.284242', '-83.80855', '1', '', 'Non-Networked', 'J1772', 'Free', 'Dealership business hours'],
    ['168663', 'Car & Driver - Tesla Destination', '', '1585 Eisenhower Place', '48108', '3.14593', '42.238068', '-83.729527', '2', '', 'Tesla Destination', 'TESLA', 'Free', '24 hours daily; for customer use only; see front desk for access'],
    ['187922', 'BMW ANN ARBOR STATION 01', '', '501 Auto Mall Dr', '48103', '3.25646', '42.285775', '-83.811745', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['19817', 'U-Haul', 'RENTAL_CAR_RETURN', '3655 S State St', '48108', '3.30497', '42.234259', '-83.737314', '', '', '', '', '', '7am-7pm M-Th and Sat, 7am-8pm F, 9am-5pm Sun'],
    ['39694', 'Marathon - Washtenaw Oil', 'CONVENIENCE_STORE', '3555 Washtenaw Ave', '48104', '3.54296', '42.255774', '-83.688609', '', '', '', '', '', '5am-2am daily'],
    ['40699', 'Speedway #8705', 'CONVENIENCE_STORE', '4001 S State St', '48108', '3.64053', '42.229197', '-83.7385', '', '', '', '', '', '24 hours daily'],
    ['172113', "DOMINO'S FARMS DOMINO'S FARMS", '', '24 Frank Lloyd Wright Dr', '48105', '4.11927', '42.316472', '-83.683413', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['69035', "DOMINO'S FARMS DOMINO'S FARMS2", '', '24 Frank Lloyd Wright Dr', '48105', '4.16802', '42.316357', '-83.682131', '2', '', 'ChargePoint Network', 'J1772', '', '24 hours daily'],
    ['99362', 'A & D Technology', 'OFFICE_BLDG', '4622 Runway Blvd', '48108', '4.36616', '42.219323', '-83.732229', '4', '', 'Non-Networked', 'J1772', 'Free', 'Open to public after company business hours'],
    ['182710', 'WASHCOMMCOLLEGE PARKING 5', '', '4800 E Huron River Dr', '48105', '4.44808', '42.262458', '-83.665546', '2', '', 'ChargePoint Network', 'J1772', '', 'Mon 6:30am - 10:30pm; Tue 6:30am - 10:30pm; Wed 6:30am - 10:30pm; Thu 6:30am - 10:30pm; Fri 6:30am - 10:30pm; Sat 6:30am - 10:30pm; Sun 6:30am - 10:30pm'],
    ['182709', 'WASHCOMMCOLLEGE PARKING 3', '', 'Parking Structure', '48197', '4.48194', '42.262318', '-83.664913', '2', '', 'ChargePoint Network', 'J1772', '', 'Mon 6:30am - 10:30pm; Tue 6:30am - 10:30pm; Wed 6:30am - 10:30pm; Thu 6:30am - 10:30pm; Fri 6:30am - 10:30pm; Sat 6:30am - 10:30pm; Sun 6:30am - 10:30pm'],
    ['182708', 'WASHCOMMCOLLEGE PARKING 4', '', '4800 E Huron River Dr', '48105', '4.50423', '42.26281', '-83.664258', '2', '', 'ChargePoint Network', 'J1772', '', 'Mon 6:30am - 10:30pm; Tue 6:30am - 10:30pm; Wed 6:30am - 10:30pm; Thu 6:30am - 10:30pm; Fri 6:30am - 10:30pm; Sat 6:30am - 10:30pm; Sun 6:30am - 10:30pm'],
    ['164341', '173 - Ann Arbor', '', '5645 Jackson Road', '48103', '4.85607', '42.286346', '-83.842995', '4', '2', 'Greenlots', 'CHADEMO J1772 J1772COMBO', '', '24 hours daily'],
    ['202411', 'WASHTENAW BP 2', '', '4975 Washtenaw Ave', '48108', '4.93659', '42.25076', '-83.66148', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily'],
    ['202417', 'WASHTENAW BP 1', '', '4975 Washtenaw Ave', '48108', '4.93684', '42.250736', '-83.66149', '', '1', 'ChargePoint Network', 'CHADEMO J1772COMBO', '', '24 hours daily']
    ]

    # Test record
    # ['TEST 123', 'Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', 'PARKING_GARAGE', '120 W Ann St', '48104', '0.09349', '42.282617', '-83.749329', '2', '', 'Non-Networked', 'J1772', 'Variable parking fee', '24 hours daily']

# Separate headers from the data
headers = data[0]
stations = data[1:]

# 1.0 COMPOUND STATEMENTS

# Return list of unique "ev_level2_evse_num" values
ev_level2_evse_num_vals = []
idx = headers.index('ev_level2_evse_num') # lookup index value
for station in stations:
    if station[idx] not in ev_level2_evse_num_vals:
        ev_level2_evse_num_vals.append(station[idx])

# print(f"\n1.0.1 ev_level2_evse_num values = {ev_level2_evse_num_vals}")

# INCORRECT SYNTAX
station_evse = []
idx = headers.index('ev_level2_evse_num') # lookup index value
# TODO Uncomment
# for station in stations:
#     if station[idx].isnumeric() and int(station[idx]) >= 2 and <= 4: # SyntaxError: invalid syntax
#         station_evse.append(f"{station[1]}: EVSEs = {station[idx]}")

# CORRECT SYNTAX
station_evse = []
idx = headers.index('ev_level2_evse_num') # lookup index value
for station in stations:
    if station[idx].isnumeric() and int(station[idx]) >= 2 and int(station[idx]) <= 4:
        station_evse.append(f"{station[1]}: EVSEs = {station[idx]}")

# TODO Uncomment
# print(f"\n1.0.3 Stations with 2-4 EVSEs (n={len(station_evse)}) = {station_evse}")

# PYTHONIC
station_evse = []
idx = headers.index('ev_level2_evse_num') # lookup index value
for station in stations:
    if station[idx].isnumeric() and 2 <= int(station[idx]) <= 4:
        station_evse.append(f"{station[1]}: EVSEs = {station[idx]}")

# TODO Uncomment
# print(f"\n1.0.4 Stations with 2-4 EVSEs (Pythonic) (n={len(station_evse)}) = {station_evse}")


# 1.1 LOGICAL AND OPERATOR

# U-M charging stations
um_count = 0
i = 0
while i < len(stations):
    if stations[i][1].startswith('U-M'):
        um_count += 1
    i += 1

# TODO Uncomment
# print(f"\n1.1.1 U-M charging stations = {um_count}")

# U-M charging stations filtered on a zip code
um_count_48104 = 0
i = 0
while i < len(stations):
    if stations[i][1].startswith('U-M') and int(stations[i][4]) == 48104:
        um_count_48104 += 1
    i += 1

# TODO Uncomment
# print(f"\n1.1.2 U-M charging stations = {um_count_48104}")


# CHALLENGE 01
um_stations_greene_st = []

# TODO Implement loop

# print(f"\nCh 01 U-M Greene St stations = {um_stations_greene_st}")


# 1.2 LOGICAL OR OPERATOR

# EV charging stations located at Meijer or at locations categorized as a "convenience store"
conv_stores = []
i = 0
while i < len(stations):
    if 'meijer' in stations[i][1].lower() or stations[i][2].lower() == 'convenience_store':
        conv_stores.append(stations[i][1])
    i += 1

# TODO Uncomment
# print(f"\n1.2.1 Convenience stores (n={len(conv_stores)})")
# pp.pprint(conv_stores) # pretty list


# CHALLENGE 02

# Add Shell station
conv_stores = []

# TODO Implement loop

# print(f"\nCh 02 Convenience stores (n={len(conv_stores)})")
# pp.pprint(conv_stores) # pretty list


# 1.3 LOGICAL NOT OPERATOR

# Return list of unique "ev_network" values (case sensitive)
ev_network_vals = []
for station in stations:
    if station[headers.index('ev_network')] not in ev_network_vals:
        ev_network_vals.append(station[headers.index('ev_network')])

# print(f"\n1.3.1 ev_network unique values (n={len(ev_network_vals)}) = {ev_network_vals}")

station_count = 0
i = 0
while i < len(stations):
    if stations[i][headers.index('ev_network')] == 'ChargePoint Network':
        station_count += 1
    i += 1

# print(f"\n1.3.2 ChargePoint network stations count = {station_count}")

# Count non ChargePoint network EV charging stations
station_count = 0
i = 0
while i < len(stations):
    if not stations[i][headers.index('ev_network')] == 'ChargePoint Network':
        station_count += 1
    i += 1

# print(f"\n1.3.3 Non ChargePoint network stations count = {station_count}")


# CHALLENGE 03

station_count = 0

# TODO Implement loop

# print(f"\nCh 03 Non J1772 connector stations = {station_count}")


# 1.4 GROUPING RELATED EXPRESSIONS

# Dedicated parking garages and lots
parking_facilities = []
i = 0
while i < len(stations):
    if (stations[i][2].lower() == 'parking_garage' or
        stations[i][2].lower() == 'pay_garage' or
        stations[i][2].lower() == 'parking_lot' or
        stations[i][1].lower().startswith('washcommcollege parking')):
        parking_facilities.append(stations[i])
    i += 1

# print(f"\n1.4.2 Parking facilities (n={len(parking_facilities)})")
# pp.pprint(parking_facilities)


# Parking facilities open 24 hours daily
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
i = 0
while i < len(stations):
    if (stations[i][2].lower() in facility_types or
        stations[i][1].lower().startswith('washcommcollege parking') and
        stations[i][-1].lower() == '24 hours daily'):
        parking_facilities.append(stations[i]) # Washtenaw Comm College parking EXCLUDED
    i += 1

# print(f"\n1.4.3.1 Parking facilities (n={len(parking_facilities)})")
# pp.pprint(parking_facilities)


# Parking facilities open 24 hours daily (includes other values)
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
i = 0
while i < len(stations):
    if (stations[i][1].lower().startswith('washcommcollege parking') or
        stations[i][2].lower() in facility_types and
        stations[i][-1].lower() == '24 hours daily'):
        parking_facilities.append(stations[i]) # Washtenaw Comm College parking INCLUDED
    i += 1

# print(f"\n1.4.3.2 Parking facilities (n={len(parking_facilities)})")
# pp.pprint(parking_facilities)

# Parking facilities open 24 hours daily
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
i = 0
while i < len(stations):
    if ((stations[i][1].lower().startswith('washcommcollege parking') or
        stations[i][2].lower() in facility_types) and
        stations[i][-1].lower() == '24 hours daily'):
        parking_facilities.append(stations[i]) # Washtenaw Comm College parking EXCLUDED
    i += 1

# print(f"\n1.4.3.3 Parking facilities (n={len(parking_facilities)})")
# pp.pprint(parking_facilities)

# Parking facilities open 24 hours daily
# Not reverses condition grouping
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
i = 0
while i < len(stations):
    if (not ((stations[i][1].lower().startswith('washcommcollege parking') or
        stations[i][2].lower() in facility_types)) and
        stations[i][-1].lower() == '24 hours daily'):
        parking_facilities.append(stations[i])
    i += 1

# print(f"\n1.4.3.4 Parking facilities (n={len(parking_facilities)})")
# pp.pprint(parking_facilities)


# 2.0 IF-ELIF-ELSE

chargepoint_count = 0
ev_connect_count = 0
evgo_count = 0
greenlots_count = 0
idx = headers.index('ev_network') # lookup index value

i = 0
while i < len(stations):
    if stations[i][idx].lower() == 'chargepoint network':
        chargepoint_count += 1
    elif stations[i][idx].lower() == 'ev connect':
        ev_connect_count += 1
    elif stations[i][idx].lower() == 'evgo network':
        evgo_count += 1
    elif stations[i][idx].lower() == 'greenlots':
        greenlots_count += 1
    i += 1

# Pass multiple strings
# print(f"\n2.0 Ann Arbor EV network charging station counts",
#     f"\nChargePoint count = {chargepoint_count}",
#     f"\nEV Connect count = {ev_connect_count}",
#     f"\nEVgo count = {evgo_count}",
#     f"\nGreenlots count = {greenlots_count}")


# CHALLENGE 04

network_count = 0
non_network_count = 0
network_unknown_count = 0
idx = headers.index('ev_network') # lookup index value

# TODO Implement loop

# Pass multiple strings
# print(f"\n2.0.1 Ann Arbor EV charging stations",
#     f"\nIn network count = {network_count}",
#     f"\nNon-network count = {non_network_count}",
#     f"\nUnknown count = {network_unknown_count}")
