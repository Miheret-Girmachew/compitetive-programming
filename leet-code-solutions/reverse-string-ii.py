class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        neww = ""
        i=0
        while(i<len(s)):
            reversee = s[i:i+k][::-1]
            neww += reversee
            val = s[i+k:i+(2*k)]
            neww += val
            i+= 2*k
        return neww