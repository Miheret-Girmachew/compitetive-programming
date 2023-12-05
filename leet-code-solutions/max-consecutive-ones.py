class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countt=[]
        count=0
        for num in nums:
            if num!=0:
                count+=1
            else: 
                countt.append(count)
                count=0
        countt.append(count)
                
        return max(countt)
        