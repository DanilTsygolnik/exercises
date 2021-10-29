"""
Arrary plus array

---

== Instructions ==

There are 2 arrays containing only integer numbers.
Calculate the sum of all their elements. Return integer.


"""
def arr_elem_sum(arr):
    assert isinstance(arr, type([]))
    elem_sum = 0
    for i in arr:
        assert isinstance(i, type(1))
        elem_sum += i
    return elem_sum

def array_plus_array(arr1,arr2):
    return arr_elem_sum(arr1) + arr_elem_sum(arr2)
