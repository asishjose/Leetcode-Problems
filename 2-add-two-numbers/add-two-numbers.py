# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        def add(l1, l2, carry):
            if l1 is None and l2 is None and carry==0:
                return None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            node = ListNode(total%10)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            node.next = add(l1, l2, total//10)
            return node
        
        return add(l1, l2, 0)