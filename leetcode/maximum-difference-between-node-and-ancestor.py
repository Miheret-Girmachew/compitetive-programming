# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def traverse(root,maxx,minn):
            print(self.answer)
            if not root:
                self.answer = max(self.answer, maxx - minn)
                return 
                
            maxx = max(maxx, root.val)
            minn = min(minn, root.val)
           
            traverse(root.left,maxx,minn) or traverse(root.right,maxx,minn)
        traverse(root,0, float("inf"))
        return self.answer 
        
        