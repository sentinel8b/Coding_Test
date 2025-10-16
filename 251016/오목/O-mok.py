board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
n = 19
winner = 0

dxs = [-1, 1, 0, 0, -1, -1, 1, 1] # N, S, W, E, NE, NW, SE, SW 
dys = [0, 0, -1, 1, 1, -1, 1, -1]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < 19 and y < 19


for i in range(n):
    for j in range(n):
        for dx, dy in zip(dxs, dys):
            if board[i][j] == 0:
                continue
            cur_x, cur_y = i, j
            curt = 1
            color = board[i][j]
            while True:
                if not in_range(cur_x + dx, cur_y + dy):
                    break
                if color != board[cur_x + dx][cur_y + dy]:
                    break
                curt += 1
                cur_x = cur_x + dx
                cur_y = cur_y + dy
            
            if curt == 5:
                print(board[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                exit()

else:
    print(0)