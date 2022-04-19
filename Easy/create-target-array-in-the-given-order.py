# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#       Initially target array is empty.
#       From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#       Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# Example 1:
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
#       nums       index     target
#       0            0        [0]
#       1            1        [0,1]
#       2            2        [0,1,2]
#       3            2        [0,1,3,2]
#       4            1        [0,4,1,3,2]

# Example 2:
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
#       nums       index     target
#       1            0        [1]
#       2            1        [1,2]
#       3            2        [1,2,3]
#       4            3        [1,2,3,4]
#       0            0        [0,1,2,3,4]

# Complexity O(n)

# Solution general idea
# for each i-th element in nums, put it on the position given by the value in the i-th index element

def foo(nums: list[int], index: list[int]) -> list[int]:
    output = []

    for i in range(len(nums)):
        output.insert(index[i], nums[i])
    
    return output





# tests
print(foo([0,1,2,3,4], [0,1,2,2,1]))