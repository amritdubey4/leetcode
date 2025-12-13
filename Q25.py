# LeetCode 25. Reverse Nodes in k-Group
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k(node, k):
            for _ in range(k):
                if not node:
                    return False
                node = node.next
            return True

        dummy = ListNode(0, head)
        prev = dummy
        while has_k(prev.next, k):
            tail = prev.next
            cur = tail.next
            for _ in range(k - 1):
                nxt = cur.next
                cur.next = prev.next
                prev.next = cur
                tail.next = nxt
                cur = nxt
            prev = tail
        return dummy.next
