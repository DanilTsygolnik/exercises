"""
Correct the mistakes of the character recognition software

Character recognition software is widely used to digitise printed texts.
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised
character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text.
You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1

The test cases contain numbers only by mistake.

---
https://www.codewars.com/kata/577bd026df78c19bca0002c0
"""
def correct(str_inp):
    str_edited = []
    mistakes = {"5":"S", "0":"O", "1":"I"}
    for i in str_inp:
        if i in mistakes:
            str_edited.append(mistakes[i])
        else:
            str_edited.append(i)
    return "".join(str_edited)

# ---- str.maketrans() ----

def correct_suggested_1(string):
    tr=str.maketrans('015','OIS')
    return string.translate(tr)

# ---- str.replace() ----
def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')
