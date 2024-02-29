# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root, value):
            if not root:
                return 0
            value = value*10 + root.val
            if not root.left and not root.right:
                return value
            return traverse(root.left, value) + traverse(root.right, value)
        
        return traverse(root, 0)


            
        