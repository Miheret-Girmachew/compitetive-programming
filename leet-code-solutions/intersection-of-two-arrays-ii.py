class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashh1={}
        hashh2={}
        ans=[]
        for num in nums1:
            hashh1[num]=hashh1.get(num,0)+1
        for num in nums2:
            hashh2[num]=hashh2.get(num,0)+1
        sett =set(nums1)
        for num in sett:
            if num in nums2:
                minn=(min(hashh1[num],hashh2[num]))
                for i in range(minn):
                    ans.append(num)
        return ans
