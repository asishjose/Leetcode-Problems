# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None or head.next is None:
            return None
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        n = length - n
        if n == 0:
            return head.next
        
        curr = head
        for _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
