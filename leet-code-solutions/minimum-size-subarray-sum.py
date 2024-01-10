class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = len(nums)+1
        l = 0
        summ = 0
        r=0
        while r<len(nums):
            summ += nums[r]
            while(summ>=target):
                minn=min(minn,r-l+1)
                summ-=nums[l]
                l+=1
            r+=1
        if minn == len(nums)+1:
            return 0
        return minn


 



 
                


            

                