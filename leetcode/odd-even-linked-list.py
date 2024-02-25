# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  the question is one indexed
        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        head_odd = dummy_odd 
        head_even = dummy_even
        index = 1 # to track the odd first
        while head != None:
            if index % 2 == 0:
                head_even.next = head
                head_even = head_even.next
            else:
                head_odd.next = head
                head_odd = head_odd.next
            head = head.next
            index += 1
        head_even.next = None # to quite the cycle
        head_odd.next = dummy_even.next

        return dummy_odd.next

     