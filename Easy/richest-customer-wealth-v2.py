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
# use python strings facilities to solve the problem...
# creates an empty list to keep the wealth of each customer
# in a loop calculates the sum of all elements of all customer and keeps it in that empty list
# return the maximum value that we have in our created list

def foo(input):
    # create an empty list
    result = []

    # for each customer, calculates and keeps his wealth
    for i in accounts:
        
        # keeps the customer total wealth
        # i is the customer, it could be represented as accounts[i] as well if the loop ware 'in range(accounts)'
        result.append(sum(i))
    
    # returns the maximum value in the result list
    return max(result)





# Tests:
accounts = [[1, 5], [7, 3], [3, 5]]
print(accounts)
print(foo(accounts))