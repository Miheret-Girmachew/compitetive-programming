class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        c1=0
        co=0
        maxx=0
        l=0
        for r in range(len(nums)):
            if nums[r]==1:
                c1+=1
            else:
                co+=1
                while co>k:
                    if nums[l]==0:
                        co-=1
                    l+=1
                    
            maxx=max(maxx,r-l+1)
        return maxx