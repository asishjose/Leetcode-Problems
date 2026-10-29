# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next


        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0)+1
        distinct = [num for num in nums if counts[num]==1]

        distinct.sort()
        head = ListNode(0)
        curr = head
        for i in range(len(distinct)):
            curr.next = ListNode(distinct[i])
            curr = curr.next
        return head.next