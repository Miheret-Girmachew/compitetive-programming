class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
            matrix = [[0] * n for _ in range(m)]

            for guard in guards:
                matrix[guard[0]][guard[1]] = "G"

            for wall in walls:
                matrix[wall[0]][wall[1]] = "W"

            for i in range(m):
                seen_guard = False
                for j in range(n):
                    if matrix[i][j] == "G":
                        seen_guard = True
                    elif matrix[i][j] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[i][j] = "x"

                seen_guard = False
                for j in range(n - 1, -1, -1):
                    if matrix[i][j] == "G":
                        seen_guard = True
                    elif matrix[i][j] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[i][j] = "x"

            for i in range(n):
                seen_guard = False
                for j in range(m):
                    if matrix[j][i] == "G":
                        seen_guard = True
                    elif matrix[j][i] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[j][i] = "x"

                seen_guard = False
                for j in range(m - 1, -1, -1):
                    if matrix[j][i] == "G":
                        seen_guard = True
                    elif matrix[j][i] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[j][i] = "x"

            count = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        count += 1
            return count