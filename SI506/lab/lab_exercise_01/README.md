
# SI 506: Lab Exercise 01

## This week's Lab Exercise

This week's lab exercise includes eight (8) problems that focus on comments, using built-in functions, basic arithmetic operations, and basic list operations.

:bulb: In order to check your work, try using the built-in function `print()` to print out the results.


## 1.0 Problem 01 (2 Points)

You've been provided with four (4) variables that represent locations on campus. These variables have been assigned string values that contain the names of those locations. Create a list called `locations` that contains the four variables.

:bulb: You must use **exactly the same** list name provided in the instructions in order to pass the auto grader.

## 2.0 Problem 02 (2 Points)

Use the built-in function `len()` to return the number of elements in the list `locations`. Assign the return value to a new variable named `num_locations`.


## 3.0 Problem 03 (2 Points)

The variables, `north_quad_study_areas`, `ccrb_study_areas`, `kelsey_museum_study_areas`, and `mason_hall_study_areas` all have the number of study areas assigned to them as an integer. Calculate the total number of study areas among these four buildings by adding up the variables and assigning the computed value to a new variable called `total_study_areas`

:bulb: You can add mulitple variables together in one assignment statement. Also these numbers represent approximate numbers of study areas.

## 4.0 Problem 04 (2 Points)

Calculate the average number of study areas per building among North Quad, CCRB, the Kelsey Museum, and Mason Hall by using the `total_study_areas` variable computed in Problem 03 and dividing it by the number of buildings you computed earlier.

:bulb: Consider using **floor division** here.

## 5.0 Problem 05 (4 Points)

The variable `study_areas` is a string with the same data provided earlier about buildings and study rooms. Replace each semi-colon with a colon and assign the new string object to a variable named `fixed_locations`.

:bulb: Each building should be followed by a colon, then the number of study areas in that building.

## 6.0 Problem 06 (4 points)

Create a list by splitting the string `fixed_locations`. Assign this list to a new variable named `study_area_locations`.

:bulb: Watch for spaces when using the `str.split()` method; the resultant list elements must have one space after splitting on the comma ", ".

## 7.0 Problem 07 (2 points)

Build a formatted string literal (f-string) using the variable `study_area_locations` from the previous problem. Create a variable named `statement` and assign the string to it.

The f-string has the following output:

``` "The locations and the number of study areas they contain are ['Central Campus Recreation Building: 0', 'Kelsey Museum of Archeology: 9', 'Mason Hall: 22', 'North Quad: 30']" ```

## 8.0 Problem 08 (2 points)

Use list slicing to assign the first two buildings and their study areas in `study_area_locations`. Created a variable named `two_smallest_buildings` and assign the value to it.

:bulb: Remember, there are several different ways to slice a list including starting from 0 or using negative numbers. Be careful about which values are inclusive or exclusive when you slice.
