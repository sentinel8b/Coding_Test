board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

winner = 0
idx_x, idx_y = 0, 0

for i in range(19):
    for j in range(19):
        if i < 15:
            if [board[i][j], board[i+1][j], board[i+2][j], board[i+3][j], board[i+4][j]] == [1, 1, 1, 1, 1]:
                winner = 1
                idx_x, idx_y = i+2,j
            elif [board[i][j], board[i+1][j], board[i+2][j], board[i+3][j], board[i+4][j]] == [2, 2, 2, 2, 2]:
                winner = 2
                idx_x, idx_y = i+2,j
        if j < 15:
            if [board[i][j], board[i][j+1], board[i][j+2], board[i][j+3], board[i][j+4]] == [1, 1, 1, 1, 1]:
                winner = 1
                idx_x, idx_y = i+1,j+3
            elif [board[i][j], board[i][j+1], board[i][j+2], board[i][j+3], board[i][j+4]] == [2, 2, 2, 2, 2]:
                winner = 2
                idx_x, idx_y = i+1,j+3
        if i < 15 and j < 15:
            if [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]] == [1, 1, 1, 1, 1]:
                winner = 1
                idx_x, idx_y = i+3,j+3
            elif [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]] == [2, 2, 2, 2, 2]:
                winner = 2
                idx_x, idx_y = i+3,j+3
        if j >= 4 and i < 15:
            if [board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3], board[i+4][j-4]] == [1, 1, 1, 1, 1]:
                winner = 1
                idx_x, idx_y = i+3,j-1
            elif [board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3], board[i+4][j-4]] == [2, 2, 2, 2, 2]:
                winner = 2
                idx_x, idx_y = i+3,j-1

if winner == 0:
    print(winner)
else:
    print(winner)
    print(idx_x,idx_y)

        
        
