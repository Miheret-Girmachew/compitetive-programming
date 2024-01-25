# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        slow=head
        fast=head        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        temp2 = None
        temp = slow
        while temp:
            temp3 = temp.next
            temp.next = temp2
            temp2 = temp
            temp = temp3
        while temp2 and first:
            if first.val!=temp2.val:
                return False
            first=first.next
            temp2=temp2.next
        return True
       

