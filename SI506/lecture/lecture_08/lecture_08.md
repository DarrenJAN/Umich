# SI 506 Lecture 08

## Topics

1. `break` and `continue` statements
2. `while` loop (indefinite iteration)
3. Built-in `input()` function
4. Challenges

## Vocabulary

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Index__. Numeric position of an element or item contained in an ordered sequence. Python
  indexes are zero-based, i.e., the first element's index value is 0 not 1.
  `len(< some_list >)` is considered an expression.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are
  examples of an iterable.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.

## 1.0 `break` and `continue` statements

You can interrupt control flow inside a loop using the `break` and `continue` statements.

## 1.1 `break` statement

The `break` statement is employed in a `for` loop to exit the loop and proceed to the next statement
in the code. Any statements inside the loop that follow the `break` statement will be ignored. The
break statement is usually triggered by a specified condition. Using a `break` statement prevents
unnecessary looping and can result in performance gains if the sequence being looped over is large.

For example, given a select list of model year 2021 electric passenger vehicles derived from the US
Department of Energy's [Fuel Economy](https://www.fueleconomy.gov/feg/ws/index.shtml) how could you
confirm programmatically whether or not the the Chinese battery and vehicle manufacturer
_Kandi Technologies Group_ is included in the `elec_vehicles` list?

```python
elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Company', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
    ['Kandi Technologies Group', 'Kandi', 'K27', 2021, 59, 51.6, 64.3, 102, 7.0],
    ['General Motors Co.', 'Chevrolet', 'Bolt EV', 2021, 259, 235.1, 277.7, 108, 9.3],
    ['Volkswagen AG', 'Audi', 'e-tron', 2021, 222, 221.9408, 222.74, 77, 10.0],
    ['Nissan Motor Co.', 'Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149, 131.3, 163.2, 99, 8.0],
    ['Tesla, Inc.', 'Tesla', 'Model 3 Performance AWD', 2021, 315, 299.0, 328.7, 107, 10.0],
    ['Volvo Group', 'Volvo', 'XC40 AWD BEV', 2021, 208, 188.0, 223.6, 72, 8.0],
    ['Volkswagen AG', 'Volkswagen', 'ID.4 1st', 2021, 250, 230.1587, 266.7659, 89, 7.5],
    ['Volvo Group', 'Polestar', '2', 2021, 233, 222.1, 241.9, 88, 8.0],
    ['Bayerische Motoren Werke AG', 'BMW', 'i3s', 2021, 153, 136.4, 166.5, 102, 7.0],
    ['Bayerische Motoren Werke AG', 'Mini', 'Cooper SE Hardtop 2 door', 2021, 110, 101.9, 116.9, 100, 4.0],
    ['Tesla, Inc.', 'Tesla','Model S Performance (19in Wheels)', 2021, 387, 373.2, 398.3, 106, 14.7]
]
```

One solution is to implement a `for` loop, checking for the existence of the automaker in the list
and, if found, assign the boolean value `True` to a variable (e.g., `has_kandi`) initialized outside
the loop. Once the variable assignment is made, a `break` statement is added in order to exit the
loop and avoid unnecessary loop iterations (a performance gain).

```python
headers = elec_vehicles[0] # column headers

has_kandi = False
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('automaker')].lower() == 'kandi technologies group':
        has_kandi = True
        break # exit loop
```

:bulb: `vehicle[headers.index('automaker')]` resolves to `vehicle[0]`.

## Challenge 01

__Task__: implement a `for` loop that includes a statement block that confirms if any vehicles in the
`elec_vehicles` list are capable of (re)charging their batteries within a three (3.0) hour period.

1. Setup
   1. Create a variable named `quick_charge` and assign it a float value of `3.0`.
   2. Create a second variable named `can_quick_charge` and assign it a value of `False`.

2. Inside the `for` loop write a conditional statement that confirms if _any_ of the vehicles in
   the `elec_vehicles` list can (re)charge their batteries in less than or equal to three (`3.0`)
   hours.

