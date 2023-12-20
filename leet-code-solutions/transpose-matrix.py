class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix2 = []
        for i in range(len(matrix[0])):
            small=[]
            for j in range(len(matrix)):
                small.append(matrix[j][i])
            matrix2.append(small)
        return matrix2

        