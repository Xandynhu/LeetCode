# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.

# Example 1:
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

# Example 2:
# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]

# Complexity O(n)

# Solution general idea:
# we keep the first element on the first pos in the output array
# now, knowing that size of encoded is n and size of array is n+1, we have to find the next n elements to keep in array
# if    encoded[i] = arr[i] XOR arr[i + 1], 
# then  encoded[i] XOR arr[i] = arr[i + 1]. (the i+1-th element on arr is the following element added)
# find arr[i + 1] and keeps it on arr

def foo(encoded: list[int], first: int) -> list[int]:
    arr = [first]

    for i in encoded:
        arr.append(arr[-1] ^ i)
    
    return arr



# tests
print(foo([6,2,7,3], 4))