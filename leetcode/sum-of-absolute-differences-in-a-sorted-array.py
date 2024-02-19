class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        pre = 0
        ans = []
        n = len(nums)
        for num in nums:
            pre += num
            prefix.append(pre)
        for i in range(n):
            before =abs( ((i+1) * nums[i]) - prefix[i+1])
            after = abs((prefix[n] - prefix[i+1]) - (( n-(i+1)) * nums[i]))
            ans.append(before + after)

        return ans


       


