class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]* len(nums)
        for i in range(len(requests)):
            prefix[requests[i][0]]+=1
            if(requests[i][1]<len(nums)-1):
                prefix[requests[i][1]+1]-=1
        
        for i in range(len(nums)):
            if(i==0):
                continue
            prefix[i]+=prefix[i-1]
        # print(prefix)

        prefix.sort()
        nums.sort()
        ans=0
        # print(prefix)
        # print(nums)
        for i in range(len(nums)-1,-1,-1):
            print(prefix[i])
            print(nums[i])
            ans+=(prefix[i]*nums[i])
        return ans%(10**9 + 7)


        # hs = {}
        # for val in requests:
        #     for i in range(val[0], val[1]+1):
        #         hs[i] = hs.get(i,0)+1
        # nums.sort(reverse=True)
        # ans = [0] * len(nums)
        # hsn = sorted(hs.items(), key=lambda x:x[1])
        # for i in range(len(nums)):
        #     ans[hsn[i]] = nums[i]
        # return ans


    