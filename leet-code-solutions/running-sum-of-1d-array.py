class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        summ=0
        for i in range(len(nums)): 
            summ+=nums[i]
            ans[i]=summ
        return ans