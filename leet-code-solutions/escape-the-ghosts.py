class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        ghost_distance=2**32
        for ghost in ghosts:
            curent_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            ghost_distance = min(curent_distance, ghost_distance)
        if distance < ghost_distance:
            return True
        else:
            return False
        