n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

mat = [[0 for _ in range(n+2)] for _ in range(n+2)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(m):
    idx_x = points[i][0]
    idx_y = points[i][1]
    mat[idx_x][idx_y] = 1
    if mat[idx_x + dx[0]][idx_y + dy[0]] + mat[idx_x + dx[1]][idx_y + dy[1]] + mat[idx_x + dx[2]][idx_y + dy[2]] + mat[idx_x + dx[3]][idx_y + dy[3]] == 3:
        print(1)
    else:
        print(0)