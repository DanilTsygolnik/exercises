"""
Make a function that will return a greeting statement that uses an input.
The program should return the exact string: "Hello, <name> how are you doing today?".

---
https://www.codewars.com/kata/55a70521798b14d4750000a4/
"""
def greet(name: str):
    return "".join(["Hello, ", name, " how are you doing today?"])


# ---- python 3.6 and newer: f-strings ----
def greet_opt_1(name: str):
    return f"Hello, {name} how are you doing today?"

# ---- .format() method ----
def greet_opt_2(name: str):
    return "Hello, {} how are you doing today?".format(name)

def greet_opt_3(name: str):
    return "Hello, %s how are you doing today?" % name
