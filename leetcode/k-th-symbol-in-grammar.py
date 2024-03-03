class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        midpoint = 2 ** (n - 2)
        
        if k <= midpoint:
            return self.kthGrammar(n - 1, k)
  
        else:
            return 1 - self.kthGrammar(n - 1, k - midpoint)


        
        # def find(s):
        #     if len(s)==2**(n-1)//2:
        #         return int(s[k-1])
            
        #     ans = ""   
        #     for i in range(len(s)):
        #         if s[i] == "0":
        #             ans += "01"
        #         else:
        #             ans += "10"

        #     return find(ans)

        # if k < 2**(n-1)//2:
        #     return find("0")
        # else:
        #     return find("1")
            

        # def find(s):
        #     if len(s)==2**(n-1):
        #         return int(s[k-1])

        #     ans = ""   
        #     for val in s:
        #         if val == "0":
        #             ans += "01"
        #         else:
        #             ans += "10"
        #     return find(ans)
            

        # return find("0")
    