# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# You have n boxes.
# You are given a binary string boxes of length n, where boxes[i] is '0' if the i-th box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the i-th box.

# Each answer[i] is calculated considering the initial state of the boxes.

# Example 1:
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation:  The answer for each box is as follows:
#               1) First box: you will have to move one ball from the second box to the first box in one operation.
#               2) Second box: you will have to move one ball from the first box to the second box in one operation.
#               3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

# Example 2:
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]

# Complexity O(n)

# Solution general idea:
# we count how many times "1" occurs on the given string and keep its indices
# the first box will need (sum of all indices)operations to get all "1"s ... (OBS: even if first pos == "1", its indice is 0, so doesnt count)
# then we create flags to count how many "1"s we have on the left and on the right
# for the next box,     each "1" on the left  will need +1 operation
#                   and each "1" on the right will need -1 operation
# then the total of operations for this box will be (same as before + ones on the left - ones on the right


# Idea Explanation:

# let ans be our list of same size as the given string which contains our answer
# for the first box we siply sum all indices where "1" occurs, ans[0] = sum(indices where 1 occurs)

# so, beeing
# ones_r = number of "1" on the right of boxes[i], and  (when i==0, starts in how many "1" we have after the first box)
# ones_l = number of "1" on the left of boxes[i]        (when i==0, starts in 0 -> we dont have any boz on the left)

# then the answer of how many operations we need for the box i is the same as we needed before,
# ans[i] = ans[i-1]

# + ones_l, because on the left box, each other box which have 1's will need 1 more operation (+1 operation for each one of all ones_l = +ones_l)
# ans[i] = ans[i-1] + ones_l

# - ones_r, because on the right box, each other box which have 1's will need 1 less operation (-1 operation for each one of all ones_r = -ones_r)
# ans[i] = ans[i-1] - ones_r + ones_l



# if we pass by an "1" going from (i-1)-th to i-th, update ones_l and ones_r

def foo(boxes):
        # array with the indices where "1" appears
        ones_indices = []

        # list with the size of the given string to contains the answer
        ans = [0]*len(boxes)

        # build ones_indices
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones_indices.append(i)

        # number of boxes where occurs "1"
        ones_r = len(ones_indices)

        # number of boxes given
        n_boxes = len(boxes)

        # initialize a flag in 0 to count how many "1"'s we've already seen
        ones_l = 0
  
        # amount of operations for the first box
        ans[0] = sum(ones_indices)

        # if the first box has a ball, we passed by one "1"
        # so, subtracts 1 from the ones_r we still have to read
        # adds 1 on the flag that counts how many "1" we readed
        if boxes[0] == "1":
            ones_l += 1
            ones_r -= 1
        
        # for each other box, starting from 1
        for i in range(1, n_boxes):

            # apply the formula
            ans[i] = ans[i-1] + ones_l - ones_r

            # if we get a "1", update the flags
            if boxes[i] == "1":
                ones_l += 1
                ones_r -= 1
                

        return ans


# tests:
print(foo("001011"))