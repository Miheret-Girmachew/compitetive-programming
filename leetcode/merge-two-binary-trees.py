# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # def traverse(root1, root2):
            # if root1 and root2:
            #     root1.val = root1.val + root2.val
            # elif root2 and not root1:
            #     root1 = TreeNode(root2.val)
            # elif not root2 and root1:
            #     root1.val = root1.val 
            # elif not root1 and not root2:
            #     return 

            # if root1 and root2:
            #     traverse(root1.left, root2.left)
            #     traverse(root1.right, root2.right)

            # return root1   
        # return traverse(root1, root2)
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left , root2.left)
            root.right = self.mergeTrees(root1.right , root2.right)
            return root
        else:
            return root1 or root2


        