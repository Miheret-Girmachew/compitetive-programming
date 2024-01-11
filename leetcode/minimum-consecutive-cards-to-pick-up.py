class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = []
        hashh = {}
        l = 0
        for r in range(len(cards)):
            if cards[r] not in hashh:
                hashh[cards[r]] = 1
            else:
                hashh[cards[r]]+=1
                while(hashh[cards[l]]!=hashh[cards[r]]):
                    hashh.pop(cards[l])
                    l+=1
                ans.append(r-l+1)
                hashh[cards[l]]-=1
                l+=1
        if not ans:
            return -1
        return min(ans)
                
                
        