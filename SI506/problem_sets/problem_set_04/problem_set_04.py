musicians = [['name', 'city', 'state', 'instruments', 'inspiration', 'birth_date', 'death_date'],
    [' Christian Scott Atunde Adjuah ', 'New Orleans', 'LA', ['trumpet'], 'Miles Davis', 'Mar 1983'],
    ['Ron Carter ', 'Ferndale', 'mi', ['double bass', 'cello'], 'Miles Davis', 'May 4, 1937'],
    [' Alice Coltrane ', 'Detroit', 'MI', ['piano', 'harp', 'vocals'], 'Ernest Farrow', '1937', '2007'],
    ['Esperanza Spalding', 'Portland', 'OR', ['double bass', 'guitar', 'vocals'], 'Ron Carter', '1984'],
    [' Robert Glasper ', 'Houston', 'tx', ['piano'], 'Herbie Hancock', 'April 1978'],
    [' Marquis Hill ', 'Chicago', 'IL', ['trumpet'], 'Lee Morgan', 'April 15, 1987'],
    [' Dorothy Ashby', 'Detroit', 'Mi', ['harp', 'piano', 'koto'], 'Omar Khayyam', 'Aug 1932', '1986'],
    ['Walter Smith III ', 'Houston', 'Tx', ['saxophone'], 'John Coltrane', 'Sept 24, 1980'],
    [' Cecile McLorin Salvant', 'Miami', 'fL', ['vocals'], 'Sarah Vaughan','August 28, 1989'],
    [' Sarah Elizabeth Charles', 'Springfield', 'MA', ['vocals'], 'Sarah Vaughan', '1989'],
    ['Miles Davis', 'Alton', 'iL', ['trumpet', 'cornet', 'piano'], 'Elwood Buchanan','1926', '1991'],
    ['John Coltrane', 'Hamlet', 'Nc', ['saxophone'], 'Alice Coltrane', 'Sep 1926', 'July 17, 1967'],
    ['Herbie Hancock', 'Chicago', 'il', ['piano', 'keyboard'], 'Miles Davis', '1940'],
    ['Roy Brooks ', 'Detroit', 'MI', ['drums'], 'Lionel Hampton','March 9, 1938', '2005'],
    ['Wayne Shorter', 'Newark', 'nj', ['saxophone'], 'John Coltrane', 'Aug 25, 1933'],
    [' Bobbi Humphrey', 'Marlin', 'TX', ['flute', 'vocals'], 'Herbie Mann', '1950'],
    [' Thelonius Monk', 'Rocky Mount', 'NC', ['piano'], 'Duke Ellington', '1917', 'February 17, 1982']
]

# PROBLEM 1 (16 POINTS)
def clean_list(info):
    leng = len(info)
    date = info[5]
    if( leng == 6):
        info.append(None)
    else:
        info[6] = int(info[6].split(',')[-1].split(' ')[-1])
    info[0] = info[0].strip()
    info[2] = info[2].lower()
    info[5] = int(date.split(',')[-1].split(' ')[-1])

for info in musicians[1:]:
    clean_list(info)
print(f'\nProblem 1: musicians =\n{musicians}')


# PROBLEM 2 (16 POINTS)
def get_state(info):
    return info[2].lower()

mi_musicians = []
for info in musicians[1:]:
    if get_state(info) == 'mi':
        mi_musicians.append(info[0])

print(f'\nProblem 2: mi_musicians =\n{mi_musicians}')


# PROBLEM 3 (16 POINTS)
south_states = ['al', 'ar', 'de', 'fl', 'ga', 'ky', 'la', 'md', 'ms',
    'nc', 'ok', 'sc', 'tn', 'tx', 'va', 'wv']

northeast_states = ['ct', 'ma', 'me', 'nh', 'nj', 'ny', 'pa', 'ri', 'vt']

def is_from_region(info, region):
    if  get_state(info) in region:
        return True
    else:
        return False

southerners = []
northeasterners = []

for info in musicians[1:]:
    if is_from_region(region=south_states, info=info):
        cur_tuple = tuple([info[0], info[2]])
        southerners.append(cur_tuple)
    elif is_from_region(region=northeast_states, info=info):
        cur_tuple = tuple([info[0], info[2]])
        northeasterners.append(cur_tuple)

print(f'\nProblem 3: southerners =\n{southerners}')
print(f'\nProblem 3: northeasterners =\n{northeasterners}')



# PROBLEM 4 (16 POINTS)
def is_inspired(info, inspo, idx=4):
    if info[idx] == inspo:
        return True
    else:
        return False

davis_count = 0
all_musicians = 0
davis_percent = 0

for info in musicians[1:]:
    if is_inspired(info, 'Miles Davis', 4):
        davis_count += 1
    all_musicians += 1

davis_percent = round(davis_count / all_musicians * 100, 2) 

print(f'\nProblem 4: davis_count =\n{davis_count}')
print(f'\nProblem 4: davis_percent =\n{davis_percent}')


# PROBLEM 5 (16 POINTS)
youngest_musicians = []
min_age = 999
def calculate_age(info, end_year=2022):
    if info[-1] == None:
        cur_tuple = tuple([info[0], end_year - info[5]])
        return cur_tuple
    else:
        cur_tuple = tuple([info[0], info[-1] - info[5]])
        return cur_tuple

for info in musicians[1:]:
    name, age = calculate_age(info, 2022)
    if(min_age > age):
        youngest_musicians = []
        youngest_musicians.append(name)
        min_age = age
    elif min_age == age:
        youngest_musicians.append(name)

print(f'\nProblem 5: youngest_musicians =\n{youngest_musicians}')

# PROBLEM 6 (20 POINTS)
past_musicians = []
current_musicians = []

j = 1
while (j < len(musicians)):
    info = musicians[j]
    if(info[-1] == None):
        cur_tuple = calculate_age(info, 2022)
        current_musicians.append(cur_tuple)
    else:
        cur_tuple = calculate_age(info, 2022)
        past_musicians.append(cur_tuple)
    j +=1
    
print(f'\nProblem 6: past_musicians =\n{past_musicians}')
print(f'\nProblem 6: current_musicians =\n{current_musicians}')

# PROBLEM 7 (25 POINTS)
def plays_woodwind(info, idx=3):
    woodwinds = ['clarinet', 'trumpet', 'saxophone', 'flute', 'bassoon',
        'oboe', 'trumpet', 'piccolo', 'cornet']
    
    instructments = info[idx]
    for instructment in instructments:
        if instructment in woodwinds:
            return True
    
    return False

wind_musicians = 0
for info in musicians[1:]:
    if plays_woodwind(info, 3):
        wind_musicians += 1 

print(f'\nProblem 7: wind_musicians =\n{wind_musicians}')
