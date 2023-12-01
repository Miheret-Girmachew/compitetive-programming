class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        n1=len(word1)
        n2=len(word2)
        i=0
        val=min(n1,n2)
        while(i<val):
            s+=word1[i]
            s+=word2[i]
            i+=1
        if val!=n1:
            s+=word1[val:]
        elif val!=n2:
            s+=word2[val:]
            
        return s
        
            
            
        