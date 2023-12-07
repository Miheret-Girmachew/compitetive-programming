class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans = []

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        l = 0
        while l < len(nums) // 2:
            ans.append(positive[l])
            ans.append(negative[l])
            l += 1  
        return ans
