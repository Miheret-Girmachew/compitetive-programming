# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       
        tempA = headA
        countA = 0
        while tempA:
            countA += 1
            tempA = tempA.next
        tempB = headB
        countB = 0
        while tempB:
            countB += 1
            tempB = tempB.next
        
        if countA > countB:
            while countA > countB:
                headA = headA.next
                countA -= 1
        if countB > countA:
            while countB > countA:
                headB = headB.next
                countB -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    
        


        