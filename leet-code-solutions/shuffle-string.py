class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashwords = {}
        ans=[0]*len(s)
        
        for i in range(len(s)):
            hashwords[indices[i]] = s[i]
           
        for i in range(len(s)):
            ans[i] = hashwords[i]
        
            
        return "".join(ans)
            