3. If such a vehicle is located assign `True` to `quick_charge` and then exit the loop
   _immediately_.

```python
fast_charge = 3.0 # battery charge (hours)
can_fast_charge = False

# TODO Implement loop
```

## 1.2 `continue` statement

The `continue` statement is employed in a `for` loop to end the current iteration and proceed
directly to the next iteration in the loop (if any), skipping any trailing statements.

In the example below, the goal is to return a list of electric vehicles that represent "outliers" in
terms of city driving battery range. If a vehicle's range is between 75 miles and 275 miles
(exclusive) the `continue` statement is executed and the trailing `list.append()` operation is
skipped. Only vehicles with a city range that falls on either side of the 75 - 275 mile range is
added to the `outliers` list.

:bulb: Use comparison operators arranged as `x < y < z` or `x <= y <= z` to test if a value
(typically a number but also a letter) is _between_ two values. The expression returns either
`True` or `False`.

```python
outliers = []
for vehicle in elec_vehicles[1:]:
    city_range = vehicle[headers.index('range_city')]
    if 75.0 < city_range < 275.0:
        continue # proceed to next iteration (skip)
    outliers.append(vehicle)
```

## Challenge 02

__Task__: given a tuple named `us_automakers` that contains the names of three US automakers, write a `for`
loop that includes a statement block that assigns Asian and European automakers' vehicles in the
`elec_vehicles` list to an empty list named `non_us_vehicles`.

1. Setup: note the following variable assignments:

   ```python
   us_automakers = ('ford motor company', 'general motors co.', 'tesla, inc.') # tuple
   non_us_vehicles = []
   ```

2. Inside the `for` loop write a conditional statement that checks whether or not each vehicle's
   _manufacturer_ is a listed in `us_automakers` . If `True` ignore the vehicle and
   check the next vehicle. If the conditional statement returns `False` assign the vehicle to the
   `non_us_vehicles` list.

   :bulb: utilize the membership operator `in` to check whether or not a vehicle's manufacturer is included in the `us_automakers` tuple.

```python
us_automakers = ('ford motor company', 'general motors co.', 'tesla, inc.') # tuple
non_us_vehicles = []

# TODO Implement loop
```

## 3.0 Indefinite iteration: the `while` loop

The `while` loop repeats a set of one or more statements _indefinitely_; that is, until a condition
is imposed that evaluates to `False` and terminates the loop.

```commandline
while < expression >:
    < statement A >
    < statement B >
```

In the example below, a counter `i` is initialized with a default value of zero (`0`). The `while`
loop, once initiated, will continue to iterate over the loop block _indefinitely_ until the
expression `i < 5` returns `False`. Note that the only way to terminate the looping operation is
to increment the counter value by `1` _inside the loop block.

```python
i = 0
while i < 5:
    print(i)
    i += 1 # increment (addition assignment operator)
```

## 3.1 Infinite loops

If a `while` loop is implemented incorrectly it will trigger an _infinite loop_, a runaway process
that, over time, will consume ever greater memory resources to the detriment of your both your
operatings system and hardware (you will hear the fans kick on as the laptop's internal
temperature rises). Eventually, your system will crash unless you kill the process.

Typically, a `while` loop is implemented when the number of required iterations is unknown. There
are other use cases, one of which we will explore below.

The following example is guaranteed to trigger an infinite loop since the `while` condition remains
`True` indefinitely:

```python
while True:
    print("infinite loop triggered") # Don't do this
```

You can tame a `while` loop condition initialized to `True` by adding a conditional statement that
includes a `break` statement in the loop code block.

```python
i = 0
while True:
    print('infinite loop triggered')
    if i == 5:
        print('infinite loop terminated\n')
        break # exit the loop
    i += 1 # increment (note indention)
```

:exclamation: if you trigger an infinite loop while running your module in VS Code click the
terminal pane's trash can icon in order to kill the session and end the runaway process.

