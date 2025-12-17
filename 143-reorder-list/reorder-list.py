# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        n = len(stack)
        curr = head

        for _ in range(n//2):
            last = stack.pop()
            tmp = curr.next
            curr.next = last
            last.next = tmp
            curr = tmp

        curr.next = None