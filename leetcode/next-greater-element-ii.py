class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numm = [0]* (n*2)
        for i in range(len(nums)):
            numm[i] = nums[i]
            numm[i+n] = nums[i]
        
        for i in range(len(nums)):
            found = False
            j = i+1
            while j < len(numm):
                if numm[j]>nums[i]:
                    nums[i] = numm[j]
                    found = True
                    break
                j+=1
            print(found)  
            if found == False:
                nums[i] = -1
            
                
        return nums


            
        