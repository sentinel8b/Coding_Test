n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

r, c = map(int, input().split())

r -= 1
c -= 1

power = grid[r][c]

grid[r][c] = 0
blast_range = power - 1

for i in range(1, blast_range + 1):
    if r - i >= 0:
        grid[r-i][c] = 0
    if r + i < n:
        grid[r+i][c] = 0
    if c - i >= 0:
        grid[r][c-i] = 0
    if c + i < n:
        grid[r][c+i] = 0

final_grid = [[0] * n for _ in range(n)]

for j in range(n):  
    write_row = n - 1 
    
    for i in range(n - 1, -1, -1): 
        if grid[i][j] > 0: 
            final_grid[write_row][j] = grid[i][j]
            write_row -= 1

for row in final_grid:
    print(*row)