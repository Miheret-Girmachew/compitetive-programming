class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open = 0 
        close = 0 
        for val in s:
            if val == "(":
                open += 1
            elif val == ")":
                if open > 0:
                    open -= 1
                else:
                    ans += 1
                    
        if open > 0 :
            ans += open

        return ans