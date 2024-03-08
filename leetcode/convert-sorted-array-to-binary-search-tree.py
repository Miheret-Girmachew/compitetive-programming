# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(left,right):
            if left>right:
                return None
            mid = (left+right)//2
            left = tree(left, mid-1)
            right = tree(mid+1, right)
            return TreeNode(nums[mid], left, right)
        
        return tree(0,len(nums)-1)
        











        res = []
        queue = deque()
        queue.append(root)
        found = True
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                res.append(node)

                if node:
                    ans.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        return res
        