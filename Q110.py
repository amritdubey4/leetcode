"""
LeetCode Q110: Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the left and right subtrees of every node 
differ in height by no more than 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = get_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return get_height(root) != -1

