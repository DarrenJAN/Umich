# SI 506 Lecture 05

# 1.0 SEQUENCES: LIST AND STRINGS

# 1.1 String basics

comedy_series = 'Monty Python'

# The object's unique identifier in memory
comedy_series_id = id(comedy_series)

# print(f"\n1.1 comedy_series (id={comedy_series_id}) = {comedy_series}")

# Return the object's type
comedy_series_type = type(comedy_series)

# print(f"\n1.1 comedy_series type (id={comedy_series_id}) = {comedy_series_type}")

# Return the object's length
comedy_series_len = len(comedy_series)

# print(f"\n1.1 comedy_series length (id={comedy_series_id}) = {comedy_series_len}")

# UNCOMMENT: Immutability check
# comedy_series[0] = 'm' # TypeError: 'str' object does not support item assignment

# String concatenation
comedy_series = comedy_series + "'s Flying Circus" # string concatenation (new object)

# print(f"\n1.1 comedy_series (id={comedy_series_id}) = {comedy_series}")


# 1.2 List basics

pythons = [
    'Graham Chapman',
    'John Cleese',
    'Terry Jones',
    'Eric Idle',
    'Michael Palin'
    ]

# The object's unique identifier in memory
pythons_id = id(pythons)

# print(f"\n1.2 pythons (id={id(pythons)}) = {pythons}")

# Return the type
pythons_type = type(pythons)

# print(f"\n1.2 pythons type (id={id(pythons)}) = {pythons_type}")

# Return the length
pythons_len = len(pythons)

# print(f"\n1.2 pythons len (id={id(pythons)}) = {pythons_len}")

# In-place method call mutates the list.
pythons.append('Terry Gilliam')
# pythons.insert(-1, 'Terry Gilliam')
# pythons.extend(['Terry Gilliam'])

# print(f"\n1.2 pythons (id={id(pythons)}) = {pythons}")

# List concatenation
pythons = pythons + ['Neil Innes'] # list concatenation (new list)

# print(f"\n1.2 pythons (id={id(pythons)}) = {pythons}") # new identity


# 2.0 INDEXING

# 2.1 Accessing a character by position

name = 'Monty Python'
letter = name[0] # first letter (zero-based index)

# print(f"\n2.1.1 Letter = {letter}")

letter = name[4]

# print(f"\n2.1.2 Letter = {letter}")

letter = name[-1]

# print(f"\n2.1.3 Letter = {letter}")


# 2.2 Index operator (list)

menu = [
    'Egg and bacon',
    'Egg, sausage and bacon',
    'Egg and Spam',
    'Egg, bacon and Spam',
    'Egg, bacon, sausage and Spam',
    'Spam, bacon, sausage and Spam',
    'Spam, egg, Spam, Spam, bacon and Spam',
    'Spam, Spam, Spam, egg and Spam',
    'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam',
    'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam'
    ]

menu_item = menu[1] # second element (zero-based index)

# print(f"\n2.2.1 Menu item = {menu_item}")

menu_item = menu[-2]

# print(f"\n2.2.2 Menu item = {menu_item}")

# 2.3 Trigger an IndexError exception
# menu_item = menu[10] # IndexError: list index out of range#


# 3.0 SLICING

cast = [
    'Terry Jones, Waitress',
    'Eric Idle, Mr Bun',
    'Graham Chapman, Mrs Bun',
    'John Cleese, The Hungarian',
    'Michael Palin, Historian',
    'Extra, Viking 01',
    'Extra, Viking 02',
    'Extra, Viking 03',
    'Extra, Viking 04',
    'Extra, Viking 05',
    'Extra, Viking 06',
    'Extra, Police Constable'
]

# 3.1 slice from index 0 to index n (stride = 1)

# Return Mr and Mrs Bun
cast_members = cast[1:3]

# print(f"\n3.1.1 The Buns = {cast_members}")

# Return Mr and Mrs Bun (negative slice)
cast_members = cast[-11:-9]

# print(f"\n3.1.2 The Buns (negative slice) = {cast_members}")


# 3.2 slice from index 0 to index n (stride = 1)
cast_members = cast[:5] # or cast[0:5]

# print(f"\n3.2 Named cast members = {cast_members}")


# 3.3 slice from index -n to end of list inclusive (stride = 1)
cast_members = cast[-7:] # warn: not the same as cast[-7:-1]

# print(f"\n3.3 Extras = {cast_members}")


# 3.4 slice with a specified stride

# Return cast members in reverse order
cast_members = cast[::-1]

# print(f"\n3.4.1 Cast members reverse order = {cast_members}")

# Return every other cast member starting from the first element
cast_members = cast[::2]

# print(f"\n3.4.2 Every other cast member = {cast_members}")

# Return every other cast member starting from the last element (negative stride)
cast_members = cast[::-2] # reverse

# print(f"\n3.4.3 Every other cast member (negative stride) = {cast_members}")

# Return every other Viking starting with Viking 01.
cast_members = cast[5:11:2]

# print(f"\n3.4.4 Every other Viking = {cast_members}")

