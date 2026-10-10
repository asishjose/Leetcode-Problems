# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head

        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        k = k % length
        
        for _ in range(k):
            curr = head
            while curr.next.next:
                curr = curr.next
            
            temp = curr.next
            curr.next = None
            new_node = temp
            new_node.next = head
            head = new_node
        return head