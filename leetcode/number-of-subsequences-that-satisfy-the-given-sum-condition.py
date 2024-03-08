class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] + nums[r] <= target:
                count+=pow(2,r-l)
                count = count%(10**9 + 7)
                l += 1
            else:
                r -= 1
        return count%(10**9 + 7)

        
      


            
        