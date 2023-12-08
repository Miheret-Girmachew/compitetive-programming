class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        after = []
        before = []
        equal = []
        ans = []
        
        for num in nums:
            if num < pivot:
                before.append(num)
                
            elif num > pivot:
                after.append(num)
                
            else :
                equal.append(num)
                
        for val in before:
            ans.append(val)
        
        for val in equal:
            ans.append(val)
            
        for val in after:
            ans.append(val)
            
        return ans
                
        
        