class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            num=abs(num)
            s=[]
            while(num>0):
                digit=num%10
                s.append(str(digit))
                num=num//10
            s.sort(reverse=True)
            ans="".join(s)
            ans=int(ans)
            ans=0-ans
        elif num>0:
            s=[]
            while(num>0):
                digit=num%10
                s.append(str(digit))
                num=num//10
            s.sort()
            if "0" in s:
                times = s.count("0")
                s.insert(times+1,"0"*times)
            ans="".join(s)
            ans=int(ans)
        else:
            ans=num

        return ans
            
            


        