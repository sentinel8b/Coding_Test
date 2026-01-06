n, m = map(int, input().split())

# Please write your code here.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

result_list = [[0 for _ in range(m)] for _ in range(n)]

idx_x, idx_y = 0, 0
init_dir = 0
tmp_val = 1
for i in range(n):
    for j in range(m):
        result_list[idx_x][idx_y] = tmp_val
        next_x = idx_x + dx[init_dir]
        next_y = idx_y + dy[init_dir]
        if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
            init_dir = (init_dir + 1) % 4
            idx_x += dx[init_dir]
            idx_y += dy[init_dir]
        elif result_list[next_x][next_y] != 0:
            init_dir = (init_dir + 1) % 4
            idx_x += dx[init_dir]
            idx_y += dy[init_dir]
        else:
            idx_x = next_x
            idx_y = next_y
        tmp_val += 1

for i in range(n):
    for j in range(m):
        if j == m-1:
            print(result_list[i][j])
        else:
            print(result_list[i][j], end=" ")