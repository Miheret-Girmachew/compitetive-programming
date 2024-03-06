class Solution:
    def mySqrt(self, x: int) -> int:
        maxx = (2 ** 31) - 1
        minn = 0
        while minn <= maxx:
            mid = (minn+maxx)//2
            if mid**2 <= x:
                minn = mid+1
            else:
                maxx = mid-1
        return maxx
    
