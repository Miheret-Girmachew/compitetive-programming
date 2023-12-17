class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1 ):
            char=True
            for j in str(i):
                if j!='0':
                    if i%int(j)!=0:
                        char=False
                else:
                    char=False
                    break   
            if char:
                ans.append(i)
        return ans