class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nott=[]
        ans = []
        hashh = {}
        for num in arr1:
            if num in arr2:
                hashh[num]=hashh.get(num,0)+1
            else:
                nott.append(num)
        for num in arr2:
            for i in range(hashh[num]):
                ans.append(num)
        nott.sort()
        for num in nott:
            ans.append(num)
        return ans




        