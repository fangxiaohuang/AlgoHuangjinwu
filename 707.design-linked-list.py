#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = Node(-1)
        self.len = 0
        

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        p = self.head
        for _ in range(index+1):
            p = p.next
        return p.val
        

    def addAtHead(self, val: int) -> None:
        self.len += 1
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        

    def addAtTail(self, val: int) -> None:
        p = self.head
        for i in range(self.len):
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
        self.len += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        elif index < 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            self.len += 1
            p = self.head
            for i in range(index):
                p = p.next
            node.next = p.next
            p.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.len:
            return
        p = self.head
        for i in range(index-1):
            p = p.next
        p.next = p.next.next if p.next else None
        self.len -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

