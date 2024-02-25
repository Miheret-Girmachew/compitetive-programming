# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listt = []
        while head:
            listt.append(head.val)
            head = head.next
        listt.sort()
        dummy = ListNode(0)
        curr = dummy 
        for i in range(len(listt)):
            neww = ListNode()
            neww.val = listt[i]
            curr.next = neww
            curr = neww
        return dummy.next
            

        