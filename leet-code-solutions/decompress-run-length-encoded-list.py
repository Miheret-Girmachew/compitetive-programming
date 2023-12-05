class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            num= nums[i+1]
            times= nums[i]
            ans.extend([num]*times)
        return ans
            
            