# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        #middle
        slow = fast = head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        #reverse
        curr = head2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        #merge
        curr = head
        ptr = head2
        while ptr:
            temp = curr.next
            next_ptr = ptr.next

            curr.next = ptr
            ptr.next = temp

            curr = temp
            ptr = next_ptr