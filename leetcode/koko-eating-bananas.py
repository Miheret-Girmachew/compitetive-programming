class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(x):
            count = 0
            for n in piles:
                if n%x:
                    count+=1
                count+=(n//x)
            return count
        minn = 0
        maxx = max(piles)+1
        while minn+1<maxx:
            mid = (minn+maxx)//2
            if check(mid)<=h:
                maxx = mid
            else:
                minn = mid
        return minn+1


                

        