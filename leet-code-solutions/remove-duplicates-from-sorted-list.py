# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if not head:
            return None

        while temp:
            if temp.next and temp.val == temp.next.val:
                temp2 = temp.next
                while temp2 and temp.val == temp2.val:
                    temp2 = temp2.next
                temp.next = temp2
            else:
                temp = temp.next
        return head
                






                
                
            
        