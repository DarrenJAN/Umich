
# SI 506: Problem Set 1

## This week's Problem Set

This week's problem includes six (6) problems that focus on comments, using built-in functions, and basic list and string operations.

:bulb: In order to check your work, try using the built-in function `print()` to print out the results.

## Background

This week's problem set is based around restaurants in Ann Arbor. Ann Arbor is home to a diverse range of tantalising restaurants and eateries and this problem set features some of Central Campus' popular spots.

## 1.0 Problem 1 (15 Points)

1. You have been provided with six lines of code that attempt to assign a string with a restaurant's name to a variable. Only three of these lines contain valid variable assignments. Uncomment the statements that contain valid variable assignments.

2. Create a new variable called `cottage_inn` and assign to it a string respresentation of the restaurant **Cottage Inn Pizza**.

3. Similarly, create a new variable called `madras_masala` and assign to it a string respresentation of the restaurant **Madras Masala**.

## 2.0 Problem 2 (10 Points)

1. Create a `list` called `restaurants` that contains the **valid** variables from Problem 1.

2. Using the appropriate in-built `list` method, add the two new variables created in Problem 1 to `restaurants`.

    :exclamation: This problem will require two lines of code, one to add `cottage_inn` and another to add `madras_masala`.

    :bulb: After the above step, the `restaurants` list *must* contain the following elements:

    ```
    ['Frita Batidos', 'Hopcat', 'Fleetwood Diner', 'Cottage Inn', 'Madras Masala']
    ```

## 3.0 Problem 3 (20 Points)

1. Use the `str.join()` method on the `restaurants` list to create a new string called `all_restaurants` where each restaurant is separated by a comma (,).

2. To improve readability, we want to replace all commas (,) with a comma followed by a space (, ). Use the `str.replace()` method to perform this operation. Assign the new string to a variable called `all_restaurants_with_spaces`.

## 4.0 Problem 4 (20 Points)

1. Use **slicing** to reverse the elements in the list `restaurants` and assign it to a variable named `restaurants_reversed`.

2. Use **slicing** to return every **other** element in the list `restaurants_reversed`, starting with the first element. Assign this return value to a list named `every_other_restaurant`.

    :exclamation: Unlike in previous problems, this variable declaration has not been started for you. You must declare a variable called `every_other_restaurant` and assign the return value to this variable.

## 5.0 Problem 5 (20 Points)

Mr. Foodie visited each of the five restaurants in the `restaurants` list. The list `restaurant_checks` contains the total amount they spent at each of these restaurants.

:exclamation: The order of the numbers in this list correlate to the order of resturants in the `restaurants` list; i.e. the first number in the `restaurant_checks` list is the order total for the first restaurant in the `restaurants` list.

1. Mr. Foodie made an error while inputting the **third** value in the `restaurant_checks` list. The correct value is **9.56** instead of **8.86**. Use list **indexing** to update the list with the correct value.

2. What is the **maximum** value in `restaurant_checks`? Assign the maximum value to a variable named `max_check`.

    :bulb: Use the appropriate built-in function to return the max value in the list.

3. What is the maximum value's **index** in `restaurant_checks`? Assign the maximum value's index to a variable named `max_check_index`.

    :bulb: Use the appropriate list method to return the index value.

4. Which was the resturant where Mr. Foodie spent the most money? Use the `restaurants` list and `max_check_index` to assign the name of the restaurant to a variable named `max_check_restaurant`.

    :exclamation: Similar to 4.2, this variable declaration has not been started for you. You must declare a variable called `max_check_restaurant` and assign the appropriate value to this variable.

## Problem 6 (15 Points)

1. You have been given a *multiline* string named `extra_restaurants` containing the names of five (5) new restaurants, each on a new line. Use the appropriate string method to create a `list` named `new_restaurants`, where each element is one line of the multiline string.

2. Use `list` **concatenation** to add elements of `restaurants` and `new_restaurants`, in that order. Assign the new list to a variable named `final_restaurants`.