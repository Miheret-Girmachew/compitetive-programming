class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        new = []
        ans = [[]]
        def backtrack(i):
            if i >= len(nums):
                return 
            for j in range(i, len(nums)):
                new.append(nums[j])
                if new not in ans:
                    ans.append(new[:])
                backtrack(j+1)
                new.pop()
        backtrack(0)
        return ans