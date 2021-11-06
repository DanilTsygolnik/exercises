"""
Given a year, return the century it is in.

Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
---
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/
"""
def century(year):
    return year//100 + 1 - 0**(year%100)
