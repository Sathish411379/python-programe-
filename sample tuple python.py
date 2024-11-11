# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:20:36 2024

@author: SATHISH S
"""

1. Creating and Accessing Tuples
““
““
# Creating a tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Accessing elements
print("First element of Tuple 1:", tuple1[0])
print("Last element of Tuple 2:", tuple2[-1])
2. Tuple with Single Element
To create a tuple with one element, add a comma after the element; otherwise, ““ will interpret it as a regular value.

““
““
single_element_tuple = (10,)  # Note the comma
not_a_tuple = (10)

print("Single element tuple:", single_element_tuple)
print("Not a tuple:", not_a_tuple)  # This is an integer
3. Unpacking Tuples
Tuples can be unpacked into individual variables.

““
““
# Unpacking a tuple
coordinates = (10, 20, 30)
x, y, z = coordinates
print("X:", x, "Y:", y, "Z:", z)

# Partial unpacking with *
a, *b = coordinates
print("A:", a, "B:", b)
4. Concatenating and Repeating Tuples
““
““
# Concatenating tuples
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
print("Concatenated tuple:", concatenated_tuple)

# Repeating tuples
repeated_tuple = tuple_a * 3
print("Repeated tuple:", repeated_tuple)
5. Checking for Elements in a Tuple
““
““
fruits = ("apple", "banana", "cherry")
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'grape' in fruits?", "grape" in fruits)
6. Finding the Length, Maximum, and Minimum of a Tuple
““
““
numbers = (10, 20, 30, 40, 50)

# Finding length
print("Length of numbers:", len(numbers))

# Finding maximum and minimum values
print("Maximum in numbers:", max(numbers))
print("Minimum in numbers:", min(numbers))
7. Count and Index Methods
““
““
tuple_c = (1, 2, 2, 3, 4, 5, 2)

# Counting occurrences of an element
print("Count of 2 in tuple_c:", tuple_c.count(2))

# Finding the first index of an element
print("Index of first 2 in tuple_c:", tuple_c.index(2))
8. Converting a Tuple to a List and Back
““
““
# Tuple to list
tuple_d = (100, 200, 300)
list_d = list(tuple_d)
print("List converted from tuple:", list_d)

# Modifying the list and converting back to tuple
list_d.append(400)
tuple_d_modified = tuple(list_d)
print("Modified tuple:", tuple_d_modified)
9. Nested Tuples
Tuples can contain other tuples, creating a nested structure.

““
““
nested_tuple = (1, 2, (3, 4), (5, 6, 7))
print("Nested tuple:", nested_tuple)

# Accessing elements in a nested tuple
print("Element at index 2:", nested_tuple[2])
print("Element at index 2,1:", nested_tuple[2][1])  # Accessing 4 in (3, 4)
10. Tuple Slicing
““
““
tuple_e = (0, 1, 2, 3, 4, 5, 6, 7)

# Slicing
print("Elements from index 2 to 5:", tuple_e[2:6])
print("Elements from start to 4:", tuple_e[:5])
print("Elements from 4 to end:", tuple_e[4:])
11. Using Tuples as Dictionary Keys
Since tuples are immutable, they can be used as keys in dictionaries.

““
““
# Dictionary with tuple keys
coordinates_dict = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}

print("Coordinates dictionary:", coordinates_dict)
print("Value at (1, 2):", coordinates_dict[(1, 2)])
12. Using Tuples in Functions
Tuples are useful for returning multiple values from a function.

““
““
# Function returning multiple values as a tuple
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

stats = get_stats([1, 2, 3, 4, 5])
print("Min, Max, and Average:", stats)

# Unpacking returned tuple
min_val, max_val, avg_val = get_stats([1, 2, 3, 4, 5])
print("Min:", min_val, "Max:", max_val, "Average:", avg_val)
13. Comparing Tuples
Tuples can be compared lexicographically, meaning they are compared element by element.

““
““
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print("Is tuple1 < tuple2?", tuple1 < tuple2)  # True, because 3 < 4
print("Is tuple1 == tuple2?", tuple1 == tuple2)
14. Zipping Tuples
You can combine two lists or tuples into a single iterable of pairs using zip.

““
““
names = ("Alice", "Bob", "Charlie")
scores = (85, 92, 78)

# Zipping tuples together
zipped = tuple(zip(names, scores))
print("Zipped tuples:", zipped)

# Unzipping
unzipped_names, unzipped_scores = zip(*zipped)
print("Names:", unzipped_names)
print("Scores:", unzipped_scores)
