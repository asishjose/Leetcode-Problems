# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            curr1, curr2 = headA, headB
            while curr1 and curr2:
                curr1, curr2 = curr1.next, curr2.next
            if curr1:
                shorter = curr1
                longer = headA
                short = headB
            else:
                shorter = curr2
                longer = headB
                short = headA
            bal = 0
            while shorter:
                shorter = shorter.next
                bal += 1
            for _ in range(bal):
                longer = longer.next
            curr1 = longer
            curr2 = short
            while curr1 and curr2:
                if curr1 == curr2:
                    return curr1
                curr1, curr2 = curr1.next, curr2.next