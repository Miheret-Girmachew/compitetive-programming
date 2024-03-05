class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        ans = []
        new = []
        sett = set()

        def backtrack(i):
            if sum(new) == target:
                neww = sorted(new[::])
                tup = tuple(neww)
                if tup not in sett:
                    ans.append(neww)
                    sett.add(tup)

                return 
            if  sum(new) > target:
                return
            vall =  None
            for j in range(i, len(candidates)):
                if candidates[j]!=vall:
                    new.append(candidates[j])
                    backtrack(j+1)
                    vall = new.pop()
            return ans
            # new.append(candidates[i])
            # backtrack(i, total + candidates[i], new)
            # new.pop()
            # backtrack(i+1, total, new)
        return backtrack(0)

        

        