class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9

        for i in range(n):
            col=set()
            for j in range(n):
                if board[i][j]!=".":
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
                
                
        for j in range(n):
            row=set()
            for i in range(n):
                if board[i][j]!=".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        for k in range(0,9,3):
            for l in range(0,9,3):
                box=set()
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if board[i][j]!=".":
                            if board[i][j] in box:
                                return False
                            box.add(board[i][j])                 
        return True
