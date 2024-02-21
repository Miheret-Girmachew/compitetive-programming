class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = [0]
        summ = 0
        for num in nums:
            summ += num
            prefix.append(summ)
        for i in range(1,len(prefix)):
            prefix[i] = ceil(prefix[i] / i)
        return max(prefix)
        