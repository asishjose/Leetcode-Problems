# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head
        curr  = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        curr.next = head
        k = count - (k%count)

        curr = head
        for _ in range(k-1):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head