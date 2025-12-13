"""
LeetCode Q61: Rotate List
Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Calculate length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        # Find new tail
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Rotate
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head