# Return every other Viking starting with Viking 01 in reverse order.
cast_members = cast[5:11:-2] # Fails: empty list returned

# print(f"\n3.4.4 Every other Viking reverse order = {cast_members}")

# Workaround
cast_members = cast[5:11]
cast_members = cast_members[::-2]

# print(f"\n3.4.5 Every other Viking reverse order workaround = {cast_members}")


# CHALLENGE 01

# print(f"Ch 01 Cast = {cast}")

cleese_palin = None # TODO slice

# print(f"\nCh 01 Cleese and Palin = {cleese_palin}")

jones_graham_palin = None # TODO slice

# print(f"\nCh 01 Jones, Graham, and Palin = {jones_graham_palin}")


# 3.5 Slice Assignment

mounties = [
    'Extra, Canadian Mountie 01',
    'Extra, Canadian Mountie 02',
    'Extra, Canadian Mountie 03',
    'Extra, Canadian Mountie 04',
    'Extra, Canadian Mountie 05',
    'Extra, Canadian Mountie 06'
]

# 3.5.1 Replace part of a list (length unchanged)
cast[5:11] = mounties[0:] # replace Vikings with Mounties

# print(f"\n4.5.1 Replace Vikings with Canadian Mounties = {cast}")

# 3.5.2 Replace part of a list (length changes)
cast[5:11] = mounties[1:5] # replace Vikings with mounties 02-04 (negative slice)

# print(f"\n4.5.2 Replace Vikings with mounties 02-04 = {cast}")


# 3.6 Built-in del() function and slicing

# Delete a slice with built-in del() function

# Delete the Mounties (retain the Police Constable)
del(cast[-5:-1])
# del(cast[5:9])

# print(f"\n3.6 Delete Mounties = {cast}")


# 3.7 built-in slice() function

# slice([start, ]end[, step]) object
s = slice(1, 4, 2) # Returns Idle and Cleese
cast_members = cast[s]

# print(f"\n3.7 slice() example = {cast_members}")


## 4.0 STR AND LIST METHODS

menu_item = 'Spam, egg, Spam, Spam, bacon and Spam'

# str.lower() -- no argument method
menu_item_lower = menu_item.lower()

# print(f"\n4.0.1 {menu_item_lower}")

# str.count(value, start=0, end=len(str) - 1) -- start and end are optional
spam_count = menu_item.count('Spam')

# print(f"\n4.0.2 {spam_count}")

# str.split(sep=' ', maxsplit=-1) -- sep and maxsplit are optional
items = menu_item.split(', ') # returns list

# print(f"\n4.0.3 {items}")

# list.remove(element) -- in place operation; removes 1st occurence; returns None
items.remove('egg')

# print(f"\n4.0.4 {items}")

# Do not do this: items variable no longer points to a list object
items = items.remove('bacon and Spam') # None is returned

# print(f"\n4.0.5 {items}")

# Chained method calls
menu_item = 'Egg, bacon, sausage and Spam'

# Good. Replace, convert to lower case, and split.
items = menu_item.replace(' and', ',').lower().split(', ')

# print(f"\n2.1.1 {items}")

# Bad. The trailing list.append() returns None (oops!)
items = menu_item.replace(' and', ',').lower().split(', ').append('pancakes')

# print(f"\n2.1.2 {items}")

# Ugly. Premature split. Calling lower on a list object raises a runtime error
# AttributeError: 'list' object has no attribute 'lower'

# TODO UNCOMMENT (WARN: RAISES EXCEPTION)
# items = menu_item.replace(' and', ',').split(', ').lower()

# # print(f"\n2.1.3 {items}")


# 5.0 SELECT STR METHODS

menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam"""

# str.startswidth()
is_first = menu.startswith('Spam')

# print(f"\n5.1 is_first = {is_first}") # formatted string literal (f-string)

# str.lower()
lower_case = menu.lower()

# print("\n5.2 lower_case = %s" % lower_case) # old school placeholder formatting (yuck)

# str.count()
spam_count = menu.count('Spam')

# print(f"\n5.3 spam_count = {spam_count}\n")

# str.replace()
gummies_menu = menu.replace('Spam', 'Gummies')

# print("\n5.4 gummies_menu = {}".format(gummies_menu)) # str.format()

# str.strip()
monty_python = " Monty Python's Flying Circus \n" # note apostrophe

# print(f"\n5.5.1 Monty Python = {monty_python}")

monty_python = monty_python.strip() # note reassignment

# print(f"\n5.5.2 Monty Python (stripped) = {monty_python}")

# str.join()
items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ''.join(items) # join to blank or empty string (not so good in this case)

# print(f"\n5.6.1 Menu item = {menu_item}")

menu_item = ', '.join(items) # better

# print(f"\n5.6.2 Menu item = {menu_item}")

# str.find()
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('Spam')

# print(f"\n5.7.1 Index position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('ham')

# print(f"\n5.7.2 Index position = {position}")

# str.index()
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.index('egg and Spam')

# print(f"\n5.8.1 Index position = {position}")

# TODO UNCOMMENT (WARN: RAISES RUNTIME EXCEPTION)
# position = menu_item.index('ham')

# # print(f"\n5.8.2 Index position = {position}")

# str.split()
menu_item = 'Spam, bacon, sausage, Spam'
dish_items = menu_item.split(', ') # returns list

# print("\n5.9 dish items = {}".format(dish_items)) # str.format()

# str.splitlines()
menu_items = menu.splitlines() # returns list

# print("\n5.10 Menu_items = {}".format(menu_items)) # str.format()


# CHALLENGE 02

menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam"""

