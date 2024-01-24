# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp2 = None
        temp = head
        while temp:
            temp3 = temp.next
            temp.next = temp2
            temp2 = temp
            temp = temp3
        return temp2


        