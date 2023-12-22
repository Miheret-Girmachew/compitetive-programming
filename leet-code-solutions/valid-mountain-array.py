class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        sarr = sorted(arr)
        rsarr = sarr[:][::-1]
        print(sarr)
        print(rsarr)
        if len(arr) < 3 or arr == sarr or arr == rsarr:
            return False
        
        j=0
        for i in range(1, len(arr)):
            j=i
            if arr[i-1] == arr[i]:
                return False
            else:
                if arr[i-1] > arr[i]:
                    break
    
        reversee=arr[j:][::-1]

        lenn = len(set(reversee))
        if reversee == sorted(arr[j:]) and lenn== len(reversee):
            return True
        else:
            return False
       
"""
        count = 0
        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                return False
            elif arr[i-1] > arr[i] and i!=1:
                count = 1
        if count == 1:
            return True
        else:
            return False
            """
        