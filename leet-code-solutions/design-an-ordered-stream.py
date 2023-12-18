class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 1
        self.array = [None] * (n+2)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey] = value
        if idKey == self.pointer:
            while self.array[self.pointer] is not None:
                self.pointer += 1
            return self.array[idKey:self.pointer]
        return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
  


