"""
LeetCode Q138: Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point 
to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node 
has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes 
should point to new nodes in the copied list such that the pointers in the original list and copied list represent 
the same list state. None of the pointers in the new list should point to nodes in the original list.
"""

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # Create mapping of original to copy
        mapping = {}
        current = head
        
        # First pass: create all nodes
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # Second pass: set next and random pointers
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next
        
        return mapping[head]

