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

# Complexity O(n^2)

# Solution general idea:
# to move all n balls from box i to box j, we need abs(i - j) * n operations
# for each box (position on the given string, be i this position)
# calculate the sum of all (abs(i - j) * n), beeing j another position running all string positions

# considering we get only binary strings
# an optimized idea is to just add abs(i - j) when i contains "1", do nothing when "0" (nothing to move)

def foo(boxes: str) -> list:

    # define an empty array to return
    output = []

    # define the quantity of loops
    end = len(boxes)

    # for all positions in boxes
    for i in range(end):

        # define a variable to count how many operations we need to do
        operations = 0

        # for all other positions
        for j in range(end):
            if boxes[j] == "1":
                operations += abs(i - j)
        
        output.append(operations)

    return output






# tests:
boxes = "001011"
print(len(boxes))
print(foo("001011"))