class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        '''
        l=0
        r=n
        ans=[]
        while(l<n and r<2*n):
            ans.append(nums[l])
            ans.append(nums[r])
        return ans
        '''
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans
            