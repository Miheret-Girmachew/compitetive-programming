class TimeMap:

    def __init__(self):
        self.hs = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hs:
            self.hs[key]=[]
        self.hs[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        for keyy in self.hs:
            if keyy == key:
                vall=self.hs[key]
        if key not in self.hs:
            vall = []
    
        l = 0
        r = len(vall)-1
        while l<=r:
            mid = (l+r)//2
            if vall[mid][1]<=timestamp:
                ans = vall[mid][0]
                l=mid+1
            else:
                r = mid-1
        return ans


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)