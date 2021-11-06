"""
Traffic light

== Instructions ==
You're writing code to control your town's traffic lights.
You need a function to handle each change from green, to yellow, to red, and then to green again.

The function that takes a string as an argument representing the current state of the light and...
... returns a string representing the state the light should change to.

For example, update_light('green') should return 'yellow'.
---
https://www.codewars.com/kata/58649884a1659ed6cb000072/
"""

def update_light(light):
    assert isinstance(light, type(""))
    signals = {
                "green":"yellow",
                "yellow":"red",
                "red":"green"
              }
    light = light.casefold()
    assert light in signals
    return signals[light]
