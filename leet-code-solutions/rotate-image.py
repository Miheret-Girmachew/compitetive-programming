class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        cols = len(matrix[0])
        rows = len(matrix)

        matrix2 = []
        for i in range(len(matrix[0])):
            small=[]
            for j in range(len(matrix)):
                small.append(matrix[j][i])
            matrix2.append(small)
        new=[]
        for matrixx in matrix2:
            matrixn = matrixx[::-1]
            new.append(matrixn)

        return neww
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(i,n-i-1):
                temp = matrix[j][n-1-i]
                matrix[j][n-1-i]  = matrix[i][j]

                temp2 = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = temp

                temp = temp2
                temp2 = matrix[n-1-j][i]
                
                matrix[n-1-j][i] = temp
                matrix[i][j] = temp2
                '''
                # reverse
l = 0
r = len(matrix) -1
while l < r:
	matrix[l], matrix[r] = matrix[r], matrix[l]
	l += 1
	r -= 1
# transpose 
for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		
        '''

        

            

            #    print(matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i])

             
                




        

        