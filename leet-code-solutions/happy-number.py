class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        summ=0
        while n != 1:
            if n in sett :
                return False
            sett.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
        
        
         