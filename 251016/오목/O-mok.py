board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
n = 19
winner = 0

for i in range(2, n-2):
    for j in range(2, n-2):
        center_val = board[i][j]
        if center_val != 0:
            # 가로
            if board[i][j-2] == board[i][j-1] == board[i][j+1] == board[i][j+2] == center_val:
                winner = center_val
                print(winner)
                print(i+1, j+1)
                exit()
            # 세로
            if board[i-2][j] == board[i-1][j] == board[i+1][j] == board[i+2][j] == center_val:
                winner = center_val
                print(winner)
                print(i+1, j+1)
                exit()
            # 대각 (좌)
            if board[i-2][j-2] == board[i-1][j-1] == board[i+1][j+1] == board[i+2][j+2] == center_val:
                winner = center_val
                print(winner)
                print(i+1, j+1)
                exit()
            # 대각 (우)
            if board[i+2][j-2] == board[i+1][j-1] == board[i-1][j+1] == board[i-2][j+2] == center_val:
                winner = center_val
                print(winner)
                print(i+1, j+1)
                exit()
else:
    print(winner)
