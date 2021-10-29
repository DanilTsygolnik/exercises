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
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError
    return list(range(1,n+1))[::-1]
