# SI 506 Lecture 10

# Note: removed cholesterol_mg and saturated_fat_mg key-value pairs from each
# cereal: all values equal 0 mg.

# 1.1 DEFINING A FUNCTION

def print_slogan():
    print('\n1.1 Snap, Crackle, Pop') # Kellogg's Rice Crispies slogan

# TODO Uncomment
# print_slogan() # call function


# 1.2 DEFINING A FUNCTION WITH A PARAMETER

def print_slogan(slogan):
    print(f"\n1.2 {slogan}")

# TODO Uncomment
# slogan = 'They’rrrre GR-R-REAT'
# print_slogan(slogan)


# 1.3 MULTIPLE PARAMETERS

# TODO Implement function

cereal = 'Wheaties'
slogan = 'The Breakfast of Champions.'
wheaties_slogan = None # TODO call function

# print(f"\n1.3.1 {wheaties_slogan}")

cereal = 'Trix'
slogan = 'Silly Rabbit. Trix are for Kids.' # General Mills Trix
trix_slogan = None # TODO call function

# print(f"\n1.3.2 {trix_slogan}")


# 1.4 ARGUMENT ORDER MATTERS (PASSED POSITIONALLY)

cereal = 'Lucky Charms'
slogan = 'They’re always after me lucky charms' # General Mills Lucky Charms leprechaun
lucky_charms = None # TODO call function # Oops! string reversed

# print(f"\n1.4 String reversed\n{lucky_charms}")


# 1.5 KEYWORD ARGUMENTS (ANY ORDER ACCEPTABLE)

lucky_charms = None # TODO call function # pass args by keyword

# print(f"\n1.5 {lucky_charms}")


# 1.6 OPTIIONAL PARAMETERS

def format_slogan(name, slogan, separator=': '):
    return f"{name}{separator}{slogan}"

cereal = 'Honey-nut Cheerios'
slogan = 'Bee Happy, Bee Healthy'

# TODO Uncomment
# honey_nut_cheerios = format_slogan(cereal, slogan) # no need to pass third arg

# print(f"\n1.6.1 {honey_nut_cheerios}")

honey_nut_cheerios = None # TODO call function (line break passed)

# print(f"\n1.6.2 {honey_nut_cheerios}")

# INFO: note use of two return statements
def format_slogan(name, slogan, separator=': ', all_caps=False):
    if all_caps:
        return f"{name.upper()}{separator}{slogan.upper()}"
    else:
        return f"{name}{separator}{slogan}"

cereal = 'Cinnamon Toast Crunch'
slogan = 'Unlock the Cinnaverse'

# WARN: < all_caps > keyword argument is required since < separator > is not specified
cinn_toast_crunch = None # TODO call function

# print(f"\n1.6.3 {honey_nut_cheerios}")


# CHALLENGE 01

cereals = [
    ['General Mills', 'Cocoa Puffs'],
    ['Kellogg Company', 'Frosted Flakes'],
    ['Post Consumer Brands', 'Grape-nuts'],
    ['Kellogg Company', 'Raisin Bran'],
    ['General Mills', 'Cheerios'],
    ['Post Consumer Brands', 'Shredded Wheat (spoon size)'],
    ['General Mills', 'Lucky Charms'],
    ['Quaker Oats Company', "Cap'n Crunch"]
    ]

# TODO Implement function

post_cereals = None # TODO call function
kellogg_cereals = None # TODO call function

# print(f"\nCh 01 Post cereals = {post_cereals}")
# print(f"\nCh 01 Kellogg's cereals = {kellogg_cereals}")


# 2.0 FUNCTIONS AND LOOPS

cereals = [
    ['company_name', 'product_name', 'ingredients', 'serving_size_gm', 'calories', 'sodium_mg', 'sugar_gm', 'protein_gm'],
    ['Kellogg Company', 'Frosted Flakes', ['Milled Corn', 'Sugar', 'Malt Flavoring', 'High Fructose Corn Syrup', 'Salt'], 37, 130, 190, 12, 2],
    ['Kellogg Company', 'Raisin Bran', ['Whole Grain Wheat', 'Raisins', 'Wheat Bran', 'Sugar', 'High Fructose Corn Syrup'], 59, 190, 200, 17, 5],
    ['General Mills', 'Cheerios', ['Whole Grain Oats', 'Modified Corn Starch', 'Sugar', 'Salt'], 36, 140, 230, 12, 3],
    ['General Mills', 'Cocoa Puffs', ['Whole Grain Corn', 'Sugar', 'Corn Syrup', 'Cornmeal', 'Canola and or Rice Bran Oil'], 36, 140, 130, 12, 2],
    ['General Mills', 'Lucky Charms', ['Oats', 'Marshmallows', 'Sugar', 'Corn Syrup', 'Corn Starch'], 36, 140, 230, 12, 3],
    ['Post Consumer Brands', 'Shredded Wheat (spoon size)', ['Whole Grain Wheat'], 60, 210, 0, 0, 7],
    ['Post Consumer Brands', 'Grape-nuts', ['Whole Grain Wheat', 'Flour', 'Malted Barley Flour', 'Salt', 'Dried Yeast'], 58, 200, 280, 5, 6]
    ]

def format_ingredients(cereal):
    return ', '.join(cereal[2])

cereal_ingredients = []
for cereal in cereals[1:]:
    cereal_name = cereal[1]
    ingredients = format_ingredients(cereal) # call function
    cereal_ingredients.append(f"{cereal_name} ingredients: {ingredients}")

# TODO Uncomment
# print(f"\n2.0 Breakfast cereals\n")
# for cereal in cereal_ingredients:
#     print(cereal)


# 3.0 FUNCTIONS CALLING OTHER FUNCTIONS

def has_corn_syrup(cereal):
    has_corn_syrup = False

    for ingredient in cereal[2]:
        if 'corn syrup' in ingredient.lower():
            has_corn_syrup = True
            break

    return has_corn_syrup

# Alternative (two return statements; no break)
# def has_corn_syrup(cereal):
#     for ingredient in cereal[2]:
#         if 'corn syrup' in ingredient.lower():
#             return True # exit function; terminates loop
#     return False


def get_cereals_with_corn_syrup(cereals):
    results = []

    for cereal in cereals:
        if has_corn_syrup(cereal): # delegates question to another function
            results.append(cereal)

    return results

# call function
cereals_with_corn_syrup = get_cereals_with_corn_syrup(cereals)

# TODO Uncomment
# print(f"\n3.0 Cereals with corn syrup\n {cereals_with_corn_syrup}")


# CHALLENGE 02 CEREALS BY INGREDIENT

# Implement helper function

# Implement function

cereals_with_oats = None # TODO Call function

# print(f"\n4.1 Cereals by ingredient\n {cereals_with_oats}")


# CHALLENGE 03 HIGHEST SUGAR CONTENT

headers = None # TODO Extract headers

# TODO Implement function

cereals_max_sugar = []
max_sugar_grm = 0

# TODO Implement loop

# print(f"\n4.2 Max sugar content ({max_sugar_grm} gms)\n{cereals_max_sugar}")
