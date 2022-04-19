# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.

# Example 1:
# Input: command = "G()()()()(al)"
# Output: "Gooooal"

# Example 2:
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"

# Complexity O(n)

# Solution general idea
# uses python features to replace substrings

def foo(command: str) -> str:
    command = command.replace("()", "o")
    command = command.replace("(al)", "al")

    return command




# tests
print(foo("G()()()()(al)"))