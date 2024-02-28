 # Definition for\ a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(left_val, right_val):
            if not left_val and not right_val:
                return True
            elif right_val and not left_val:
                return False
            elif not right_val and left_val:
                return False
            else:
                return left_val.val == right_val.val and traverse(left_val.left,right_val.right) and  traverse(left_val.right, right_val.left)
        
        return traverse(root.left, root.right)
        