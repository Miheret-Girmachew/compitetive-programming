class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[0:k])
        maxx=summ
        l=0
        for i in range(k, len(nums)):
            summ+=nums[i]
            summ-=nums[l]
            maxx=max(maxx, summ)
            l+=1
        return maxx/k

        