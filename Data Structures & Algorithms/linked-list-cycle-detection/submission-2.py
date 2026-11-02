# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head
        while r and r.next:
            r = r.next.next
            l = l.next
            if l == r:
                return True
        return False