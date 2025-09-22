n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
OFFSET = 100
GridSize = 200

grid = [
    [0] * (GridSize + 1) for _ in range(GridSize+1)
]

for i in range(n):
    x1_coord, x2_coord, y1_coord, y2_coord = x1[i] + OFFSET, x2[i] + OFFSET, y1[i] + OFFSET, y2[i] + OFFSET
    for x in range(x1_coord, x2_coord):
        for y in range(y1_coord, y2_coord):
            if i%2 == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = -1

val = 0
for x in range(GridSize+1):
    for y in range(GridSize+1):
        if grid[x][y] == -1:
            val += 1

print(val)