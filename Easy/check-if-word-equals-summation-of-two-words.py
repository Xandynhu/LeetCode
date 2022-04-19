# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
# You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

 
# Example 1:
# Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
# Output: true
# Explanation:  The numerical value of firstWord is "acb" -> "021" -> 21.
#               The numerical value of secondWord is "cba" -> "210" -> 210.
#               The numerical value of targetWord is "cdb" -> "231" -> 231.
#               We return true because 21 + 210 == 231.

# Example 2:
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
# Output: false
# Explanation:  The numerical value of firstWord is "aaa" -> "000" -> 0.
#               The numerical value of secondWord is "a" -> "0" -> 0.
#               The numerical value of targetWord is "aab" -> "001" -> 1.
#               We return false because 0 + 0 != 1.

# Complexity O(n)

# Solution general idea:
# calculates the 3 values and compare if n1 + n2 == ntarget

def foo(firstWord: str, secondWord: str, targetWord: str) -> bool:
    
    # uses ord("char") to get its ascii value
    # - 97 because it is the value of "a", the first letter

    # generates all 3 numbers in str format
    n1 = ""
    for char in firstWord:
        n1 = n1 + str(ord(char) - 97)

    n2 = ""
    for char in secondWord:
        n2 = n2 + str(ord(char) - 97)
    
    nt = ""
    for char in targetWord:
        nt = nt + str(ord(char) - 97)

    # turns all numbs in int and compare
    if int(n1) + int(n2) == int(nt):
        return True
    return False



# tests
print(foo("acb", "cba", "cdb"))