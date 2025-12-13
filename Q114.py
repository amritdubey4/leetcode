"""
LeetCode Q114: Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node 
  in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root) -> None:
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store right subtree
        right = root.right
        
        # Move left subtree to right
        root.right = root.left
        root.left = None
        
        # Attach original right subtree to the end
        while root.right:
            root = root.right
        root.right = right

