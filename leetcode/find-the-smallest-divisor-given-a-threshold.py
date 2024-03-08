class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxx = max(nums)
        def check(x):
            count = 0
            for i in range(len(nums)):
                if nums[i]<=x:
                    count+=1
                elif nums[i] > x and nums[i]%x:
                    count+=nums[i]//x
                    count+=1
                elif nums[i] > x and nums[i]%x==0:
                    count+=nums[i]//x
            return count


        l = 1
        r = maxx
        while l<=r:
            mid = (l+r)//2
            result = check(mid)
            print("r",result)
            if result <= threshold:
                r = mid-1
            else:
                l = mid+1
        return l


        