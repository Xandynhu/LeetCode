# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# exemple 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# exemple 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Complexity O(n^2)

# Solution general idea:
# creates a variable initiated at 0 to count the amount of good pairs
# for each element in the given array, read all next elements
# if both elements are the same value, count++

def foo(nums):
    # creates a count variable initialized in 0
    count = 0

    # for each element in the given array, read all next elements
    for i in range(len(nums)):
        
        # starts the reading from the next element
        for j in range(i+1, len(nums)):

            # if both number are equal, count one
            if nums[i] == nums[j]:
                count += 1

    return count





# Tests:
nums = [1,2,3,1,1,3]
print(foo(nums))