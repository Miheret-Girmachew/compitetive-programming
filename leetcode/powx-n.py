class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x ** n
        if n < 0:
            return 1/self.myPow(x, -n)
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            if n%2!=0:
                return self.myPow(x,n-1)*x
            return self.myPow(x*x,n//2)

        
        
        