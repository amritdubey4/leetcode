"""
LeetCode Q113: Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum 
of the node values in the path equals targetSum. Each path should be returned as a list of the node values, 
not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            
            path.append(node.val)
            
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            
            path.pop()
        
        dfs(root, targetSum, [])
        return result

