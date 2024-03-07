class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = float("-inf")
        for i in range(len(houses)):
            l = 0
            r = len(heaters)-1
            minn = float("inf")
            while l <= r:
                mid = (l+r)//2
                if houses[i] < heaters[mid]:
                    minn = min(minn, abs(houses[i] - heaters[mid]))
                    r = mid-1
                else:
                    minn = min(minn, abs(houses[i] - heaters[mid]))
                    l =mid+1
            ans = max(ans, minn)
        return ans
