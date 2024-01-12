class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        nice=0
        curr=0
        l=0
        for r in range(len(nums)):
            if nums[r]%2==1:
                count+=1
                curr=0
            while(count==k):
                if nums[l]%2==1:
                    count-=1
                curr+=1
                l+=1
            nice+=curr
        
        return nice
                