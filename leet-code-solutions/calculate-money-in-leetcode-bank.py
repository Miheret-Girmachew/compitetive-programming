class Solution:
    def totalMoney(self, n: int) -> int:
        summ=0
        val = 0
        if n%7 != 0 :
            days = n%7
        else:
            days = 7
       
        if n%7 == 0:
            times= n//7
        else:
            times= n//7 + 1
            
            
        for i in range(times-1):
            for j in range(i+1,i+8):
                summ+=j
            val=i+1
            print(val)
            print(summ)
        print(summ)
            
        for k in range(val+1, val+1+days):
            summ+=k
            
        return summ
            
        
        
   
            

        
        