"""
Opposites Attract

---

== Instructions ==

Timmy & Sarah think they are in love.
Around where they live, they will only know once they pick a flower each.
They are in love if:
- one of the flowers has an even number of petals;
- the other has an odd number of petals.

Write a function that will take the number of petals of each flower...
...and return true if they are in love and false if they aren't.

---
https://www.codewars.com/kata/555086d53eac039a2a000083/solutions/python
"""

def lovefunc(flower1, flower2):
    assert type(flower1)==type(1)
    assert type(flower2)==type(1)

    if flower1%2+flower2%2==1:
        return True
    return False

def lovefunc_best_practice(flower1, flower2):
    return (flower1+flower2)%2
