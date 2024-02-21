class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        count = 0
        hs= {}
        for i in range(len(nums)):
            hs.clear()
            print(hs)
            for j in range(len(nums)):
                hs[nums[j]] = hs.get(nums[j], 0)+1
                print(hs)
                print(len(hs))
                if len(hs) == len(set(nums)):
                    count += 1
                    print(i)
        
        return count
        """
        n = len(nums)
        m = len(set(nums))

        ans=0
        for i in range(n):
            sett=set()
            for j in range(i,n):
                # print(sett)
                sett.add(nums[j])
                if len(sett)==m:
                    ans+=1

        return ans 
        
        

   