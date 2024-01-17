class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        tot=[0]
        summ=0
        found=False
        for i in range(len(nums)):
            summ+=nums[i]
            tot.append(summ)
        for i in range(1, len(tot)):
            if total-tot[i]==tot[i-1]:
                found=True
                break
            else: continue
        if found==True:
            return i-1
        else:
            return -1
        


        