## 3.2 `while` loop `else` condition

The `while` loop includes a built-in `else` condition that you can use to execute one or more
statements after the loop terminates.

```python
i = 0
while i < 5:
    print('I want an EV.')
    i += 1 # increment
else:
    print('Enough said. We believe you.')
```

## 3.3 `while` loop and conditional statements

You can employ conditional statements inside a `while` loop in order to determine the control flow
of each iteration. In the following example the modulus (`%`) operator is used to identify even and
odd numbers between 0 and 10.

:bulb: use the modulus operator to return the remainder after one number is divided by another. If
the remainder equals zero the number evaluated is an even number.

```python
i = 0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i += 1 # increment

i = 10
while i >= 0:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i -= 1 # decrement
```

## 3.4 `while` loop and `range`

You can employ a `while` loop in conjunction with the `range` type to loop over a sequence of numbers. In the example below the `while` loop iterates
over the sequence `0, 2, 4, 6, 8` provided by `range(0, 10, 2)`.

:exclamation: note that `i` is incremented by 2 not 1.

```python
i = 0
while i in range(0, 10, 2):
    print(f"{i} is an even number.")
    i += 2 # increment by 2
```

## 3.5 `while` loop and the built-in `input()` function

The built-in `input()` function accepts user-supplied strings from the command prompt. It is often
positioned inside a `while` loop in order to process user input. The pattern is illustrated in the
following example.

```python
ev_automakers = (
    'audi',
    'bmw',
    'ford',
    'gm',
    'yyundai',
    'kandi',
    'kia',
    'jaguar',
    'nissan',
    'tesla',
    'volkswagen',
    'volvo'
    )

while True:
    automaker = input('\nName your favorite EV automaker: ')
    if automaker.lower() in ev_automakers:
        print(f"\nThanks for selecting {automaker}.\n\nFinis.")
        break # terminate loop

    # print() can accept a comma-delimited set of strings
    print(
        f"\n'{automaker}' is not listed among the EV manufacturers.",
        f"Please check spelling and enter again or provide a different automaker."
        )
```

## Challenges 03 - 05

