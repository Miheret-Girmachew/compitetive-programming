# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        temp=head
        if head:
            while temp.next:
                sett.add(temp)
                temp=temp.next
                if temp.next in sett:
                    return True
        return False
        