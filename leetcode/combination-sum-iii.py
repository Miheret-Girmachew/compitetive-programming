class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # candidates.sort()
        ans = []
        new = []
        sett = set()

        def backtrack(i):
            if sum(new) == n and len(new)==k:
                neww = sorted(new[:])
                tup = tuple(neww)
                if tup not in sett:
                    ans.append(neww)
                    sett.add(tup)
                return 
            if  sum(new) > n:
                return
            vall = None
            for j in range(i,10):
                if j!=vall:
                    new.append(j)
                    backtrack(j+1)
                    vall = new.pop()
            return ans
           
        return backtrack(1)