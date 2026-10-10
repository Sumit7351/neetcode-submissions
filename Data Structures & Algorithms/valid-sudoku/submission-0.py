class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        # Step 1: check every row
        for i in range(n):
            seen = set()  # a set holds each item only once
            for j in range(n):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # Step 2: check every column
        for j in range(n):
            seen = set()
            for i in range(n):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # Step 3: check every 3x3 box
        for k in range(0, n, 3):        # box start row: 0, 3, 6
            for l in range(0, n, 3):    # box start column: 0, 3, 6
                seen = set()
                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        val = board[i][j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True