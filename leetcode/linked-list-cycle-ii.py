# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # floyd's cycle needed
        # if there is cycle in floyd's algorithm the faster pointer will meet the slow pointer
        # else the fast pointer meet the end first
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow =slow.next
                    fast = fast.next
                return slow
        return None
        # or can also be implemented using set



        