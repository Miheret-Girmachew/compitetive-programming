class Solution:
    def sortSentence(self, s: str) -> str:
        hashh={}
        ans=""
        ss=""
        for i in range(len(s)):
            if s[i].isnumeric():
                hashh[s[i]]=ss
                ss=""
            elif s[i] is not " ":
                ss+=s[i]
        keysort = list(sorted(hashh.keys()))
        for i in range(len(keysort)-1):
            ans+=hashh[keysort[i]]
            ans+=" "
        ans+=hashh[keysort[-1]]
        return ans


        