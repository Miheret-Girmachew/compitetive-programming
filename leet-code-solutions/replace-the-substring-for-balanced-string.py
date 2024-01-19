class Solution:
    def balancedString(self, s: str) -> int:
        hs =Counter(s)
        n = len(s) // 4
        hs2 = {} #extras
        for key in hs:
            if hs[key] > n:
                hs2[key] = hs[key] - n
        
        if not hs2:
            return 0
        i = 0
        res = len(s)
        for j in range(len(s)):
            if s[j] in hs2:
                hs2[s[j]] -= 1
            
            while max(hs2.values()) <= 0:
                res = min(res, j-i+1)
                if s[i] in hs2:
                    hs2[s[i]] += 1
                i += 1
                
                
        return res