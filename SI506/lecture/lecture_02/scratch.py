# SI 506 lecture 02

# Sequence: list of tuples assigned to variable
teaching_team = [
    ('Tasha', 'GSI'),
    ('Yaoqi', 'GSI'),
    ('Yash', 'GSI'),
    ('Swathi', 'IA'),
    ('Joshua', 'IA'),
    ('Anthony', 'Instructor')
    ]

# Access "Yash" tuple by index (zero-based) and assign to variable
yash = teaching_team[2]

# Print name of GSI
print(yash[0])

# Access IAs (negative slice); returns list
ia_members = teaching_team[-3:-1]

# check ia_members type and print
print(type(ia_members))

# Role count {'GSI': x, 'IA': y, 'Instructor': z}
role_counts = {} # dictionary of key-value pairs
for member in teaching_team:
    if member[1] in role_counts.keys():
        role_counts[member[1]] += 1 # existing k-v pair; increment
    else:
        role_counts[member[1]] = 1 # add new k-v pair

# print dictionary
print(role_counts)
