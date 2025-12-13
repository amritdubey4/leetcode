"""
LeetCode Q92: Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        current = prev.next
        next_node = current.next
        
        for _ in range(right - left):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next
        
        return dummy.next

