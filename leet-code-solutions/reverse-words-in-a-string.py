class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        n = len(s)
        i = 0
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i>=n :
                break
            j = i + 1
            while j < n and s[j] != " ":
                j += 1
            sub = s[i:j]
            if len(ans) == 0:
                ans = sub
            else:
                ans = sub + " " + ans
            i = j + 1
        return ans

   
           

            
            
        