class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            check1=[]
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in check1:
                        return False
                    else:
                        check1.append(board[i][j])
        for j in range(len(board[0])):
            check2 = []
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in check2:
                        return False
                    else:
                        check2.append(board[i][j])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.':
                            if board[x][y] in box:
                                return False
                            else:
                                box.append(board[x][y])

        return True


      
     