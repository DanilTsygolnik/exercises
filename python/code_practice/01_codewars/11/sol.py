"""
Third Angle of a Triangle

== Instructions ==

You are given two interior angles (in degrees) of a triangle.
Write a function to return the 3rd.

Note: only positive integers will be tested.
---
https://www.codewars.com/kata/5a023c426975981341000014/
"""
def other_angle(a, b):
    if not (a+b)<180:
        raise ValueError
    return 180-a-b
