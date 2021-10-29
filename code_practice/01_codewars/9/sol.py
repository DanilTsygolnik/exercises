"""
Return negative

== Instructions ==

You are given a number and have to make it negative.
The number may be already negative.

Examples:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0

---
https://www.codewars.com/kata/55685cd7ad70877c23000102/
"""
def make_negative(num):
    if not isinstance(num, (int, float)):
        raise TypeError
    if num > 0:
        return -num
    return num
