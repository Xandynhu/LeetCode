# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# exemple 1:
# input: nums = [2,5,1,3,4,7], n = 3
# output: [2,3,5,4,1,7] 
# explanation:  Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7
#               then the answer is [2,3,5,4,1,7].

# exemple 2:
# input: nums = [1,2,3,4,4,3,2,1], n = 4
# output: [1,4,2,3,3,2,4,1]

# Complexity O(n)

# Solution general idea:
# creates an empty array to return
# for each "i" in "n" in a loop, push in empty_array the first element of first half (i) and first element of second half (n+i)

from typing import List


def foo(nums: List, n: int):
    # creates an empty array
    output = []

    for i in range(n):
        output.append(nums[i])
        output.append(nums[n+i])
    
    return output





# Tests:
nums = [1,2,3,4,4,3,2,1]
n = 4
print(foo(nums, n))