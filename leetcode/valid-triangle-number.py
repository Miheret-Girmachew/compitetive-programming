class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        for i in  range(len(nums)):
            count = 0
            k = i + 2
            for j in range(i+1,len(nums)-1):
                count += k - j - 1
                # print(j , k)
                # print( k - j - 1)
            
                while k < len(nums):
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
                    else:
                        if  j+1 == k:
                            k += 1
                        break
                    k += 1
                # print(count)   
                
                
            summ += count
        return summ
                


                    


      