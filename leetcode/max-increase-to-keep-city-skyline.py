class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = []
        max_col = []
        ans = 0
        for val in grid:
            max_row.append(max(val))
        for i in range(len(grid)):
            maxx = 0
            for val in grid:
                maxx = max(maxx,val[i])
            max_col.append(maxx)
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = min(max_row[i],max_col[j])
                vall = val - grid[i][j]
                ans += vall
        return ans


