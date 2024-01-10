class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for r in range(len(nums)):
            if nums[r]!=val and nums[l]==val:
                nums[l], nums[r]= nums[r], nums[l]
            if nums[l]!=val:
                l+=1
        return l


