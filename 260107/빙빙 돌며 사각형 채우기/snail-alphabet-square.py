n, m = map(int, input().split())

# Please write your code here.
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
a_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

result_list = [[0 for _ in range(m)] for _ in range(n)]
idx_x, idx_y = 0, 0
init_dir = 0
tmp_val = 0

for i in range(n):
    for j in range(m):
        result_list[idx_x][idx_y] = a_list[tmp_val]
        next_x = idx_x + dx[init_dir]
        next_y = idx_y + dy[init_dir]
        if (next_x >= 0 and next_x < n and next_y >= 0 and next_y < m) and (result_list[next_x][next_y] == 0):
            idx_x = next_x
            idx_y = next_y
        else:
            init_dir = (init_dir + 1) % 4
            idx_x += dx[init_dir]
            idx_y += dy[init_dir]
        tmp_val = (tmp_val + 1) % len(a_list)

for i in range(n):
    for j in range(m):
        if j == m-1:
            print(result_list[i][j])
        else:
            print(result_list[i][j], end=" ")