# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if  list1.val <= list2.val:
                neww = ListNode()
                neww.val = list1.val
                curr.next = neww
                curr = neww
                list1 = list1.next
            
            else:
                neww = ListNode()
                neww.val = list2.val
                curr.next = neww
                curr = neww
                list2 = list2.next

        if list1 == None and list2:
            curr.next = list2
        elif list2 == None and list1:
            curr.next = list1
        
        return dummy.next
    


                


