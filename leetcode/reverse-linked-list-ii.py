# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left_pre = dummy
        curr = head
        for i in range(left-1):
            left_pre = curr
            curr = curr.next
        right_pre = None
        for i in range(right - left+1):
            temp = curr.next
            curr.next=right_pre
            right_pre = curr
            curr = temp
        left_pre.next.next = curr
        left_pre.next=right_pre
        return dummy.next
        
       

            

        