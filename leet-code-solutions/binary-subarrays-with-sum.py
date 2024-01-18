class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = [0]
        summ=0
        count=0
        hs={0: 1}

        for num in nums:
            summ+=num
            x = summ-goal
            count+=hs.get(x,0)
            hs[summ]=hs.get(summ,0)+1
            
        return count