class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashh={}
        summ=0
        maxx=0
        l=0
        for r in range(len(nums)):
            if nums[r] in hashh:
                hashh[nums[r]]+=1
                summ+=nums[r]
                while(hashh[nums[r]]>1):
                    summ-=nums[l]
                    if nums[l]!=nums[r]:
                        hashh.pop(nums[l])
                    else:
                        hashh[nums[l]]-=1
                    l+=1
                maxx=max(summ, maxx)
                print(summ)
            else:
                hashh[nums[r]]=1
                summ+=nums[r]
                print(summ)
                maxx=max(summ, maxx)
        return maxx


        