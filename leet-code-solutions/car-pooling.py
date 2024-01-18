class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre = [0]*1001
        tot=0
        for trip in trips:
            pre[trip[1]]+=trip[0]
            pre[trip[2]]-=trip[0]
        for val in pre:
            tot+=val
            if tot>capacity:
                return False
        return True
            




        
        