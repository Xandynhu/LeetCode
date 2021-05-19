# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer,
# return the minimum number of positive deci-binary numbers needed so that they sum up to n. 

# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

# Example 2:
# Input: n = "82734"
# Output: 8

# Complexity O(n)

# Solution general idea:
# the amout of times we need to add deci-binary numbers is equal to the highest digit
# search for the highest digit (stops when find 9)
# return the highest digit

def foo(num: str) -> int:
    # varible to keep the highest digit
    highest = "0"

    for i in num:
        if highest < i:
            highest = i
        if i == "9":
            break
    
    return int(highest)





# tests
print(foo("82734"))
