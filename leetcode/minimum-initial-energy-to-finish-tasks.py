class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:x[1]-x[0], reverse =True)
        summ = 0
        for t in tasks:
            summ += t[0]
        # m = max(tasks[0][1], summ)
        m =summ

        for t in tasks:
            if t[1] > m:

                summ += t[1] - m
                m = t[1]
                
            m -= t[0]

        return summ
        
        

        