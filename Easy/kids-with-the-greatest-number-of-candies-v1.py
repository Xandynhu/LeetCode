# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the i-th kid has.
# For each kid check:
# if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.

# exemple 1:
# input: candies = [2,3,5,1,3], extraCandies = 3
# output: [true,true,true,false,true] 
# explanation:  Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies (the greatest number of candies among the kids). 
#               Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
#               Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
#               Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
#               Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.

# example 2:
# input: candies = [4,2,1,1,2], extraCandies = 1
# output: [true,false,false,false,false] 
# explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.

# Complexity O(2n)

# Solution general idea:
# get the max element in the given list and subtracts extraCandies from it
# then every element higher or equal to this result can be the highest element
# one by one read each element of the given array and generate another array pushing back
# true if element >= result,
# false if otherwise

def foo(candies, extraCandies):
    # creates a variable to keep the higher element - extraCandies
    result = max(candies) - extraCandies

    # creates an empty array to return
    output = []

    # for each candie amount in candies, do
    for i in candies:
        if i >= result:
            output.append(True)
        else:
            output.append(False)
    
    return output





# Tests
candies = [2,3,5,1,3]
extraCandies = 3
print(foo(candies, extraCandies))