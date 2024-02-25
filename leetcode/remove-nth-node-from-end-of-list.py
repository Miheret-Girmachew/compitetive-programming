# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        curr = head
        i = 0
        while i != n and curr:
            curr = curr.next
            i += 1
        while curr:
            temp = temp.next
            curr = curr.next
        temp.next = temp.next.next
        return dummy.next


        