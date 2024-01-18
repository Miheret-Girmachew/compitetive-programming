class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0]*(n+2)
        final=[]
        summ=0
        for s in bookings:
            pre[s[0]]+=s[2]
            pre[s[1]+1]-=s[2]
        for i in range(1,len(pre)):
            summ+=pre[i]
            final.append(summ)

        return final[:-1]

        