class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sortt = sorted(nums)
        hashh={}
        for i, num in enumerate(sortt):
            if num not in hashh:
                hashh[num]=i
        print(hashh)
        for num in nums:
            ans.append(hashh[num])
        return ans





        