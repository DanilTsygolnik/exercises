"""
Twice as old

---

== Instructions ==

Your function takes two arguments:

    current father's age (years)
    current age of his son (years)

Сalculate:how many years ago the father was twice as old as his son...
...or in how many years he will be twice as old.

---
https://www.codewars.com/kata/5b853229cfde412a470000d0/solutions/python
"""
def fiter(son, dad, cnt, grow):
    if dad//son==2 and dad%son==0:
        return cnt
    if grow:
        return fiter(son+1, dad+1, cnt+1, True)
    return fiter(son-1, dad-1, cnt+1, False)

def twice_as_old(dad_yo, son_yo):
    assert dad_yo!=son_yo

    if son_yo == 0:
        return dad_yo
    if dad_yo - son_yo > son_yo:
        return fiter(son_yo, dad_yo, 0, True)
    return fiter(son_yo, dad_yo, 0, False)

def twice_as_old_bp(dad_years_old, son_years_old):
    """the best suggested solution"""
    return abs(dad_years_old - 2*son_years_old)
