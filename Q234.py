"""
LeetCode Q234: Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True
        
        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev = None
        current = slow.next
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Compare
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True

