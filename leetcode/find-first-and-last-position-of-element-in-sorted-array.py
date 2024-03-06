class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = -1
        r = len(nums)
        ans= []
        found = False
        while l+1 < r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid
            elif target <= nums[mid]:
                if target == nums[mid]:
                    found =True
                r = mid
        if found == True:
            ans.append(r)
        else:
            ans.append(-1)

        l = -1
        r = len(nums)
        found = False
        while l+1 < r:
            mid = (l+r)//2
            if target >= nums[mid]:
                if target == nums[mid]:
                    found =True
                l = mid
            elif target < nums[mid]:
                r = mid
        if found == True:
            ans.append(l)
        else:
            ans.append(-1)

        if ans:
            return ans
       

        



                
               
        