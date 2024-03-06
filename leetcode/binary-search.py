class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        found = False
        while left+1 < right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            elif target == nums[mid]:
                found = True
                return mid
        if found == False:
            return -1




        