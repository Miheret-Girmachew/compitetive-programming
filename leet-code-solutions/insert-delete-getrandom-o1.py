class RandomizedSet:

    def __init__(self):
        self.hashh={}
        self.array = []
        

    def insert(self, val: int) -> bool:
        if val in self.hashh:
            return False
        self.hashh[val]=len(self.array)
        self.array.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.hashh:
            return False
        lastt = self.array[-1]
        indexx = self.hashh[val]
        self.hashh[lastt]=indexx
        self.array[indexx]=lastt
        self.array[-1]=val
        self.array.pop()
        self.hashh.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()