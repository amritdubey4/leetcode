"""
LeetCode Q148: Sort List
Given the head of a linked list, return the list after sorting it in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Split list into two halves
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        current.next = left or right
        
        return dummy.next

