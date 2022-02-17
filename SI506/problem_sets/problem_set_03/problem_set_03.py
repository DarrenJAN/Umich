# Problem Set 3

# SETUP
chinese_holidays = [
    ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
    ["New Year's Day", '2022-01-01', '3 days off', False],
    ['Spring Festival', '2022-02-01', '7 days off', True],
    ['Lantern Festival', '2022-02-15', '0 days off', False],
    ['Qingming Festival', '2022-04-05', '3 days off', True],
    ['Labor Day', '2022-05-01', '5 days off', True],
    ['Dragon Boat Festival', '2022-06-03', '3 days off', True],
    ['Qixi Festival', '2022-08-04', '0 days off', True],
    ['Mid-Autumn Festival', '2022-09-10', '3 days off', True],
    ['National Day', '2022-10-01', '7 days off', False],
    ['Double Ninth Festival', '2022-10-04', '0 days off', True]
]

activities = [
    ["New Year's Day", 'Decorating Houses | Eating Dumplings'],
    ['Spring Festival', 'Exchanging Red Envelopes | Family Reunion Dinner'],
    ['Lantern Festival', 'Watching Lanterns | Eating Tangyuan'],
    ['Qingming Festival', 'Tomb Sweeping | Spring Outing'],
    ['Labor Day', 'Visiting Tourist Spots | Shopping'],
    ['Dragon Boat Festival', 'Dragon Boat Racing | Eating Zongzi'],
    ['Qixi Festival', 'Dating | Shopping'],
    ['Mid-Autumn Festival', 'Eating Mooncakes | Family Reunion Dinner'],
    ['National Day', 'Military Parade | Visiting Tourist Spots'],
    ['Double Ninth Festival', 'Climbing Mountain | Eating Chongyang Cakes']
]


# Problem 1
print("Problem 1\n")
for holiday in chinese_holidays[1:]:
    day= holiday[2].split(' ')[0]
    holiday[2] = int(day)
    if int(day) == 0:
        holiday[-1] = False;
    else:
        holiday[-1] = True;
print(f"chinese_holidays = {chinese_holidays}\n") # UNCOMMENT TO CHECK

# Problem 2
print("Problem 2\n")
num_holidays = 0
for holiday in chinese_holidays[1:]:
    if( holiday[-1] == True):
        num_holidays = num_holidays + 1
print(f"num_holidays = {num_holidays}\n") # UNCOMMENT TO CHECK

# Problem 3
print("Problem 3\n")
public_holidays = []
other_holidays = []

for holiday in chinese_holidays[1:]:
    if( holiday[-1] == 0):
        other_holidays.append(holiday[0])
    else:
        public_holidays.append(holiday[0])

print(f"public_holidays = {public_holidays}\n") # UNCOMMENT TO CHECK
print(f"other_holidays = {other_holidays}\n") # UNCOMMENT TO CHECK


# Problem 4
print("Problem 4\n")

long_break = []
medium_break = []
short_break = []
no_break = []

for holiday in chinese_holidays[1:]:
    if( holiday[-2] == 0):
        no_break.append(holiday[0])
    elif ( holiday[-2]  <= 3 ):
        short_break.append(holiday[0])
    elif(   holiday[-2] > 3 and holiday[-2]<= 5):
        medium_break.append(holiday[0])
    else:
        long_break.append(holiday[0])

print(f"long_break = {long_break}\n") # UNCOMMENT TO CHECK
print(f"medium_break = {medium_break}\n") # UNCOMMENT TO CHECK
print(f"short_break = {short_break}\n") # UNCOMMENT TO CHECK
print(f"no_break = {no_break}\n") # UNCOMMENT TO CHECK

# Problem 5
print("Problem 5\n")
i = 1
while i < len(chinese_holidays):
    holiday = chinese_holidays[i]
    date = holiday[1]
    date_list = date.split("-")
    holiday[1] = date_list
    i +=1

print(f"chinese_holidays = {chinese_holidays}\n") # UNCOMMENT TO CHECK


# Problem 6
print("Problem 6\n")
Spring = ['03', '04', '05']
Summer = ['06', '07', '08']
Fall = ['09', '10', '11']
Winter = ['12', '01', '02']

for i in range(1, len(chinese_holidays)):
    holiday = chinese_holidays[i]
    month = holiday[1][1]
    Season = ''
    if month in Spring:
        Season = 'Spring'
        chinese_holidays[i].insert(0, 'Spring')
    elif  month in Summer:
        Season = 'Summer'
        chinese_holidays[i].insert(0, 'Summer')
    elif month in Fall:
        Season = 'Fall'
        chinese_holidays[i].insert(0, 'Fall')
    else:
        Season = 'Winter'
        chinese_holidays[i].insert(0, 'Winter')
    #chinese_holidays[i].insert(0, Season)

print(f"chinese_holidays = {chinese_holidays}\n") # UNCOMMENT TO CHECK

# Problem 7
print("Problem 7\n")
j = 0

while j < len(activities):
    all_activities = activities[j][1].split(' | ')
    if 'Eating Zongzi' in all_activities:
        dragon_boat_activities = all_activities
        break;
    j += 1

print(f"dragon_boat_activities = {dragon_boat_activities}\n") # UNCOMMENT TO CHECK

