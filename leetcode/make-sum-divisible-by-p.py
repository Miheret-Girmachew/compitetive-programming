class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        if summ % p == 0 :
            return 0
        hs = {}
        prefix = [0]
        sums = 0
        ans = len(nums)
        for num in nums:
            sums += num
            prefix.append(sums)
        target = summ % p
        for i in range(len(prefix)):
            see = (prefix[i] - target)% p
            if see in hs:
                ans = min(ans, i-hs[see])
            hs[prefix[i]%p]=i
        if ans == len(nums):
            return -1
        return ans

        
        