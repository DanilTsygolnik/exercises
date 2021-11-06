"""
Convert a string to an array

---

== Instructions ==
Write a function to split a string and convert it into an array of words.

"""
def string_to_array(inp_str):
    if inp_str == "":
        return [inp_str]
    return inp_str.split()

def string_to_array_bp(string):
    return string.split(" ")
