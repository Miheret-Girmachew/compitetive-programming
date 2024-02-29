# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        def traverse(root):
            if root:
                traverse(root.left)
                self.ans.append(root.val)
                traverse(root.right)
            else:
                return
        traverse(root)
        ans2 = sorted(self.ans)
        # print(self.ans)
        # print(ans2)
        if len(set(self.ans)) != len(self.ans):
            return False
        for i in range(len(self.ans)):
            if self.ans[i] != ans2[i]:
                return False
        return True
            
        