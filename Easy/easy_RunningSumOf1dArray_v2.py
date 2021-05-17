# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given an array list of integers, returns a same lenght array where:
# the i-th element is the sum of all firsts i elements of the given array

# exemple 1:
# input = [1, 2, 3, 4]
# ouptut = [1, 3, 6, 10]
# explanation = [1, 1+2, 1+2+3, 1+2+3+4]

# exemple 2:
# input = [1, 1, 1, 1]
# output = [1, 2, 3, 4]
# explanation = [1, 1+1, 1+1+1, 1+1+1+1]

# Complexity O(n)

# Solution general idea:
# Use the base array to update it and return.
# For the given array update the i-th element with the sum of the i-th and its previous element.

def foo(input):
    # for each element but the first...
    # (the first element doesnt have a previous value, therefore it doesnt need to be added to anything)
    for i in range(1, len(input)):
        # updates the i-th element adding itself with the previous element
        input[i] = input[i] + input[i-1]

    return input






# Tests:
input = [1, 2, 3, 4, 5]
print(input)
print(foo(input))