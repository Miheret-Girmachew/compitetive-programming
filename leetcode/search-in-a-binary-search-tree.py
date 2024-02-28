# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # ans = []
        # def inorder_traversal(root):
        #     if root:
        #         ans.append(root.val)
        #         inorder_traversal(root.left)
        #         inorder_traversal(root.right)
        #     return ans
        if not root:
            return root
        if root.val == val:
            return root
        else:
            if val < root.val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)
        
   
        