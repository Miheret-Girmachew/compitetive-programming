class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.pre = []
        for r in range(row + 1):
            self.pre.append([0] * (col + 1))
        for i in range(row):
            summ=0
            for j in range(col):
                summ+=matrix[i][j]
                before=self.pre[i][j+1]
                self.pre[i+1][j+1]= summ+before

        print(self.pre)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1+1
        col1=col1+1
        row2=row2+1
        col2=col2+1
         
        return self.pre[row2][col2] - self.pre[row1-1][col2]-self.pre[row2][col1-1] + self.pre[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)