class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        hp = {}
        hs = {}
        for i in range(len(p)):
            hp[p[i]]=hp.get(p[i],0)+1
            hs[s[i]]=hs.get(s[i],0)+1
        ans=[]
        if hp==hs:
            ans.append(0)

        j=0
        for i in range(len(p),len(s)):
            hs[s[i]]=hs.get(s[i],0)+1
            hs[s[j]]-=1
            if hs[s[j]]==0:
                hs.pop(s[j])
            j+=1
            if hs==hp:
                ans.append(j)
        return ans


   