class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minn = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if abs(summ - target) < abs(minn - target):
                    minn=summ
                if summ == target:
                    return target
                elif summ < target:
                    l += 1
                else:
                    r -= 1
        return minn