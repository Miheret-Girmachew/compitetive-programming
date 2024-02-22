class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minn or self.minn[-1]>=val:
            self.minn.append(val)

        
    
    def pop(self) -> None:
        if self.stack:
            if self.stack[-1]==self.minn[-1]:
                self.minn.pop()
            self.stack.pop()
        
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minn: 
            return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()