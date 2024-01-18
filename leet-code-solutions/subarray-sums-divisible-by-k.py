class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = 0
        final = 0
        hs = defaultdict(int)
        hs[0]=1
        for num in nums:
            summ+=num
            if (summ%k) in hs:
                final+=hs[summ%k]
            hs[summ%k] += 1
        return final
       
   