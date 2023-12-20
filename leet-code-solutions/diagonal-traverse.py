class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
    
        for d in range(m + n - 1):
            if d % 2 == 0:
                i = min(d, m - 1)
                j = max(0, d - (m - 1))
                while i >= 0 and j < n:
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                i = max(0, d - (n - 1))
                j = min(d, n - 1)
                while i < m and j >= 0:
                    ans.append(mat[i][j])
                    i += 1
                    j -= 1

        return ans

        