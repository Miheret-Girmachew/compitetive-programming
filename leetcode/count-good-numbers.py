class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # def find(x, y):
        #     if y == 0:
        #         return 1
        #     z = find(x,  y // 2)

        #     # find(x, ceil(y / 2)) * find(x,  y // 2)
            
        #     if y % 2:
        #         return (z*z*x) % (10**9 + 7)
        #     else:
        #         return (z*z) % (10**9 + 7)

        # if n%2:
        #     ans  =find( 5 , ceil(n/2) ) * find(4 , n//2)
        # else:
        #     ans = find( 5 , n//2 ) * find(4 , n//2)
        # return ans % (10**9 + 7)




        if n%2:
            ans = pow(5,ceil(n/2), 10**9 + 7) * pow(4, n//2,10**9 + 7)
        else:
            ans = pow(5 , n//2,10**9 + 7) * pow(4, n//2,10**9 + 7)
        return ans % (10**9 + 7)
        
      
            

        

        
        