# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
# example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
#           Product of digits = 2 * 3 * 4 = 24 
#           Sum of digits = 2 + 3 + 4 = 9 
#           Result = 24 - 9 = 15

# example 2:
# Input: n = 4421
# Output: 21
# Explanation: 
#           Product of digits = 4 * 4 * 2 * 1 = 32 
#           Sum of digits = 4 + 4 + 2 + 1 = 11 
#           Result = 32 - 11 = 21

# Complexity O(n)

# Solution general idea
# define 2 variables to keep the mul and sum totals
# transform the number from an integer to a string
# for each char, turn it back to integer to calculate what we want to

def foo(input):
    # variables to keep totals
    mul = 1
    sum = 0

    # integer to string
    str_input = str(input)

    for i in str_input:
        mul *= int(i)
        sum += int(i)
    
    return (mul - sum)




# Tests:
print(foo(81275387124))