class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []
        r = len(rowSum)
        c = len(colSum)
        for i in range(r):
            matrix.append([0]*c)
        for i in range(r):
            for j in range(c):
                matrix[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= matrix[i][j] 
                colSum[j] -= matrix[i][j] 
        return matrix
        