class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""

        length=len(strs[0])
        first=strs[0]
      
        for i in range(length):
            c=first[i]
            for s in strs:
                if  i>= len(s) or c!=s[i]  :
                    return prefix
            prefix+=c
        return prefix