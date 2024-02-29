# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        found = True
        while queue:
            n = len(queue)
            ans = []
            for i in range(n):
                node = queue.popleft()
                if node:
                    ans.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if ans and found:
                res.append(ans)
            elif ans and not found:
                res.append(ans[::-1])
            if found:
                found = False
            elif not found:
                found = True

                
        return res

        
        # self.hs={}
        # self.level = 0
        # self.found =True
        # def traverse(root):
        #     if not root:return
        #     if root:
        #         self.hs[root.val]=self.level
        #     if self.found:
        #         self.level+=1 
        #     self.found= False
        #     traverse(root.left)
        #     traverse(root.right)
        #     self.found = True
        
        # traverse(root)
        # print(self.hs)
        # new_hs = {}
        # for key,value in self.hs.items():
        #     if value not in new_hs:
        #         new_hs[value]=[]
        #     new_hs[value].append(key)
        # ans = []
        # for i in new_hs:
        #     if i%2 == 1:
        #         ans.append(new_hs[i][::-1])
        #     else:
        #         ans.append(new_hs[i])
            
        # return ans
                              
            

        