class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(x):
            count = 1
            summ = 0
            for i in range(len(weights)):
                if summ + weights[i] <= x:
                    summ += weights[i]
                
                else:
                    count+=1 
                    summ = weights[i]

           
            return count




        minn = max(weights)
        maxx = sum(weights)
        while minn <= maxx:
            mid = (minn + maxx)//2
            val = check(mid)
            if val <= days:
                maxx = mid -1
            else :
                minn = mid+1

        return minn
                





            
            