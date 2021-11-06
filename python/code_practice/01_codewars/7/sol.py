"""
Arrary plus array

---

== Instructions ==

There are 2 arrays containing only integer numbers.
Calculate the sum of all their elements. Return integer.

---
https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/
"""
def array_plus_array(arr1,arr2):
    def arr_check(arr):
        """Checking if input is correct"""
        assert isinstance(arr, type([]))
        for i in arr:
            assert isinstance(i, type(1))
    arr_check(arr1)
    arr_check(arr2)

   # best practice for this task
    return sum(arr1) + sum(arr2)
