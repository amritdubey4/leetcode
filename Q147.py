"""
LeetCode Q147: Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs 
   within the sorted list, and inserts it there.
3. It repeats until no input elements remain.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        last_sorted = head
        
        while current:
            if current.val >= last_sorted.val:
                last_sorted = current
                current = current.next
            else:
                last_sorted.next = current.next
                prev = dummy
                while prev.next.val < current.val:
                    prev = prev.next
                current.next = prev.next
                prev.next = current
                current = last_sorted.next
        
        return dummy.next

