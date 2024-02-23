class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        maxx = deque()
        l=0
        for i in range(len(nums)):
            if not maxx:
                maxx.append(nums[i])

            else:
                # print(maxx)
                while maxx and  maxx[-1]<nums[i]:
                    maxx.pop()
                maxx.append(nums[i])
                # print(maxx)
            if i-l+1 > k:
                if maxx[0]==nums[l]:
                    maxx.popleft()
                l+=1
            if i-l+1 == k:
                ans.append(maxx[0])
        if len(nums)<k:
            return maxx
        return ans

            
    

        

        