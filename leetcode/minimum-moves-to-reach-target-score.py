class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        need = 0
        doubled = []
        if maxDoubles < 0 :
            return target - 1
        else:
            while target>1 and maxDoubles > 0:
                if target % 2 != 0:
                    target -= 1
                    need += 1
                if target % 2 == 0:
                    target = target // 2
                    need += 1
                    maxDoubles -= 1
            print(target)
            need += target - 1
        return need

            
                




        