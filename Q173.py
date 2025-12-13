"""
LeetCode Q173: Binary Search Tree Iterator
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part 
  of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a next number, otherwise returns false.
- int next() Moves the pointer to the right, then returns the next smallest number.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return 
the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the 
in-order traversal when next() is called.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_all_left(root)
    
    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_all_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