The following data set was sourced from the [National Renewable Energy Laboratory](https://www.nrel.gov/)
(NREL) [Alternative Fuel Stations](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/)
API. The API can be used to retrieve information on biodiesel, compressed natural gas, ethanol,
electric charging, hydrogen, liquefied natural gas, and propane station locations in the US.

The data covers all electric charging stations located in Ann Arbor, MI. The `data` list comprise
nested lists of charging station locations. Each nested list represents a modest subset of the
information otherwise collected by the NREL. Each nested charging station list includes the
following elements described in the "header" element:

* station name
* street address
* ev connector types (1 or more)
* ev network

```python
data = [
    ['station_name', 'street_address', 'ev_connector_types', 'ev_network'],
    ['Ann Arbor Downtown Development Authority - Library Parking Structure', '319 S Fifth Ave', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', '120 W Ann St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', '121 Catherine St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Forrest Parking Structure', '650 Forrest St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Maynard Parking Structure', '316 Maynard St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - William Street Parking Structure', '115 William St', 'J1772', 'Non-Networked'],
    ['U-M ANN ARBOR ANN STREET #2', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR ICL EDU #1', '1000 Greene St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALGREEN #1', '1300 Murfin Ave', 'J1772', 'ChargePoint Network'],
    ['BMW ANN ARBOR STATION 01', '501 Auto Mall Dr', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALL STREET #2', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["DOMINO'S FARMS DOMINO'S FARMS2", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', '215 W Washington', 'J1772', 'Non-Networked'],
    ['MEADOWLARK BLDG STATION 2', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['Shell', '2991 S State St', 'CHADEMO, J1772COMBO', 'eVgo Network'],
    ['Meijer - Tesla Supercharger', '3145 Ann Arbor-Saline Rd', 'TESLA', 'Tesla'],
    ['Sheraton Ann Arbor Hotel - Tesla Destination', '3200 Boardwalk Dr', 'J1772, TESLA', 'Tesla Destination'],
    ['MEIJER STORES 064 SALINE RD 1', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC STATION 2', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['FLEET SERVICES CITY HALL STA 4', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['173 - Ann Arbor', '5645 Jackson Road', 'CHADEMO, J1772COMBO', 'Greenlots'],
    ['Car & Driver - Tesla Destination', '1585 Eisenhower Place', 'TESLA', 'Tesla Destination'],
    ['U-M ANN ARBOR ANN STREET #1', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR ANN STREET #3', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALL STREET #1', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["DOMINO'S FARMS DOMINO'S FARMS", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['MEADOWLARK BLDG STATION 1', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['MEIJER STORES 064 SALINE RD 2', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC STATION 1', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['FLEET SERVICES POLICE SPACE #5', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['BEEKMAN BEEKMAN ST1', '1200 Broadway St', 'J1772', 'ChargePoint Network']
  ]
```

For example, if one chose to employ a `while` loop instead of a `for` loop in order to return a
count of ChangePoint Network EV charging stations it could be written as follows:

```python
chargepoint_count = 0
i = 0
while i < len(data[1:]):
    if data[i][-1] == 'ChargePoint Network':
        chargepoint_count += 1
    i += 1 # increment
```

## Challenge 03

__Task__: Implement a `while i in range()` loop and return a count of U-M EV charging
stations in the `data` list.

1. Ignore the "header row" in `data` and access _only_ the charging stations in `data`
   using slicing. Assign the slice to a variable named `charging_stations`.

2. Employing a `while` loop in conjunction with `range` and an `if` statement, loop over
   `charging_stations`, return a count of U-M EV charging stations to access the list data.
   Accumulate the count to the variable named `um_count`.

   :exclamation: be sure to increment your loop variable `i` by one (`1`) as you iterate over the
   list.

```python
charging_stations = None # TODO Access charging stations
um_count = None # TODO Initialize
i = None # TODO Initialize

# TODO Implement loop
```

## Challenge 04

__Task__: Certain station names in the `charging_stations` list contain an uppercase 'ANN ARBOR'
substring. Convert the uppercase substring to a mixed case 'Ann Arbor' substring. This "cleaning"
task will regularize case usage across the charging station names.

1. Employ a `while` loop and an `if` statement to convert the 'ANN ARBOR' station name substrings
   to mixed case. Replace the "station_name" element with the new `str` value.

  :exclamation: Limit the number of `while` loop iterations to the length of the `charging_stations`
  list; increment the counter `i` inside the loop and use it to access each charging station in the
  list. This will also prevent generating an infinite loop.

```python
i = None # TODO Initialize

# TODO Implement loop
```

## Challenge 05

__Task__: The "ev_connector_types" value is, in certain cases, a list masquerading as a string (e.g., `'CHADEMO, J1772COMBO'`). Convert this value to a list for all
charging stations in the `charging_stations` list.

1. Extract the "headers" element from `data` and assign to a variable named `headers.`

2. Employ a `while` loop to convert each charging station "ev_connector_type" string to a list
   (e.g., `'CHADEMO, J1772COMBO'` to a list `['CHADEMO', 'J1772COMBO']`. Replace the
   "ev_connector_types" element with the new `list` value.

   :exclamation: Limit the number of `while` loop iterations to the length of the
   `charging_stations` list; increment the counter `i` inside the loop and use it to access each
   charging station in the list. This will also prevent generating an infinite loop.

3. When using subscript notation chaining to perform the assignment, look up each charging
   station's"ev_connector_type" value using `headers.index(< header >)` rather than hard-coding the
   index value.

```python
headers = None # TODO Access "headers" element
i = None # TODO Initialize

# TODO Implement loop
```
