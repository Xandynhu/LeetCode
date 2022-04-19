# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given an m x n integer grid like accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank,
# returns the wealth of that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the highest wealth.

# exemple 1:
# input = [[1, 2, 3], [3, 2, 1]]
# output = 6
# explanation:  1st cutomer has wealth = 1 + 2 + 3 = 6
#               2st cutomer has wealth = 1 + 2 + 3 = 6
#               both customers are considered the richest with a wealth of 6, so return 6.

# exemple 2:
# input = [[1, 5], [7, 3], [3, 5]]
# output = 10
# explanation:  1st customer has wealth = 6
#               2nd customer has wealth = 10
#               3rd customer has wealth = 8
#               the 2nd customer is the richest with a wealth of 10.

# Complexity O(i*j)

# Solution general idea:
# creates a variable to keep the highest wealth found so far, initialized in 0
# for each i customer sum all values in their j bank accounts
# compare the sum with the highest wealth at the moment
# if it is higher than the highest, update with the new value

def foo(input):
    # creates a variable to keep the highest wealth found so far
    max = 0

    # for each customer, do:
    for i in range(len(input)):
        # creates a variable to keep the wealth of the current customer beeing calculated
        current = 0

        # sum all his wealth
        for j in range(len(input[i])):
            current += input[i][j]
        
        # if current wealth it bigger than the max, update max
        if current > max:
            max = current
    
    return max





# Tests:
accounts = [[1, 5], [7, 3], [3, 5]]
print(accounts)
print(foo(accounts))