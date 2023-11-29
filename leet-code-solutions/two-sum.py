class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh={}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in hashh:
                return [ i, hashh[num2]]
            hashh[num1]=i
        return []
 


        