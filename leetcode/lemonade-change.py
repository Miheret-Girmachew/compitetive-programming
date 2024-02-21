class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                if fives == 0:
                    return False
                else:
                    fives -= 1
            elif bill == 20:
                if tens > 0:
                    tens -= 1
                    if fives > 0:
                        fives -= 1
                    else:
                        return False
                else:
                    if fives > 2:
                        fives -= 3
                    else:
                        return False
        return True

        

            
        