# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head

        length = 1
        curr = head
        while curr.next:
            length+=1
            curr = curr.next
        k = k % length 
        k = length - k       
        curr.next = head

        curr = head
        print(k)
        for _ in range(k-1):
            curr = curr.next
        head = curr.next
        curr.next = None
        
        return head