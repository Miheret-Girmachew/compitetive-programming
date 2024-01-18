class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        suf=[]
        smul=1
        mul = 1
        final=[]
        for i  in range(1, len(nums)):
            mul*=nums[i-1]
            pre.append(mul)
        numm = nums[::-1]
        for i in range(len(nums)-1):
            smul*=numm[i]
            suf.append(smul)
        ssuf = suf[::-1]
        ssuf.append(1)
        print(ssuf)
        print(pre)
        for i in range(len(nums)):
            final.append(ssuf[i] * pre[i])
        return final
        
    
    
       



            



        