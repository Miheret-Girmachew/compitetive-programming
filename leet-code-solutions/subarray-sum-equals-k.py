class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        summ=0
        count=0
        hs={0: 1}

        for num in nums:
            summ+=num
            x = summ-k
            count+=hs.get(x,0)
            hs[summ]=hs.get(summ,0)+1
            
        return count


   






        