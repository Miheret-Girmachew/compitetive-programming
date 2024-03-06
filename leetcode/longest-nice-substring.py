class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                count = 0
                for k in s[i:j+1]:
                    if k.swapcase() in s[i:j+1]:
                        count+=1
                if count == len(s[i:j+1]):
                    ans.append(s[i:j+1])
        hs = {}
        # print(ans)
        if ans:
            for val in ans:
                hs[val]=len(val)
      
        if ans:
            ans.sort(key = len)
        # print(ans)
    
        if hs:
            for val in hs:
                if len(val) == len(ans[-1]):
                    return val
        else:
            return ""
        
        # if ans:
        #     ans.sort(key = len)
        #     ans.sort(reverse=True)
        #     return ans[0]
        # else:
        #     return ""

        