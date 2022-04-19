# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:  For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
#               For nums[1]=1 does not exist any smaller number than it.
#               For nums[2]=2 there exist one smaller number than it (1). 
#               For nums[3]=2 there exist one smaller number than it (1). 
#               For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Complexity O(n^2)

# Solution general idea:
# for each element on the given array
# create a variable to count how many numbers are smaller
# and count it by running by the array again.

def foo(input: list):
    # create an empty array to return the result
    output = []

    # for each element in input, do
    for i in input:

        # creates a variable to count how many smallers are
        count = 0

        # compare to all array numbers,
        # if we find a number smaller than i, add 1 on count
        for j in input:
            if i > j:
                count += 1
        
        # add the count on the array
        output.append(count)
    
    return output





# Tests:
nums = [8,1,2,2,3]
print(foo(nums))