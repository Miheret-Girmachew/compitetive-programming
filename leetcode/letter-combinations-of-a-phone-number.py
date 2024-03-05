class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hs = {
2: "abc",
3: "def",
4: "ghi",
5: "jkl",
6: "mno",
7: "pqrs",
8: "tuv",
9: "wxyz"
}
        ans = []
        new = []
        n = len(digits)
        def backtrack(i):
            if len(new) == n:
                ans.append("".join(new))
                return
            for j in range(len(hs[int(digits[i])])):
                new.append(hs[int(digits[i])][j])
                backtrack(i+1)
                new.pop()
            return ans
        return backtrack(0)
       

        