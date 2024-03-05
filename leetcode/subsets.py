class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        new = []
        ans = [[]]
        def backtrack(i):
            if i >= len(nums):
                return 
            for j in range(i, len(nums)):
                new.append(nums[j])
                ans.append(new[:])
                backtrack(j+1)
                new.pop()
        backtrack(0)
        return ans
        
        