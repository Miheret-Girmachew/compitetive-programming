class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        new = []
        def backtrack(i):
            if len(new)==k:
                ans.append(new[:])
                # print(new)
                # print(ans)
                return
            for j in range(i+1, n+1):
                if j <=n :
                    new.append(j)
                backtrack(j)
                if new:
                    new.pop()
        backtrack(0)
        return ans
        