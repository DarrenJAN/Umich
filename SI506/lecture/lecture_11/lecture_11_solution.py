# SI 506 Lecture 11

# 1.0 TRUTH VALUES

cereal = []
truth_value = bool(cereal) # falsy

print(f"\n1.0.1 cereal list truth value = {truth_value}")

cereal = ["Cap'n Crunch", 'Quaker Oats Company'],

truth_value = bool(cereal) # truthy

print(f"\n1.0.2 cereal list truth value = {truth_value}")


# WHILE LOOP/INPUT() TRUTH VALUE TESTING EXAMPLE

cereals = (
    ('apple jacks', 12),
    ('cocoa puffs', 10),
    ('honey bunches of oats', 12),
    ('frosted flakes', 11),
    ('fruity pebbles', 11),
    ('raisin bran', 17)
    )


def find_cereal(cereals, cereal_name):
    """Attempts to match a cereal in < cereals > based on passed in < cereal_name >.
    If match occurs, cereal is returned immediately to the caller and the loop and
    function are terminated. otherwise None is returned."""

    for cereal in cereals:
        if cereal[0].lower() == cereal_name.lower():
            return cereal


# TODO Uncomment while loop

# prompt = '\nPlease name a high sugar content cereal: '
# cereal = None
# while not cereal:
#     name = input(prompt)
#     cereal = find_cereal(cereals, name) # attempt to match on name

#     # Check truth value of cereal
#     if cereal:
#         print(f"\n1.0.3 {cereal[0].title()} contains {cereal[1]} grams of sugar per serving.\n")
#     else:
#         prompt = '\nCereal not located. Please provide another cereal name: '


# 2.0 VARIABLE SCOPE

cocoa_puffs = [
    'General Mills',
    'Cocoa Puffs',
    [
        'Whole Grain Corn',
        'Sugar',
        'Corn Syrup',
        'Cornmeal',
        'Canola and or Rice Bran Oil'
        ]
    ]

if cocoa_puffs: # truth value
    cocoa_puffs_truth_value = True # variable now available globally

print(f"\n2.0.1: cocoa_puffs truth value = {truth_value}")


def get_cereal_ingredients(cereal):
    ingredients = cereal[2] # variable possesses local scope only
    return ingredients


# TODO UNCOMMENT (TRIGGER EXCEPTION)
# Triggers NameError: name 'ingredients' is not defined
# print(f"\n2.0.2: variable w/local scope only = {ingredients}")

# Variable has global scope
cocoa_puffs_ingredients = get_cereal_ingredients(cocoa_puffs) # call function

print(f"\n2.0.3: cocoa_puffs_ingrediants = {cocoa_puffs_ingredients}")


# 3.0 TUPLES

cereal = ('Rice Krispies',) # single item tuple
# cereal = 'Rice Krispies', # no parentheses (legal)
# cereal = ('Rice Krispies') # a string

print(f"\n3.0 Single item tuple (type={type(cereal)}) = {cereal}")

cereals = ('Rice Krispies', 'Corn Flakes', 'Frosted Mini-Wheats')

print(f"\n3.1 Single item tuple (type={type(cereals)}) = {cereals}")

# TODO Uncomment (trigger TypeError)
# cereals[1] = 'Fruit Loops' # TypeError: 'tuple' object does not support item assignment

cereals = (cereals[0],) + ('Fruit Loops',) + (cereals[-1],) # each a single tuple

print(f"\n3.2 Tuple concatenation (type={type(cereals)}) = {cereals}")

cereals = tuple([cereals[0], 'Fruit Loops', cereals[-1]]) # pass a list

print(f"\n3.3 Built-in function tuple (type={type(cereals)}) = {cereals}")

fruit_loops = cereals[1] # returns string

print(f"\n3.4 Tuple indexing (type={type(fruit_loops)}) = {fruit_loops}")

cereals_subset = cereals[-2:] # returns tuple

print(f"\n3.5 Tuple slicing (type={type(cereals_subset)}) = {cereals_subset}")

fruity_pebbles = ('fruity pebbles', 'Post Consumer Brands', 11)
cereal_name, manufacturer, sugar_content_gm = fruity_pebbles # unpack

print(f"\n3.6 Uunpack cereal name = {cereal_name}")
print(f"\n3.6 Unpack manufacturer = {manufacturer}")
print(f"\n3.6 Unpack sugar content (grams) = {sugar_content_gm}")

# TODO Uncomment (triggers ValueError)
# cereal_name, manufacturer, sugar_content_gm = fruity_pebbles[1:] # triggers a runtime exception
# cereal_name, manufacturer, sugar_content_gm, rating = fruity_pebbles # triggers a runtime exception


# 4.0 CHALLENGES

scale = [('5 stars', 5), ('4 stars', 4), ('3 stars', 3), ('2 stars', 2), ('1 star', 1)]

