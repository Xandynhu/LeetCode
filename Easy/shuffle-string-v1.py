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
# crate an empty string to generates the output value
# search for the i indice in indices
# if finds, concatenate the output + the char of s on that position (output = output + s[indice of i in indices])
# do it again till complete to read indices array

def foo(s: str, indices: list) -> list:
    # creates a variable string to return
    output = ""

    # search for the i-th indice on indices (the value, not the position)
    for i in range(len(indices)):
        for j in range(len(indices)):

            # search for the i-th indice
            if i == indices[j]:
                output += s[j]
                j += len(indices)

    return output

# Tests:
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(foo(s, indices))