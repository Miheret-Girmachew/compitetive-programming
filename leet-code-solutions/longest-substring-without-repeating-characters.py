class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist=[]
        left=0
        maximum=0
        for right in range(len(s)):
            while s[right] in slist:
                slist.remove(s[left])
                left+=1
            slist.append(s[right])
            maximum=max(maximum,right-left+1)
        return maximum



        