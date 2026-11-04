# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        ## total length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        multiple_k = True if length%k == 0 else False

        ## Splitting
        heads = []
        next_head = head
        while next_head:
            heads.append(next_head)
            curr = next_head
            count = 1
            while curr.next and count < k:
                curr = curr.next
                count+=1
            next_head = curr.next
            curr.next = None

        ## Reveresing
        n = len(heads) if multiple_k else len(heads)-1
        reversed_heads = []
        for h in range(n):
            curr = heads[h]
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            reversed_heads.append(prev)
        if not multiple_k:
            reversed_heads.append(heads[n])

        ## Joining
        dummy = ListNode(0)
        dummy.next = reversed_heads[0]
        for i in range(len(reversed_heads)-1):
            curr = reversed_heads[i]
            while curr.next:
                curr = curr.next
            curr.next = reversed_heads[i+1]
            i+=1
        return dummy.next