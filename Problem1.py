
## Problem1 (https://leetcode.com/problems/path-sum-ii/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper(node, currSum, path, res):
            if node is None:
                return
            
            # Add the current node's value to the current sum and path
            currSum += node.val
            path.append(node.val)
            
            # If it's a leaf node and the current sum matches the target sum, add the path to the result
            if node.left is None and node.right is None:
                if currSum == targetSum:
                    res.append(path.copy())
            
            # Recur for left and right subtrees
            helper(node.left, currSum, path, res)
            helper(node.right, currSum, path, res)
            
            # Backtrack: remove the current node's value from the path
            path.pop()
        
        res = []
        helper(root, 0, [], res)
        return res