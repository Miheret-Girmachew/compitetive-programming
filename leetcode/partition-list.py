# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    
        # new0 = ListNode()
        head0 = ListNode()
        # new1 = ListNode()
        # head1 = new1
        # new2 = ListNode()
        head2 = ListNode()

        new0 = head0
        new2 = head2

        curr = head
        while curr:
            if curr.val < x:
                new0.next = curr
                new0 = new0.next
            # elif curr.val == x:
            #     new1.next = ListNode(curr.val)
            #     new1 = new1.next
            else:
                new2.next = curr
                new2 = new2.next
            curr = curr.next

       
        # head0 = head0.next if head0.next else head1.next if head1.next else head2.next
        # if head1.next:
        #     new0.next = head1.next
        # if head2.next:
        #     new1.next = head2.next
        new0.next = head2.next
        new2.next = None

        return head0.next