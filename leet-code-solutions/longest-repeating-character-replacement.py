class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hs ={}
        maxx=0
        l=0
        freqq=0
        for r in range(len(s)):
            hs[s[r]]=hs.get(s[r],0)+1
            freqq = max(freqq, hs[s[r]])
            if (r-l+1)-freqq>k:
                hs[s[l]]-=1
                l+=1       
            maxx=max(maxx,r-l+1)
        return maxx






                    



            

        