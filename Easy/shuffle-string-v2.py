# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

# exemple 1:
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation:  "codeleet" becomes "leetcode" after shuffling.

# example 2:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

# Complexity O(n^2)

# Solution general idea:
# create a aux list with the same size as the given one
# overwrite all elements of this aux list with the right letter
# the right spot for the s[i] letter is the spot indicated by the i-th value in indices (indices[i])
# output[spot indicated by the value at indices[i]] = s[i]

def foo(s: str, indices: list) -> list:
    # variable to return
    # same size as indices
    output = list(s)

    # for each position, from 0 till end of s|indices
    for i in range(len(s)):
        # overwrite the output list with s[i]
        # at the indice indicated by the i-th element of indices
        output[indices[i]] = s[i]
    
    return "".join(output)

# Tests:
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(foo(s, indices))
