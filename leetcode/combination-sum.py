class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        new = []
        ans = []
        def backtrack(i, summ, new):
            if summ == target:
                ans.append(new[:])
                return
            if i >= len(candidates) or  summ > target :
                return
            new.append(candidates[i])
            backtrack(i, summ+candidates[i], new)
            new.pop()
            backtrack(i+1,summ, new)
        backtrack(0, 0, [])
        return ans
            
            #     val = sum(new)
            #     while( val+candidates[j] <= target):
            #         val+=candidates[j]
            #         if val == target:
            #             break
            #         new.append(candidates[j])
            #     backtrack(j+1)
            #     if new:
            #         new.pop()
            #     return
            # return ans
            # backtrack(0)


        