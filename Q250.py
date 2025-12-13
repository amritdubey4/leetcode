"""
LeetCode Q250: Count Univalue Subtrees
Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root) -> int:
        self.count = 0
        
        def is_unival(node):
            if not node:
                return True
            
            left_unival = is_unival(node.left)
            right_unival = is_unival(node.right)
            
            if left_unival and right_unival:
                if (not node.left or node.left.val == node.val) and \
                   (not node.right or node.right.val == node.val):
                    self.count += 1
                    return True
            
            return False
        
        is_unival(root)
        return self.count

