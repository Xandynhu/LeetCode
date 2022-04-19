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

# Complexity O(n^2)

# Solution general idea:
# Use a base array to generate another array to return.
# For each element of the given array,
# sum all previous elements with it and put it on the "same spot" in the other array.

def foo (input):
    # define the output array list
    output = []

    # for each element in the given list, do:
    for i in range(len(input)):
        # create an auxiliary variable on each loop
        aux = 0

        # add all elements from the first till the i-th and put in the back of output array
        for j in range(i+1):
        # update aux value with the +next given array
            aux = aux + input[j]

        # add the new element on the output array
        output.append(aux)

    return output






# Tests:
input = [1, 2, 3, 4, 5]
print(input)
print(foo(input))