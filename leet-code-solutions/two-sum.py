class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashh:
                return [hashh[target - nums[i]],i]
            else:
                hashh[nums[i]]=i
                
        
            
        