class Robot:

    def __init__(self, width: int, height: int):
        self.curr = [0,0]
        self.x = width
        self.y= height
        self.dirr="East"

    def step(self, num: int) -> None:
        total=((self.x+self.y-2)*2)
        num = num % total
        if num!=0:
            while num > 0:
            
                if self.curr[1] == 0 and self.curr[0] < self.x - 1:
                    self.curr[0] += 1
                    self.dirr="East"
                    # if self.curr[0] >= self.x - 1:
                    #     self.curr[1] += self.curr[0] - self.x + 1
                    #     self.curr[0] = self.x - 1
                elif self.curr[0] == self.x - 1 and self.curr[1] < self.y - 1:
                    self.curr[1] += 1
                    self.dirr="North"
                    # if self.curr[1] >= self.y - 1:
                    #     self.curr[0] -= self.curr[1] - self.y + 1
                    #     self.curr[1] = self.y - 1
                elif self.curr[1] == self.y - 1 and self.curr[0] > 0:
                    self.curr[0] -= 1
                    self.dirr="West"
                    # if self.curr[0] <= 0:
                    #     self.curr[1] -= abs(self.curr[0])
                    #     self.curr[0] = 0
                else:
                    self.curr[1] -= 1
                    self.dirr="South"
                    # if self.curr[1] <= 0:
                    #     self.curr[0] += abs(self.curr[1])
                    #     self.curr[1] = 0
                num -=1
        elif self.dirr=="East" and self.curr==[0,0]:
            self.dirr ="South"

        


    def getPos(self) -> List[int]:
        return self.curr

    def getDir(self) -> str:
        # if self.curr[1] == 0 and self.curr[0] < self.x-1:
        #     return "East"
        # elif self.curr[0] == self.x-1 and self.curr[1] < self.y-1:
        #     return "North"
        # elif self.curr[1] == self.y - 1 and self.curr[0] >= 0:
        #     return "West"
        # else:
        #     return "South"
        return self.dirr