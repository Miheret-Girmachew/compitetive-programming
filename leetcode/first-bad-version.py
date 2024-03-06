# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = -1
        r = n+1
        ans = [] 
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if isBadVersion(mid) == False:
                l = mid+1
            elif isBadVersion(mid) == True:
                ans.append(mid)
                r = mid-1
            

        print(ans)
        if ans:
            ans.sort()
            return ans[0]
        
        
        