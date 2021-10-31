"""
Convert number to a reversed array of digits.

Example:

348597 => [7,9,5,8,4,3]

---
https://www.codewars.com/kata/5583090cbe83f4fd8c000051/
"""
def digitize(n):
    templ = list(str(n))[::-1]
    return list(int(i) for i in templ)

# ---- map() ----

def digitize_opt_1(n):
    return map(int, str(n)[::-1])

# ---- new_str = src_str[::-1] & list(iterable) ----

def digitize_opt_2(n):
    return [int(x) for x in str(n)[::-1]]

