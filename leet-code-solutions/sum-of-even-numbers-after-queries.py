class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans= []
        summ=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                summ+= nums[i]
        for i in range(len(queries)):
            v = nums[queries[i][1]]
            if v % 2 == 0:
                nums[queries[i][1]]+= queries[i][0]
                if nums[queries[i][1]] % 2  == 0:
                    summ= summ - v + nums[queries[i][1]]
                else:
                    summ= summ - v
            elif v%2 !=0:
                nums[queries[i][1]]= nums[queries[i][1]] + queries[i][0]
                if nums[queries[i][1]] % 2  == 0:
                    summ= summ + nums[queries[i][1]]
                
            ans.append(summ)
         
        return ans
                
                
                
                
                
                
          
        