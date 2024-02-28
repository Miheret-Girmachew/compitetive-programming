# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # curr , left? ->curr.left 
        # ans = []
        # if root:
        #     ans.append(root.val)
        #     while root.left:
        #         ans.append(root.left)
        #         if root.left:
        #             root -> root.left
        #         else:
        self.ans =[] 
        def traverse(root):          
            if root:
                self.ans.append(root.val)
                traverse(root.left)
                traverse(root.right) 
        traverse(root)
        return self.ans


        