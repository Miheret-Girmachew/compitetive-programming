class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashh={}
        for letter in s1:
            hashh[letter]=hashh.get(letter,0)+1
        hash2={}
        l=0
        for r in range(len(s2)):
            if s2[r] not in hashh:
                while l <= r:
                    if s2[l] in hash2:
                        hash2[s2[l]] -= 1
                        if hash2[s2[l]] == 0:
                            del hash2[s2[l]] 
                    l += 1
            else:
                hash2[s2[r]]=hash2.get(s2[r],0)+1
                while hashh[s2[r]] < hash2[s2[r]]:
                    hash2[s2[l]] -= 1
                    if hash2[s2[l]] == 0:
                        del hash2[s2[l]]
                    l+=1
                if hash2==hashh:
                    return True
        return False
                




        