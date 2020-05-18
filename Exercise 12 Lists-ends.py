# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


import random


def lists_ends(list_item):
    return [list_item[0], list_item[len(list_item) - 1]]


num_list = [random.randrange(1, 99, 1) for i in range(5)]
print(num_list)
print(lists_ends(num_list))