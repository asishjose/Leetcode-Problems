class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(index):
            prev = prev.next
            if prev is None:
                return

        new_node = Node(val)
        new_node.next = prev.next
        prev.next = new_node
        self.head = dummy.next


    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(index):
            prev = prev.next
            if prev is None:
                return
            
        if prev.next is None:
            return
        prev.next = prev.next.next
        self.head = dummy.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)