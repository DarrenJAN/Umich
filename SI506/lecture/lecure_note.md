# SI 506 Lecture summary

## Lecture 1


## Lecture 2
Useful Unix shell commands


## Lecture 3
### Topics

1. Comments (single line, multiline)
2. Values (objects) and types
3. Variables (labels) and variable assignment
4. Built-in functions print(), type(), len()
5. Basic arithmetic operations (add, subtract, multiply, divide)

### Vocabulary

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Dictionary__. An associative array or a map, wherein each specified value is associated with or
  mapped to a defined key that is used to access the value.
* __Immutable__. Object state cannot be modified following creation. Strings and tuples are immutable.
* __Mutable__. Object state can be modified following creation. Lists are mutable.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed.
* __Tuple__. An ordered sequence that cannot be modified once it is created.


## Lecture 4
### Topics

1. Statements and expressions
2. Object behaviors (a gentle intro)
3. string formatting: f-string; `\n` newline escape sequence
4. In-class coding challenges

### Vocabulary

* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.lower()` and `str.strip()`.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.


## Lecture 5

### Topics

1. Sequences: strings and lists
2. Indexing
3. Slicing
4. String and list methods
5. Select `str` methods
6. Select `list` methods
7. String formatting

### Vocabulary

* __Concatenation__. Joining one object to another in order to create a new object. Joining two
  strings together (e.g., `greeting = 'Hello ' + 'SI 506'`) is an example of string concatenation.
* __Index__. Numeric position of an element or item contained in an ordered sequence. Python
  indexes are zero-based, i.e., the first element's index value is 0 not 1.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are
  examples of an iterable.
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed individually or in groups.
* __Slice__. A subset of a sequence. A slice is created using the subscript notation `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.