# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.found = False
        def traverse(root):
            if root:
                traverse(root.left)
                if root.val == low:
                    self.found = True
                if self.found:
                    self.ans += root.val
                if root.val == high:
                    self.found = False
                traverse(root.right)
        traverse(root)
        return self.ans
        