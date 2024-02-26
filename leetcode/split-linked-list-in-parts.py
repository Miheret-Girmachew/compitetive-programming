# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        ans = [] 
        curr = head
        while curr:
            curr = curr.next
            n += 1
        subb = n // k
        last = n % k
        curr=head
        pre=None
        for i in range(k):
            ans.append(curr)
            for j in range(subb):
                if curr:
                    pre = curr
                    curr =curr.next
            if last and curr:
                pre = curr
                curr =curr.next
                last -= 1
            if pre:
                pre.next= None
        return ans


        