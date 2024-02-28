# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.left_Height = 0
        self.right_Height = 0
        def traverse(root):
            if not root:
                return 0
            else: 
                return 1 + max(traverse(root.left),traverse(root.right) )

        return traverse(root)
     