cereals = [
    ['Apple Jacks', 'Kellogg Company', (5, 185), (4, 21), (3, 10), (2, 4), (1, 2)],
    ["Cap'n Crunch", 'Quaker Oats Company', (5, 49), (4, 5), (3, 3), (2, 1), (1, 1)],
    ["Cap'n Crunch's Crunch Berries", 'Quaker Oats Company', (5, 196), (4, 15), (3, 6), (2, 2), (1, 4)],
    ['Cheerios', 'General Mills', (5, 1310), (4, 95), (3, 14), (2, 11), (1, 28)],
    ['Cinnamon Toast Crunch', 'General Mills', (5, 577), (4, 46), (3, 10), (2, 5), (1, 19)],
    ['Cocoa Puffs', 'General Mills', (5, 147), (4, 9), (3, 1), (2, 2), (1, 5)],
    ['Corn Flakes', 'Kellogg Company', (5, 467), (4, 45), (3, 9), (2, 3), (1, 10)],
    ['Frosted Flakes', 'Kellog Company', (5, 1465), (4, 116), (3, 37), (2, 11), (1, 35)],
    ['Frosted Mini-Wheats', 'Kellogg Company', (5, 883), (4, 95), (3, 18), (2, 6), (1, 26)],
    ['Fruit Loops', 'Kellogg Company', (5, 750), (4, 84), (3, 14), (2, 6), (1, 8)],
    ['Fruity Pebbles', 'Post Consumer Brands', (5, 170), (4, 23), (3, 8), (2, 2), (1, 7)],
    ['Grape-Nuts', 'Post Consumer Brands', (5, 322), (4, 25), (3, 3), (2, 1), (1, 15)],
    ['Honey Bunches of Oats', 'Post Consumer Brands', (5, 95), (4, 7), (3, 3), (2, 1), (1, 2)],
    ['Honey Nut Cheerios', 'General Mills', (5, 814), (4, 64), (3, 22), (2, 8), (1, 22)],
    ['Lucky Charms', 'General Mills', (5, 388), (4, 38), (3, 12), (2, 3), (1, 7)],
    ['Raisin Bran', 'Kellogg Company', (5, 946), (4, 79), (3, 21), (2, 14), (1, 30)],
    ["Reese's Puffs", 'General Mills', (5, 184), (4, 14), (3, 10), (2, 4), (1, 3)],
    ['Rice Krispies', 'Kellogg Company', (5, 429), (4, 31), (3, 11), (2, 5), (1, 13)],
    ['Shredded Wheat', 'Post Consumer Brands', (5, 208), (4, 13), (3, 6), (2, 5), (1, 11)],
    ['Wheaties', 'General Mills', (5, 215), (4, 18), (3, 5), (2, 2), (1, 12)]
]

# CHALLENGE 01

def get_cereal(cereals, cereal_name):
    for cereal in cereals:
        # if cereal[0] == cereal_name: # risky
        if cereal[0].lower() == cereal_name.lower():
            return cereal


lucky_charms = get_cereal(cereals, 'Lucky Charms')

print(f"\nCh 01: Lucky Charms = {lucky_charms}")


# CHALLENGE 02

def get_ratings(cereal):
    return cereal[2:]

raisin_bran = get_cereal(cereal_name='Raisin Bran', cereals=cereals)
raisin_bran_ratings = get_ratings(raisin_bran)

print(f"\nCh 02 {raisin_bran[0]} ratings = {raisin_bran_ratings}")


# CHALLENGE 03

cereal_ratings = []
for cereal in cereals:
    five, four, three, two, one = get_ratings(cereal)

    fav = five[1] + four[1]
    neutral = three[1]
    unfav = two[1] + one[1]

    string = f"{cereal[0]} ratings: favorable={fav}, neutral={neutral}, unfavorable={unfav}"
    cereal_ratings.append(string)

print(f"\nCh 03: Cereal ratings:\n{cereal_ratings}")


# CHALLENGE 04

def count_ratings(cereal):
    count = 0
    ratings = get_ratings(cereal)
    for rating in ratings:
        count += rating[1]
    return count

# Alternative (call get_ratings function in for loop)
# def count_ratings(cereal):
#     count = 0
#     for rating in get_ratings(cereal):
#         count += rating[1]
#     return count


def compute_favorability_rating(cereal):
    ratings = get_ratings(cereal)
    ratings_count = count_ratings(cereal)
    fav_pct = (ratings[0][1] + ratings[1][1]) / ratings_count * 100
    return fav_pct


cheerios = get_cereal(cereals, 'cheerios')
cheerios_fav_pct = compute_favorability_rating(cheerios)

print(f"\nCh 04 {cheerios[0]} favorability rating = {cheerios_fav_pct:.2f}%")
