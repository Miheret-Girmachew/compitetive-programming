class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        count = 0
        i = 0
        while tickets[k]>0:
            if tickets[i%n] != 0:
                tickets[i%n]-=1
                count += 1
    
            i+=1
        return count
        
            
        