class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.l = ListNode(0)
        self.r = ListNode(0)
        self.l.next = self.r
        self.r.prev = self.l
        

    def get(self, index: int) -> int:
        temp = self.l.next
        while temp and index > 0:
            temp = temp.next
            index -= 1
        if temp and temp != self.r and index==0:
            return temp.val
            
        
        return -1
        

        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        next = self.l.next
        prev = self.l
        prev.next = node
        next.prev= node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.r
        prev = self.r.prev
        prev.next = node
        next.prev= node
        node.next = next
        node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.l.next
        while temp and index>0:
            temp = temp.next
            index -=1
        if temp and index == 0:
                node = ListNode(val)
                next = temp
                prev = temp.prev
                prev.next = node
                next.prev= node
                node.next = next
                node.prev = prev

            
            
            
        

    def deleteAtIndex(self, index: int) -> None:
        temp = self.l.next
        while temp and index>0:
            temp = temp.next
            index -=1
        if temp and temp!= self.r and index == 0:
                next = temp.next
                prev = temp.prev
                next.prev = prev
                prev.next = next
               
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)