healthy_choice = 'Oatmeal'

menu_v2 = None # TODO Implement

# TODO Uncomment
# print(f"\nCh 02 menu_v2 = {menu_v2}")

# BONUS: Add menu item
# Multiline expression surrounded with parentheses (...)
bonus_menu_v2 = None # TODO Implment (if time permits)

# TODO Uncomment
# print(f"\nCh 02 bonus_menu_v2 = {bonus_menu_v2}")


# 6.0 LIST METHODS

# list.append() (in-place)
# TODO Uncomment
# menu_v2.append('red beans and rice') # modify in-place (no variable assignment)

# print(f"\n6.1 New menu item = {menu_v2}")

# list.remove() (in-place)
# TODO Uncomment
# item = menu_v2[-2] # Lobster Thermidor
# menu_v2.remove(item)

# print(f"\n6.2 Lobster Thermidor removed = {menu_v2}")

# list.extend() (in-place)
healthy_items = ['cereal, yogurt, and spam', 'oatmeal, fruit plate, and spam']
# TODO Uncomment
# menu_v2.extend(healthy_items)

# print(f"\n6.3 new menu extended = {menu_v2}")

# list.sort() (in-place)
# TODO Uncomment
# menu_v2.sort() # default alpha sort

# print(f"\n6.4 New menu sorted = {menu_v2}")

# list.index()
# TODO Uncomment
# index = menu_v2.index('egg, bacon and spam')

# print(f"\n6.5 Index postion = {index}")

# list.insert() (in-place)
# TODO Uncomment
# menu_v2.insert(1, 'belgian waffle, strawberries, and spam')

# print(f"\n6.6 Belgian waffle added to the menu = {menu_v2}")

# list.pop()
# TODO Uncomment
# retired_item = menu_v2.pop(-1) # pop the last item out of the list

# print(f"\n6.7 Retired item = {retired_item}")

# list.copy()

# print(f"\n6.8.1 menu_v2 (len={len(menu_v2)}) = {menu_v2}")

# Don't do this
# TODO Uncomment
# new_menu = menu_v2 # not a copy
# popped = new_menu.pop(-1) # mutates both new_menu and menu_v2

# print(f"\n6.8.1 popped item = {popped}")
# print(f"\n6.8.1 menu_v2 (len={len(menu_v2)}) = {menu_v2}") # lost an item

# Do this
# TODO Uncomment
# new_menu = menu_v2.copy() # shallow copy
# popped = new_menu.pop(-1) # mutates new_menu only

# print(f"\n6.8.2 menu_v2 (len={len(menu_v2)}) = {menu_v2}") # no change


# CHALLENGE 03

# Copy menu_v2 to menu_v3 (shallow copy)
menu_v3 = None # TODO Make a shallow copy

# TODO Uncomment
# print(f"\nCh 03 menu_v3 start (len={len(menu_v3)}) = {menu_v3}") # Start

# Reverse order
menu_v3 = None # TODO employ slicing

# TODO Uncomment
# print(f"\nCh 03 menu_v3 reversed (len={len(menu_v3)}) = {menu_v3}")

# Calculate length
menu_v3_len = None # Call built-in function

# TODO Uncomment
# print(f"\nCh 03 menu_v3 len = {menu_v3_len}")

# Access last element using menu_v3_len
# WARN: indexes are zero-based.
menu_item = None # TODO access element

# Remove last element

# TODO Remove menu_item from menu (in-place operation)

# TODO Uncomment
# print(f"\nCh 03 menu_v3 last item removed (len={len(menu_v3)}) = {menu_v3}")

# Return every other menu item
menu_v3 = None # TODO employ slicing

# TODO Uncomment
# print(f"\nCh 03 menu_v3 every other item (len={len(menu_v3)}) = {menu_v3}")


# 7.0 STRING FORMATTING

# Formatted string literal (f-string)
special_item = 'egg, bacon, spam and sausage'
question = f"Why can't she have {special_item}?"

# print(f"\n7.1 f-string = {question}") # embedded variable

# str.format()s
question = "Could I have {}, {}, {} and {}, without the spam?".format('egg', 'bacon', 'spam', 'sausage')

# print(f"\n7.2 str.format() = {question}")

# 7.3 C-style or simple provisional formatting
question = "No, it wouldn't be %s, %s, %s and %s, would it?" % ('egg', 'bacon', 'spam', 'sausage')

# print(f"\n7.3.1 C-style = {question}")

string = "%s %i %c" % ('Spam Sketch (', 1970, ')')

# print(f"\n7.3.2 C-style = {string}")
