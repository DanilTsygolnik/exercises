"""
Reversed sequence

== Instructions ==

Build a function that returns an array of integers from n to 1 where n>0.

Example:
n=5 --> [5,4,3,2,1]
---
https://www.codewars.com/kata/5a00e05cc374cb34d100000d/
"""
def reverse_seq(n):
    def seq_iter(arr, cnt):
        if cnt > 0:
            arr.append(cnt)
            return seq_iter(arr, cnt-1)
        return arr
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError
    return seq_iter([],n)
