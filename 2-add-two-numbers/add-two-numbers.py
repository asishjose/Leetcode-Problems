# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        fd = ''
        while l1:
            fd+=(str(l1.val))
            l1 = l1.next
        sd = ''
        while l2:
            sd+=(str(l2.val))
            l2 = l2.next
        fd = fd[::-1]
        sd = sd[::-1]
        sum = int(fd) + int(sd)
        n = len(str(sum))
        head = ListNode(0)
        curr = head
        for _ in range(n):
            num = sum%10
            new_node = ListNode(num)
            curr.next = new_node
            curr = curr.next
            sum = sum//10
        return head.next