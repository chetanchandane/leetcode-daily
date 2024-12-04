
def isValidSudoku(board):
    ver = dict(set)
    hor = dict(set)
    block = dict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in ver[c] 
            or board[r][c] in hor[r] 
            or board[r][c] in block[(r//3, c//3)]): return False

            ver[c].add(board[r][c])
            hor[r].add(board[r][c])
            block[(r // 3 , c // 3)].add(board[r][c])

    return True   