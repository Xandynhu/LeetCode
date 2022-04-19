# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution general idea
# defines a local recursive function to update a dictionary with the most local maximum sum
# search in this dictionary for the value on the highest key

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        hsh = {}
        def get_level(root, level = 0):
            if root == None:
                return

            # update the level-key with the new num total (what it cointained before + now)
            print("\n1: ", hsh)
            if root.left == None and root.right == None:
                hsh[level] = hsh.get(level, 0) + root.val

            # do it for all nodes
            print("3: ", hsh)
            get_level(root.left, level + 1)
            get_level(root.right, level + 1)

        get_level(root)
        level_key = 0
        level_value = 0

        # search for the value of the highest key
        for (key, value) in hsh.items():
            if key > level_key:
                level_value = value
                level_key = key

        return level_value






# tests
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(15)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(10)

print(Solution().deepestLeavesSum(root))
