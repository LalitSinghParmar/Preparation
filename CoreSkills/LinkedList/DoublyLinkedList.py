from typing import List


class Node:
    def __init__(self, val=0, next=None):
        '''
        Initialize a node with val as val and link to next node and prev node as None
        '''
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        '''
        Initialize a head node and size of linked list
        '''
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        '''
        Get value at given index (0-index based) of linkedlist
        else it will return -1 if index is invalid
        '''
        if index >= self.size or index < 0:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        '''
        Add node to the head of linked list
        '''
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        '''
        Add node to the last of linked list
        '''
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Add node at specific index (valid) of linked list
        '''
        # Handling case for invalid index value
        if index > self.size or index < 0:
            return
        temp = Node(val)

        # Add node to the front of linked list
        if index == 0:
            temp.next = self.head
            if self.head:
                self.head.prev = temp
            self.head = temp
            self.size += 1
            return
        
        # Add node at given index of list, including in the tail of linked list
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        temp.next = curr.next
        if curr.next:
            curr.next.prev = temp
        temp.prev = curr
        curr.next = temp
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        '''
        Delete node from given valid index else skip
        '''
        # Handling case for invalid index value
        if index >= self.size or index < 0:
            return
        
        # Deleting node from the front of linked list
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return
        
        # Deleting node from given index of list
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        curr.next = curr.next.next
        if curr.next:
            curr.next.prev = curr
        self.size -= 1
        return
    
    def getValues(self) -> List[int]:
        '''
        Return val at each node in the linked list
        '''
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
obj = MyLinkedList()
print(obj.get(0))
obj.addAtHead(1)
print(obj.getValues())
obj.addAtTail(3)
print(obj.getValues())
obj.addAtIndex(1,2)
print(obj.getValues())
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.getValues())
print(obj.size)
print(obj.get(1))