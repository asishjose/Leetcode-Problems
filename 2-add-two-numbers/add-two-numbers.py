# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = ListNode(0)
        curr = result
        carry = 0
        h1, h2 = l1, l2
        while h1.next or h2.next:
            if h1.next == None:
                h1.next = ListNode(0)
            if h2.next ==None:
                h2.next = ListNode(0)
            h1, h2 = h1.next, h2.next

        h1, h2 = l1, l2
        
        while h1 or h2 or carry:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            num = carry + val1 + val2

            carry = 1 if num > 9 else 0

            num = num%10
            new_node = ListNode(num)
            curr.next = new_node
            curr = curr.next
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next

        return result.next
