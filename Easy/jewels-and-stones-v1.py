# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# exemple 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# exemple 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

# Complexity O(n*m)
# n is how many characters are in jewels
# m is how many characters are in strones

# Solution general idea:
# creates an variable initialized in 0 to count and return
# for each letter in jewels, search for it in stones
# if finds one, add one in count

def foo(jewels, stones):
    # variable to count
    count = 0

    # search for each char in jewels an equal char in stones
    for i in jewels:
        for j in stones:
            if i == j:
                count += 1
    
    return count





# Tests
jewels = "aAc"
stones = "aAAbcbbAb"
print(foo(jewels, stones))