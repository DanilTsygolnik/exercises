"""


---

== Instructions ==

Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

"""
def count_sheeps(sheep):
    assert type(sheep)==type([])
    num_missing = 0
    for i in sheep:
        if i is True:
            num_missing += 1
    return num_missing

def count_sheeps(arrayOfSheeps):
    """best practice"""
    return arrayOfSheeps.count(True)
