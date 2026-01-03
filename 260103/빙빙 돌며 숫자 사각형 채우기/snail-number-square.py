n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

count_list = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
init_x = 0
init_y = 0
init_dir = 0
result = 1
for i in range(n):
    for j in range(m):
        arr[init_x][init_y] = result
        count_list[init_x][init_y] = 1
        next_x = init_x + dx[init_dir]
        next_y = init_y + dy[init_dir]
        if next_x < n and next_x >= 0 and next_y < m and next_y >= 0:
            if count_list[next_x][next_y] != 1:
                init_x = next_x
                init_y = next_y
            else:
                init_dir = (init_dir + 1) % 4
                init_x += dx[init_dir]
                init_y += dy[init_dir]
        else:
            init_dir = (init_dir + 1) % 4
            init_x += dx[init_dir]
            init_y += dy[init_dir]
        result += 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j != len(arr[i]) - 1:
            print(arr[i][j],"", end="")
        else:
            print(arr[i][j])
