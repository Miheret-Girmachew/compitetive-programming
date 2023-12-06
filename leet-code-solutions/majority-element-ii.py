class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashh = {}
        ans = []
        n = len(nums)
        for num in nums:
            hashh[num] = hashh.get(num,0)+1
            
        for num in nums:
            if hashh[num] > n/3:
                ans.append(num)
        anss=set(ans)
                
        return anss