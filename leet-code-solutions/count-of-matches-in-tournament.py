class Solution:
    def numberOfMatches(self, n: int) -> int:
        summ=0
        while(n>1):
            if n%2==0:
                matches=n//2
                summ+=matches
                n=matches
            else:
                matches=(n-1)//2
                summ+=matches
                n=matches+1
        return summ