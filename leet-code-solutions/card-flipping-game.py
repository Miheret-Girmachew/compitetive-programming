class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:     
        set_equals = set()
        min_flips = 2**31
        for i in range(len(fronts)):
            if fronts [i] == backs[i]:
                set_equals.add(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] not in set_equals:
                min_flips = min(min_flips , fronts[i])
            if backs[i] not in set_equals:
                min_flips = min(min_flips , backs[i])
        if min_flips != 2**31:
            return min_flips
        else:
            return 0
        
        