# SI 506 Lecture 03

# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line string. This is actually a string
constant that is denoted by the use of triple quotation marks.
"""

# 3.0 VARIABLES

num = 506

welcome_message = 'Welcome to SI 506'

uniqnames = ['arwhyte', 'brooksch', 'collemc', 'csev', 'cteplovs']

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 4.0 VARIABLE NAMING RULES AND CONVENTIONS

# 4.1 Good

# Choose lowercase
uniqname = 'arwhyte'

# Separate words with underscore (_)
course_code = 'SI 506'

# Use plural form to indicate a set or sequence
course_codes = ['SI 504', 'SI 506', 'SI 507']

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 27

# "is_", "has_" Boolean true/false
is_enrolled = False
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://si506.org/'

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

print(f"\n4.2: function return value = {product}\n") # formatted string literal (f-string)

# For loop incorporating a counter < i > value
course_codes = ['SI 564', 'SI 574', 'SI 579', 'SI 582']
i = 1 # counter
for code in course_codes:
    print(f"{i}. {code}")
    i += 1 # addition assignment (increment)

print('\n') # pad with newline escape character

# Alternative: call built-in function enumerate()
for i, code in enumerate(course_codes, start=1):
    print(f"{i}. {code}")


# 4.3 Ugly (illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

# class = 'SI 506' # use clazz # TODO UNCOMMENT

# Illegal: variable name commences with a numeric value.

# 506_umsi = 'SI 506' # TODO UNCOMMENT

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

# $number = 506 # TODO UNCOMMENT

# Illegal: variable name includes a dash (`-`).

# course-list = ['SI 506', 'SI 507', 'SI 618'] # TODO UNCOMMENT

# Illegal: variable name includes whitespace.

# course name = 'SI 506' # illegal; uncomment to test


# 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 5.1 print(): print passed in object to the screen

# Passing a hard-coded string.
print('\n5.1.1: SI 506 rocks!') # \n = newline escape character

# Passing a variable name which points to a string.
print(f"\n5.1.2: print welcome_message = {welcome_message}") # formatted string literal

# Passing a variable name which points to a multiline string.
print(f"\n5.1.3: print multiline str = {chorus}")


# 5.2 type(): determine object's data type

data_type = type(num)
print(f"\n5.2.1: num type = {data_type}") # returns <class 'int'>

data_type = type(welcome_message)
print(f"\n5.2.2: welcome_message type = {data_type}") # returns <class 'str'>

data_type = type(uniqnames)
print(f"\n5.2.3: uniqnames type = {data_type}") # returns <class 'list'>


# 5.3 len(): check length of sequence (i.e., number of elements)

# TODO UNCOMMENT
# len = 10 # Shadowing built-in function name (avoid)
# Generates TypeError: 'int' object is not callable when len() is called below.

# Count characters in string (including whitespace).
char_count = len(welcome_message)
print(f"\n5.3.1: welcome_message length = {char_count}")

# Count number of elements in list.
uniqname_count = len(uniqnames)
print(f"\n5.3.2: uniqnames length = {uniqname_count}")


# 5.4 CHALLENGE 01

print(f"\n5.4 Challenge 01") # f-string

# Variable assignment
attractions = ['Detroit Observatory', 'Museum of Art', 'Museum of Natural History']
print(attractions)

# Return data type and print to screen (2 lines permitted)
attractions_type = type(attractions)
print(attractions_type)

# Return length and print to screen (one line only)
print(len(attractions))


# 6.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# 6.1 Variable assignment

# Counts
lecturer_count = 1
gsi_count = 3
ia_count = 2 # not considered instructors
lab_count = 6
student_count = 142

# Addition (+ operator)
team_count = lecturer_count + gsi_count + ia_count
print(f"\n6.1.1: teaching_team_count = {team_count}")

# Subtraction (- operator)
instructor_count = team_count - ia_count
print(f"\n6.1.2: instructor_count = {instructor_count}")

# Multiplication (* operator)
max_enrollment = lab_count * 25 # approximate
print(f"\n6.1.3: max_enrollment = {max_enrollment}")

# Floating point division (/ operator)
avg_lab_size = student_count / lab_count
print(f"\n6.1.4: average lab size = {avg_lab_size}")

# Floor division a.k.a integer division (//)
avg_lab_size = student_count // lab_count
print(f"\n6.1.5: average lab size = {avg_lab_size}")


### 6.2 Challenge 02

# ratio = 35.5:1
student_teacher_ratio = student_count / instructor_count
print(f"\n6.2.1 Student:Teacher ratio = {student_teacher_ratio}")

# Max enrolled percentage = 94.67%
max_enrolled_pct = student_count / max_enrollment * 100
print(f"\n6.2.2 Max enrolled percent = {max_enrolled_pct:.2f}")
