class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashh = {}
        ans=[0]*len(nums)
        for i in range(len(nums)):
            hashh[nums[i]]=i
            
        for i in range(len(operations)):
            k = hashh[operations[i][0]]
            del hashh[operations[i][0]]
            hashh[operations[i][1]]= k
        for key, value in hashh.items():
            ans[value]=key
        return ans
            
            
        
            
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        