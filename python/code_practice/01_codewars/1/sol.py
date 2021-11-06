"""
Find the smallest integer in the array

---

== Instructions ==

Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

"""

def get_smallest_v1(array):
    assert type(array) == type([])
    assert array != []

    return sorted(array)[0]

def get_smallest_v2(array):
    assert type(array) == type([])
    assert array != []

    smallest = array[0]
    index = 1
    while index < len(array):
        if array[index] < smallest:
            smallest = array[index]
        index += 1
    return smallest

# best practice
def get_smallest_v1(array):
    return min(array)
