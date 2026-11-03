# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        ptr1  = head
        while ptr1:
            ptr2 = ptr1
            while ptr2.next and ptr2.val == ptr2.next.val:
                ptr2 = ptr2.next
            if ptr1 != ptr2:
                prev.next = ptr2.next
            else:
                prev = ptr2
            ptr1 = ptr2.next
        return dummy.next
