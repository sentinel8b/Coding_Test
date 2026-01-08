N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

init_dir = 0
idx_x, idx_y = N // 2, N // 2
result = board[idx_x][idx_y]

for t in range(T):
    if str[t] == 'L':
        init_dir = (init_dir - 1) % 4
    elif str[t] == 'R':
        init_dir = (init_dir + 1) % 4
    elif str[t] == 'F':
        idx_x += dx[init_dir]
        idx_y += dy[init_dir]
        if idx_x < 0 or idx_x >= N or idx_y < 0 or idx_y >= N:
            idx_x -= dx[init_dir]
            idx_y -= dy[init_dir]
        else:
            result += board[idx_x][idx_y]

print(result)