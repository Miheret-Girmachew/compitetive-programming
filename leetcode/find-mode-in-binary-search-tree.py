# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def traverse(root):
            if not root:
                return
            if root:
                traverse(root.left)
                self.ans.append(root.val)
                traverse(root.right)
        traverse(root)
        c = Counter(self.ans)
        maxx =  max(c.values())
        print(c)
        print(maxx)
        answer = []
        for val in c:
            if c[val]==maxx:
                answer.append(val)
        return answer
    
