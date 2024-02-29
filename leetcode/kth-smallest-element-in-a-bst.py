# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # result = []
        # def traverse(root, count):
        #     if root:
        #         traverse(root.left, count)
        #         if len(result) < k:
        #             result.append(root.val)
        #         traverse(root.right, count)
        # traverse(root, k)
        # return result[k-1]

        self.count = 0
        def traverse(root, k):
            if root:
                left_result = traverse(root.left, k)
                if left_result is not None:
                    return left_result

                self.count += 1
                if self.count == k:
                    return root.val

                right_result = traverse(root.right, k)
                if right_result is not None:
                    return right_result

        return traverse(root, k)

        