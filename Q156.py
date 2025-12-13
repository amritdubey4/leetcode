"""
LeetCode Q156: Binary Tree Upside Down
Given the root of a binary tree, turn the tree upside down and return the new root.
You can turn a binary tree upside down with the following steps:
1. The original left child becomes the new root.
2. The original root becomes the new right child.
3. The original right child becomes the new left child.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        
        return new_root

