class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hs = {}
        summ = 0
        for val in answers:
            if val not in hs:
                if val != 0:
                    hs[val] = val
                summ += 1
            else:
                summ += 1
                if hs[val] > 0:
                    hs[val] -= 1
                else:
                    hs[val] += val
                
        for val in hs:
            if hs[val] != 0:
                summ += hs[val]
        return summ


