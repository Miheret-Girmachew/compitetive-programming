class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        num2=num
        for i in range(t):
            num2+=1
        x=num2
        for i in range(t):
            x+=1
        return x
        
        