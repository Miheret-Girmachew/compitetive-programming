class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n =  len(arr)
        val = int(n * 0.25)
        hashh = {}
        for i in range(n):
            hashh[arr[i]]=hashh.get(arr[i],0)+1
        for key, value in hashh.items():
            if value > val:
                return key
        