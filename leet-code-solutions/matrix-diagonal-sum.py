class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mainn=0
        subb = 0
        n = len(mat)
        for i in  range(n):
            for j in range(n):
                if i==j:
                    mainn+=mat[i][j]
                elif i+j==n-1 and i!=j:
                    subb+=mat[i][j]
        return subb + mainn
        
