class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        lv=0
        maxx=0
        for r in range(len(s)):
            
            if r-l+1>k:
                if s[l]=='a' or s[l]=='e'or s[l]=='i' or s[l]=='o' or s[l]=="u":
                    lv-=1
                l+=1
        
            if s[r]=='a' or s[r]=='e'or s[r]=='i' or s[r]=='o' or s[r]=='u':
                lv+=1
                maxx=max(maxx,lv)

        return maxx
                
        